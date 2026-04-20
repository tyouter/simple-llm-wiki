from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from .config import WikiConfig, init_wiki, load_config
from .lint import lint_wiki
from .search import bm25_search
from .schema import PageType
from .utils import get_all_wiki_pages, get_raw_sources, get_source_files, is_source_ingested, load_ingest_cache, compute_file_hash

console = Console()


def _find_wiki_root() -> Path:
    current = Path.cwd()
    while current != current.parent:
        if (current / ".wikirc.yaml").exists():
            return current
        current = current.parent
    return Path.cwd()


def _load() -> WikiConfig:
    return load_config(_find_wiki_root())


@click.group()
@click.version_option(package_name="llm-wiki")
def cli():
    """LLM Wiki — A personal knowledge base that builds itself."""
    pass


@cli.command()
@click.option("--root", default=".", help="Directory to initialize the wiki in")
def init(root: str):
    """Initialize a new wiki in the current or specified directory."""
    root_path = Path(root).resolve()
    config = init_wiki(root_path)

    source_dir = config.raw_source_dir
    source_count = 0
    if source_dir.exists():
        source_count = len(get_source_files(config))

    console.print(Panel.fit(
        f"[bold green]Wiki initialized![/bold green]\n\n"
        f"Root: {config.root}\n"
        f"Config: {config.config_path}\n"
        f"Raw sources: {config.raw_dir}\n"
        f"Source data: {source_dir} ({source_count} files)\n"
        f"Wiki pages: {config.wiki_dir}\n\n"
        f"Next steps:\n"
        f"1. Edit [cyan]{config.config_path}[/cyan] to set your LLM API key\n"
        f"2. Run [cyan]wiki ingest --all[/cyan] to process sources\n"
        f"3. Run [cyan]wiki query \"your question\"[/cyan] to ask questions",
        title="LLM Wiki",
    ))


@cli.command()
@click.argument("source", required=False)
@click.option("--url", help="Ingest from a URL instead of a file")
@click.option("--all", "ingest_all", is_flag=True, help="Ingest all available sources")
@click.option("--max", "max_sources", default=0, help="Max sources to ingest (0=all)")
@click.option("--workers", default=2, help="Number of parallel workers for batch ingest")
@click.option("--dry-run", is_flag=True, help="Preview without writing")
def ingest(source: str | None, url: str | None, ingest_all: bool, max_sources: int, workers: int, dry_run: bool):
    """Process a source document into the wiki."""
    from .ingest import batch_ingest, ingest_source, ingest_url as ingest_url_fn

    config = _load()

    if url:
        console.print(f"[cyan]Fetching URL:[/cyan] {url}")
        try:
            pages = ingest_url_fn(config, url, dry_run=dry_run)
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)
    elif ingest_all:
        console.print("[cyan]Batch ingesting all sources...[/cyan]")
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Processing...", total=None)
                pages = batch_ingest(config, max_sources=max_sources, dry_run=dry_run, workers=workers)
                progress.update(task, completed=True)
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)
    elif source:
        source_path = Path(source).resolve()
        if not source_path.exists():
            console.print(f"[red]File not found:[/red] {source_path}")
            sys.exit(1)
        console.print(f"[cyan]Ingesting:[/cyan] {source_path.name}")
        try:
            pages = ingest_source(config, source_path, dry_run=dry_run)
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)
    else:
        all_sources = get_source_files(config)
        cache = load_ingest_cache(config)
        ingested_set = set()
        for s in all_sources:
            try:
                key = str(s.relative_to(config.root))
                current_hash = compute_file_hash(s)
                if cache.get(key) == current_hash:
                    ingested_set.add(s)
            except (ValueError, OSError):
                pass
        uningested = [s for s in all_sources if s not in ingested_set]

        if not all_sources:
            console.print("[yellow]No source files found.[/yellow]")
            return

        console.print(f"[bold]Available sources ({len(uningested)} uningested / {len(all_sources)} total):[/bold]")

        display_sources = uningested[:20]
        for i, src in enumerate(display_sources, 1):
            try:
                rel = str(src.relative_to(config.root))
            except ValueError:
                rel = str(src)
            console.print(f"  {i}. {rel}")

        if len(uningested) > 20:
            console.print(f"  ... and {len(uningested) - 20} more. Use --all to ingest all.")

        console.print(f"\n[dim]Tip: Use 'wiki ingest --all' to ingest all, or 'wiki ingest <file>' for a specific file.[/dim]")
        return

    if dry_run:
        console.print(f"\n[bold]Dry run — {len(pages)} pages would be created:[/bold]")
    else:
        console.print(f"\n[bold green]Created/updated {len(pages)} pages:[/bold green]")

    for page in pages:
        type_emoji = {"concept": "💡", "entity": "🏷️", "source": "📄", "answer": "💬"}.get(
            page.page_type.value, "📝"
        )
        console.print(f"  {type_emoji} [{page.page_type.value}] {page.title}")


@cli.command()
@click.argument("question")
@click.option("--save", is_flag=True, help="Save the answer as a wiki page if novel")
def query(question: str, save: bool):
    """Ask a question against the wiki."""
    from .query import query_wiki

    config = _load()
    console.print(f"[cyan]Searching wiki for:[/cyan] {question}")

    try:
        answer = query_wiki(config, question, save=save)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    console.print()
    console.print(Panel(answer, title="Answer", border_style="green"))

    if save:
        console.print("[dim]Answer saved to wiki if it was novel.[/dim]")


@cli.command()
def lint():
    """Health-check the wiki for issues."""
    config = _load()
    issues = lint_wiki(config)

    if not issues:
        console.print("[bold green]Wiki is healthy — no issues found![/bold green]")
        return

    severity_colors = {"error": "red", "warning": "yellow", "info": "blue"}

    table = Table(title="Wiki Lint Results")
    table.add_column("Severity", style="bold")
    table.add_column("Category")
    table.add_column("Page")
    table.add_column("Description")

    for issue in issues:
        color = severity_colors.get(issue.severity, "white")
        table.add_row(
            f"[{color}]{issue.severity}[/{color}]",
            issue.category,
            issue.page,
            issue.description,
        )

    console.print(table)

    error_count = sum(1 for i in issues if i.severity == "error")
    warning_count = sum(1 for i in issues if i.severity == "warning")
    info_count = sum(1 for i in issues if i.severity == "info")

    console.print(
        f"\n[red]{error_count} errors[/red], "
        f"[yellow]{warning_count} warnings[/yellow], "
        f"[blue]{info_count} info[/blue]"
    )


@cli.command("list")
@click.argument("type", type=click.Choice(["raw", "pages", "orphans", "sources"]))
def list_content(type: str):
    """List wiki contents."""
    config = _load()

    if type == "raw":
        untracked = get_raw_sources(config.raw_dir, ingested=False)
        ingested = get_raw_sources(config.raw_dir, ingested=True)

        console.print(f"[bold]Untracked sources ({len(untracked)}):[/bold]")
        for src in untracked:
            console.print(f"  📥 {src.relative_to(config.raw_dir)}")

        console.print(f"\n[bold]Ingested sources ({len(ingested)}):[/bold]")
        for src in ingested:
            console.print(f"  ✅ {src.relative_to(config.raw_dir)}")

    elif type == "sources":
        all_sources = get_source_files(config)
        cache = load_ingest_cache(config)
        ingested_set = set()
        for src in all_sources:
            try:
                key = str(src.relative_to(config.root))
                current_hash = compute_file_hash(src)
                if cache.get(key) == current_hash:
                    ingested_set.add(src)
            except (ValueError, OSError):
                pass

        uningested = [s for s in all_sources if s not in ingested_set]
        console.print(f"[bold]Source files ({len(uningested)} uningested / {len(all_sources)} total):[/bold]")

        display_sources = all_sources[:50]
        for src in display_sources:
            status = "✅" if src in ingested_set else "📥"
            try:
                rel = str(src.relative_to(config.root))
            except ValueError:
                rel = str(src)
            console.print(f"  {status} {rel}")

        if len(all_sources) > 50:
            console.print(f"  ... and {len(all_sources) - 50} more.")

    elif type == "pages":
        pages = get_all_wiki_pages(config.wiki_dir)
        if not pages:
            console.print("[yellow]No wiki pages yet.[/yellow]")
            return

        table = Table(title="Wiki Pages")
        table.add_column("Type")
        table.add_column("Title")
        table.add_column("Path")

        for path in sorted(pages):
            try:
                from .schema import load_page
                page = load_page(path)
                type_emoji = {"concept": "💡", "entity": "🏷️", "source": "📄", "answer": "💬"}.get(
                    page.page_type.value, "📝"
                )
                table.add_row(f"{type_emoji} {page.page_type.value}", page.title, str(path.relative_to(config.wiki_dir)))
            except Exception:
                table.add_row("❓ unknown", path.stem, str(path.relative_to(config.wiki_dir)))

        console.print(table)

    elif type == "orphans":
        issues = lint_wiki(config)
        orphans = [i for i in issues if i.category == "orphan"]
        if not orphans:
            console.print("[green]No orphan pages found.[/green]")
            return
        for issue in orphans:
            console.print(f"  🔗 {issue.page}: {issue.description}")


@cli.command()
@click.argument("query_str")
@click.option("--top-k", default=10, help="Number of results to return")
def search(query_str: str, top_k: int):
    """Search wiki pages by keyword."""
    config = _load()
    results = bm25_search(config.wiki_dir, query_str, top_k=top_k)

    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    table = Table(title=f"Search Results: {query_str}")
    table.add_column("Score", justify="right", style="bold")
    table.add_column("Type")
    table.add_column("Title")
    table.add_column("Path")

    from .schema import load_page

    for path, score in results:
        try:
            page = load_page(path)
            type_emoji = {"concept": "[C]", "entity": "[E]", "source": "[S]", "answer": "[A]"}.get(
                page.page_type.value, "[?]"
            )
            table.add_row(
                f"{score:.2f}",
                f"{type_emoji} {page.page_type.value}",
                page.title,
                str(path.relative_to(config.wiki_dir)),
            )
        except Exception:
            table.add_row(f"{score:.2f}", "❓", path.stem, str(path.relative_to(config.wiki_dir)))

    console.print(table)


@cli.command()
def stats():
    """Show wiki statistics."""
    config = _load()
    pages = get_all_wiki_pages(config.wiki_dir)
    all_sources = get_source_files(config)
    cache = load_ingest_cache(config)
    ingested_count = 0
    for s in all_sources:
        try:
            key = str(s.relative_to(config.root))
            current_hash = compute_file_hash(s)
            if cache.get(key) == current_hash:
                ingested_count += 1
        except (ValueError, OSError):
            pass

    type_counts: dict[str, int] = {}
    total_words = 0
    all_tags: set[str] = set()
    all_links: set[str] = set()

    from .schema import load_page

    for path in pages:
        try:
            page = load_page(path)
            type_counts[page.page_type.value] = type_counts.get(page.page_type.value, 0) + 1
            total_words += len(page.content.split())
            all_tags.update(page.tags)
            from .schema import extract_wikilinks
            all_links.update(extract_wikilinks(page.to_markdown()))
        except Exception:
            pass

    table = Table(title="Wiki Statistics")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    table.add_row("Total wiki pages", str(len(pages)))
    for ptype, count in sorted(type_counts.items()):
        table.add_row(f"  {ptype}", str(count))
    table.add_row("Total words", f"{total_words:,}")
    table.add_row("Unique tags", str(len(all_tags)))
    table.add_row("Cross-references", str(len(all_links)))
    table.add_row("Source files", str(len(all_sources)))
    table.add_row("Ingested sources", str(ingested_count))
    table.add_row("Pending sources", str(len(all_sources) - ingested_count))

    console.print(table)


@cli.command()
@click.option("--language", type=click.Choice(["cn", "en", "as_origin"]), help="Set output language mode")
@click.option("--model", help="Set LLM model")
@click.option("--api-key", help="Set API key")
@click.option("--base-url", help="Set API base URL")
@click.option("--show", is_flag=True, help="Show current configuration")
def config(language: str | None, model: str | None, api_key: str | None, base_url: str | None, show: bool):
    """View or modify wiki configuration."""
    from .config import save_config

    wiki_config = _load()

    if show or not any([language, model, api_key, base_url]):
        # Show current config
        table = Table(title="Current Configuration")
        table.add_column("Setting", style="bold")
        table.add_column("Value")

        table.add_row("Language", wiki_config.language)
        table.add_row("LLM Provider", wiki_config.llm.provider)
        table.add_row("LLM Model", wiki_config.llm.model)
        table.add_row("API Base URL", wiki_config.llm.base_url)
        table.add_row("Temperature", str(wiki_config.llm.temperature))
        table.add_row("Max Tokens", str(wiki_config.llm.max_tokens))
        table.add_row("Config File", str(wiki_config.config_path))

        console.print(table)
        console.print("\n[dim]Tip: Use 'wiki config --language cn' to change language mode.[/dim]")
        return

    # Update config
    changed = []
    if language:
        wiki_config.language = language
        changed.append(f"language: {language}")
    if model:
        wiki_config.llm.model = model
        changed.append(f"model: {model}")
    if api_key:
        wiki_config.llm.api_key = api_key
        changed.append("api_key: (updated)")
    if base_url:
        wiki_config.llm.base_url = base_url
        changed.append(f"base_url: {base_url}")

    save_config(wiki_config)

    console.print("[bold green]Configuration updated:[/bold green]")
    for change in changed:
        console.print(f"  - {change}")


@cli.command()
@click.argument("keyword_args", nargs=-1, required=True)
@click.option("--top-k", default=10, help="Number of results to return")
def keywords(keyword_args: tuple[str, ...], top_k: int):
    """Exact keyword search (match all keywords)."""
    from .search import keyword_search

    config = _load()
    keyword_list = list(keyword_args)
    results = keyword_search(config.wiki_dir, keyword_list, top_k=top_k)

    if not results:
        console.print(f"[yellow]No pages found with keywords: {keyword_list}[/yellow]")
        return

    table = Table(title=f"Keyword Results: {keyword_list}")
    table.add_column("Matches", justify="right", style="bold")
    table.add_column("Type")
    table.add_column("Title")
    table.add_column("Path")

    from .schema import load_page

    for path, match_count in results:
        try:
            page = load_page(path)
            type_emoji = {"concept": "[C]", "entity": "[E]", "source": "[S]", "answer": "[A]"}.get(
                page.page_type.value, "[?]"
            )
            table.add_row(
                str(match_count),
                f"{type_emoji} {page.page_type.value}",
                page.title,
                str(path.relative_to(config.wiki_dir)),
            )
        except Exception:
            table.add_row(str(match_count), "❓", path.stem, str(path.relative_to(config.wiki_dir)))

    console.print(table)


@cli.command()
@click.argument("path")
def tokens(path: str):
    """Estimate token count for a file or wiki page."""
    from .utils import count_tokens_approx

    file_path = Path(path).resolve()
    if not file_path.exists():
        console.print(f"[red]File not found:[/red] {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    token_count = count_tokens_approx(content)

    console.print(Panel.fit(
        f"[bold]File:[/bold] {file_path.name}\n"
        f"[bold]Characters:[/bold] {len(content):,}\n"
        f"[bold]Words:[/bold] {len(content.split()):,}\n"
        f"[bold]Estimated Tokens:[/bold] {token_count:,}",
        title="Token Estimate",
    ))


@cli.command()
@click.argument("page_title")
@click.option("--resolve", is_flag=True, help="Show resolved file paths")
def links(page_title: str, resolve: bool):
    """Show wikilinks in a page."""
    from .schema import load_page, extract_wikilinks, find_page_by_title
    from .utils import resolve_wikilinks as resolve_links_fn

    config = _load()

    # Find the page by title
    page_path = find_page_by_title(config.wiki_dir, page_title)
    if not page_path:
        console.print(f"[yellow]Page not found:[/yellow] {page_title}")
        console.print("[dim]Tip: Use exact page title as stored in wiki[/dim]")
        return

    page = load_page(page_path)
    wikilinks = extract_wikilinks(page.to_markdown())

    if not wikilinks:
        console.print(f"[yellow]No wikilinks found in:[/yellow] {page_title}")
        return

    if resolve:
        resolved = resolve_links_fn(config, page.to_markdown())
        table = Table(title=f"Wikilinks in {page_title} (Resolved)")
        table.add_column("Link")
        table.add_column("Resolved Path")
        table.add_column("Status")

        for link, resolved_path in zip(wikilinks, resolved):
            if resolved_path.exists():
                status = "[green]OK[/green]"
            else:
                status = "[red]Missing[/red]"
            table.add_row(f"[[{link}]]", str(resolved_path.relative_to(config.wiki_dir)) if resolved_path else "-", status)

        console.print(table)
    else:
        console.print(f"[bold]Wikilinks in {page_title}:[/bold] ({len(wikilinks)} links)")
        for link in wikilinks:
            console.print(f"  [[{link}]]")


@cli.command()
@click.argument("action", type=click.Choice(["parse", "query", "lint", "stats"]))
@click.option("--source", help="Source file to deep parse")
@click.option("--all", "parse_all", is_flag=True, help="Deep parse all pending sources")
@click.option("--max", "max_sources", default=0, help="Max sources to parse (0=all)")
@click.option("--workers", default=2, help="Parallel workers for batch processing")
@click.option("--question", help="Question for deep query")
@click.option("--top-k", default=20, help="Context pages for deep query")
def deep(action: str, source: str | None, parse_all: bool, max_sources: int, workers: int, question: str | None, top_k: int):
    """Deep operations with enhanced analysis and bidirectional linking."""
    from .deep import deep_parse_source, deep_query_wiki, deep_lint_wiki, deep_stats, batch_deep_parse

    config = _load()

    if action == "parse":
        if parse_all:
            console.print("[cyan]Batch deep parsing all pending sources...[/cyan]")
            console.print("[dim]This may take a while - extracting 10-15 concepts per source[/dim]")

            try:
                console.print("[dim]Processing...[/dim]")
                results = batch_deep_parse(config, max_sources=max_sources, workers=workers)

                total_pages = sum(len(pages) for pages in results)
                console.print(f"\n[bold green]Deep parsed {len(results)} sources, {total_pages} pages created/enriched[/bold green]")

                # Summary stats
                concepts_created = 0
                entities_created = 0
                links_added = 0

                for pages in results:
                    for page in pages:
                        if page.page_type == PageType.CONCEPT:
                            concepts_created += 1
                        elif page.page_type == PageType.ENTITY:
                            entities_created += 1
                        links_added += len(page.related)

                console.print(f"[dim]Concepts: {concepts_created} | Entities: {entities_created} | Links added: {links_added}[/dim]")

            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")
                sys.exit(1)

        elif source:
            source_path = Path(source).resolve()
            if not source_path.exists():
                console.print(f"[red]Source not found:[/red] {source_path}")
                sys.exit(1)

            console.print(f"[cyan]Deep parsing with bidirectional linking:[/cyan] {source_path.name}")

            try:
                pages = deep_parse_source(config, source_path)
                console.print(f"\n[bold green]Created/enriched {len(pages)} pages with deep analysis[/bold green]")

                table = Table(title="Deep Parse Results")
                table.add_column("Type")
                table.add_column("Title")
                table.add_column("Related Links")

                for page in pages:
                    type_label = {"concept": "[C]", "entity": "[E]", "source": "[S]", "answer": "[A]"}.get(
                        page.page_type.value, "[?]"
                    )
                    related_str = ", ".join(page.related[:3]) if page.related else "-"
                    table.add_row(type_label, page.title, related_str)

                console.print(table)

            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")
                sys.exit(1)
        else:
            console.print("[yellow]Use --source <file> or --all for batch processing[/yellow]")
            console.print("[dim]Examples:")
            console.print("  wiki deep parse --source raw/articles/file.md")
            console.print("  wiki deep parse --all --workers 4[/dim]")

    elif action == "query":
        if not question:
            console.print("[yellow]Use --question for deep query[/yellow]")
            return

        console.print(f"[cyan]Deep query with {top_k} context pages...[/cyan]")

        try:
            answer = deep_query_wiki(config, question, top_k=top_k)
            console.print()
            console.print(Panel(answer, title="Deep Answer", border_style="green"))

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    elif action == "lint":
        console.print("[cyan]Deep linting with bidirectional link analysis...[/cyan]")

        try:
            issues = deep_lint_wiki(config)

            if not issues:
                console.print("[bold green]No deep issues found - all links bidirectional[/bold green]")
                return

            # Group by category
            categories = {}
            for issue in issues:
                cat = getattr(issue, "category", "unknown")
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(issue)

            for cat, cat_issues in categories.items():
                console.print(f"\n[bold]{cat}:[/bold] ({len(cat_issues)} issues)")
                for issue in cat_issues[:5]:
                    pages = getattr(issue, "pages", "-")
                    desc = getattr(issue, "description", "-")
                    console.print(f"  {pages}: {desc}")

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    elif action == "stats":
        console.print("[cyan]Deep statistics with quality metrics...[/cyan]")

        try:
            stats_data = deep_stats(config)

            table = Table(title="Deep Statistics")
            table.add_column("Metric", style="bold")
            table.add_column("Value")

            for key, value in stats_data.items():
                table.add_row(key, str(value))

            console.print(table)

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)


if __name__ == "__main__":
    cli()
