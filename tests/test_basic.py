from pathlib import Path

from llm_wiki.config import init_wiki, load_config, WikiConfig, LLMConfig
from llm_wiki.schema import PageType, WikiPage, _slugify, extract_wikilinks, load_page, find_page_by_title
from llm_wiki.utils import (
    compute_file_hash,
    compute_text_hash,
    extract_clean_content,
    get_all_wiki_pages,
    get_source_files,
    is_source_ingested,
    load_ingest_cache,
    mark_source_ingested,
    parse_source_metadata,
    save_ingest_cache,
    truncate_to_tokens,
    update_index,
)
from llm_wiki.search import bm25_search, keyword_search
from llm_wiki.lint import lint_wiki


def test_slugify():
    assert _slugify("Hello World") == "hello-world"
    assert _slugify("Transformer Architecture") == "transformer-architecture"
    assert _slugify("  spaces  ") == "spaces"


def test_extract_wikilinks():
    content = "See [[Attention Mechanism]] and [[Transformer]] for details."
    links = extract_wikilinks(content)
    assert links == ["Attention Mechanism", "Transformer"]


def test_wiki_page_to_markdown():
    page = WikiPage(
        title="Test Concept",
        page_type=PageType.CONCEPT,
        content="This is a test concept.",
        tags=["test"],
        related=["Other Concept"],
    )
    md = page.to_markdown()
    assert "---" in md
    assert "title:" in md
    assert "type:" in md and "concept" in md
    assert "[[Other Concept]]" in md


def test_wiki_page_save_and_load(tmp_path: Path):
    page = WikiPage(
        title="My Concept",
        page_type=PageType.CONCEPT,
        content="This is a concept about testing.",
        tags=["test", "unit-test"],
        related=["Testing"],
    )
    saved_path = page.save(tmp_path)
    assert saved_path.exists()

    loaded = load_page(saved_path)
    assert loaded.title == "My Concept"
    assert loaded.page_type == PageType.CONCEPT
    assert "testing" in loaded.content
    assert "test" in loaded.tags
    assert "Testing" in loaded.related


def test_init_wiki(tmp_path: Path):
    config = init_wiki(tmp_path)
    assert config.wiki_dir.exists()
    assert config.raw_dir.exists()
    assert config.index_path.exists()
    assert config.log_path.exists()
    assert (config.wiki_dir / "concepts").exists()
    assert (config.wiki_dir / "entities").exists()
    assert (config.raw_dir / "untracked").exists()
    assert (config.raw_dir / "ingested").exists()


def test_load_config(tmp_path: Path):
    init_wiki(tmp_path)
    config = load_config(tmp_path)
    assert config.root == tmp_path
    assert config.llm.model == "gpt-4o"


def test_raw_source_dir(tmp_path: Path):
    config = init_wiki(tmp_path)
    assert config.raw_source_dir == tmp_path / "raw" / "raw"


def test_hash_cache_path(tmp_path: Path):
    config = init_wiki(tmp_path)
    assert config.hash_cache_path == tmp_path / ".ingest_cache.json"


def test_compute_file_hash(tmp_path: Path):
    f = tmp_path / "test.txt"
    f.write_text("hello world", encoding="utf-8")
    h = compute_file_hash(f)
    assert len(h) == 64
    assert h == compute_file_hash(f)


def test_compute_text_hash():
    h = compute_text_hash("hello world")
    assert len(h) == 64
    assert h == compute_text_hash("hello world")
    assert h != compute_text_hash("hello world!")


def test_ingest_cache(tmp_path: Path):
    config = init_wiki(tmp_path)

    cache = load_ingest_cache(config)
    assert cache == {}

    cache["test/file.md"] = "abc123"
    save_ingest_cache(config, cache)

    loaded = load_ingest_cache(config)
    assert loaded["test/file.md"] == "abc123"


def test_is_source_ingested(tmp_path: Path):
    config = init_wiki(tmp_path)

    source_dir = config.raw_source_dir / "articles"
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / "test.md"
    source.write_text("# Test Article\n\nContent here.", encoding="utf-8")

    assert not is_source_ingested(config, source)

    mark_source_ingested(config, source)

    assert is_source_ingested(config, source)

    source.write_text("# Modified Article\n\nDifferent content.", encoding="utf-8")
    assert not is_source_ingested(config, source)


def test_get_source_files(tmp_path: Path):
    config = init_wiki(tmp_path)

    articles_dir = config.raw_source_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)
    (articles_dir / "article1.md").write_text("# Article 1", encoding="utf-8")
    (articles_dir / "article2.md").write_text("# Article 2", encoding="utf-8")

    videos_dir = config.raw_source_dir / "videos"
    videos_dir.mkdir(parents=True, exist_ok=True)
    (videos_dir / "video1.md").write_text("# Video 1", encoding="utf-8")

    files = get_source_files(config)
    assert len(files) == 3
    assert all(f.suffix == ".md" for f in files)


def test_parse_source_metadata_article():
    content = """# Test Article
## 文章信息
- **作者**: 张三
- **平台**: zhihu
- **标签**: AI, 知识库, LLM
## 内容
This is the content."""
    metadata = parse_source_metadata(content)
    assert metadata["type"] == "article"
    assert metadata["author"] == "张三"
    assert metadata["platform"] == "zhihu"
    assert "AI" in metadata["tags"]


def test_parse_source_metadata_video():
    content = """# Test Video
## 视频信息
- **作者**: 李四
- **平台**: bilibili
## 内容
Video content here."""
    metadata = parse_source_metadata(content)
    assert metadata["type"] == "video"
    assert metadata["author"] == "李四"


def test_extract_clean_content():
    content = """# Test Article
## 文章信息
- **作者**: 张三
- **平台**: zhihu
## 内容
This is the main content.
It has multiple lines."""
    clean = extract_clean_content(content)
    assert "main content" in clean
    assert "张三" not in clean


def test_truncate_to_tokens():
    short_text = "Hello world"
    result, was_truncated = truncate_to_tokens(short_text, max_tokens=100)
    assert not was_truncated
    assert result == short_text

    long_text = "word " * 50000
    result, was_truncated = truncate_to_tokens(long_text, max_tokens=100)
    assert was_truncated
    assert len(result) < len(long_text)


def test_update_index(tmp_path: Path):
    config = init_wiki(tmp_path)

    update_index(config, "Test Concept", PageType.CONCEPT, "A test concept")
    content = config.index_path.read_text(encoding="utf-8")
    assert "Test Concept" in content
    assert "A test concept" in content

    update_index(config, "Another Entity", PageType.ENTITY, "A test entity")
    content = config.index_path.read_text(encoding="utf-8")
    assert "Another Entity" in content


def test_get_all_wiki_pages(tmp_path: Path):
    config = init_wiki(tmp_path)

    page = WikiPage(
        title="Test Page",
        page_type=PageType.CONCEPT,
        content="Content",
    )
    page.save(config.wiki_dir)

    pages = get_all_wiki_pages(config.wiki_dir)
    assert len(pages) == 1


def test_find_page_by_title(tmp_path: Path):
    page = WikiPage(
        title="Unique Test Title",
        page_type=PageType.CONCEPT,
        content="Content",
    )
    page.save(tmp_path)

    found = find_page_by_title(tmp_path, "Unique Test Title")
    assert found is not None

    not_found = find_page_by_title(tmp_path, "Does Not Exist")
    assert not_found is None


def test_bm25_search(tmp_path: Path):
    page1 = WikiPage(
        title="Python Programming",
        page_type=PageType.CONCEPT,
        content="Python is a popular programming language used for web development, data science, and AI.",
    )
    page1.save(tmp_path)

    page2 = WikiPage(
        title="JavaScript Basics",
        page_type=PageType.CONCEPT,
        content="JavaScript is the language of the web, used for building interactive websites.",
    )
    page2.save(tmp_path)

    results = bm25_search(tmp_path, "python programming", top_k=5)
    assert len(results) >= 1
    result_stems = [r[0].stem for r in results]
    assert "python-programming" in result_stems


def test_keyword_search(tmp_path: Path):
    page1 = WikiPage(
        title="Machine Learning",
        page_type=PageType.CONCEPT,
        content="Machine learning is a subset of artificial intelligence.",
    )
    page1.save(tmp_path)

    results = keyword_search(tmp_path, ["machine", "learning"], top_k=5)
    assert len(results) >= 1


def test_lint_empty_wiki(tmp_path: Path):
    config = init_wiki(tmp_path)
    issues = lint_wiki(config)
    assert len(issues) >= 1
    assert any(i.category == "empty" for i in issues)


def test_lint_wiki_with_pages(tmp_path: Path):
    config = init_wiki(tmp_path)

    page = WikiPage(
        title="Standalone Page",
        page_type=PageType.CONCEPT,
        content="Short.",
    )
    page.save(config.wiki_dir)

    issues = lint_wiki(config)
    has_orphan = any(i.category == "orphan" for i in issues)
    has_shallow = any(i.category == "shallow" for i in issues)
    assert has_orphan or has_shallow


def test_page_type_enum():
    assert PageType.CONCEPT.value == "concept"
    assert PageType.ENTITY.value == "entity"
    assert PageType.SOURCE.value == "source"
    assert PageType.ANSWER.value == "answer"


def test_wiki_page_without_related():
    page = WikiPage(
        title="Simple Page",
        page_type=PageType.CONCEPT,
        content="Just content.",
    )
    md = page.to_markdown()
    assert "Simple Page" in md
    assert "Just content." in md


def test_llm_config_defaults():
    llm = LLMConfig()
    assert llm.model == "gpt-4o"
    assert llm.temperature == 0.3
    assert llm.max_tokens == 4096


def test_wiki_config_paths(tmp_path: Path):
    config = WikiConfig(root=tmp_path)
    assert config.wiki_dir == tmp_path / "wiki"
    assert config.raw_dir == tmp_path / "raw"
    assert config.raw_source_dir == tmp_path / "raw" / "raw"
    assert config.hash_cache_path == tmp_path / ".ingest_cache.json"
    assert config.index_path == tmp_path / "wiki" / "index.md"
    assert config.log_path == tmp_path / "wiki" / "log.md"
