from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


WIKI_DIR_NAME = "wiki"
RAW_DIR_NAME = "raw"
CONFIG_FILE = ".wikirc.yaml"
INDEX_FILE = "index.md"
LOG_FILE = "log.md"
OVERVIEW_FILE = "overview.md"
HASH_CACHE_FILE = ".ingest_cache.json"

WIKI_SUBDIRS = ["concepts", "entities", "sources", "answers"]
RAW_SUBDIRS = ["untracked", "ingested"]
RAW_SOURCE_SUBDIRS = ["articles", "videos"]


@dataclass
class LLMConfig:
    provider: str = "openai"
    model: str = "gpt-4o"
    api_key: str = ""
    base_url: str = "https://api.openai.com/v1"
    temperature: float = 0.3
    max_tokens: int = 4096


@dataclass
class WikiConfig:
    root: Path = field(default_factory=Path.cwd)
    llm: LLMConfig = field(default_factory=LLMConfig)

    @property
    def wiki_dir(self) -> Path:
        return self.root / WIKI_DIR_NAME

    @property
    def raw_dir(self) -> Path:
        return self.root / RAW_DIR_NAME

    @property
    def raw_source_dir(self) -> Path:
        return self.root / RAW_DIR_NAME

    @property
    def hash_cache_path(self) -> Path:
        return self.root / HASH_CACHE_FILE

    @property
    def index_path(self) -> Path:
        return self.wiki_dir / INDEX_FILE

    @property
    def log_path(self) -> Path:
        return self.wiki_dir / LOG_FILE

    @property
    def overview_path(self) -> Path:
        return self.wiki_dir / OVERVIEW_FILE

    @property
    def config_path(self) -> Path:
        return self.root / CONFIG_FILE


def load_config(root: Path | None = None) -> WikiConfig:
    root = root or Path.cwd()
    config_path = root / CONFIG_FILE

    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {}

    llm_data = data.get("llm", {})
    env_api_key = os.getenv("WIKI_LLM_API_KEY", "") or os.getenv("DEEPSEEK_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")
    env_model = os.getenv("WIKI_LLM_MODEL", "")
    env_base_url = os.getenv("WIKI_LLM_BASE_URL", "")

    llm = LLMConfig(
        provider=llm_data.get("provider", "openai"),
        model=env_model or llm_data.get("model", "gpt-4o"),
        api_key=env_api_key or llm_data.get("apiKey", ""),
        base_url=env_base_url or llm_data.get("baseUrl", "https://api.openai.com/v1"),
        temperature=llm_data.get("temperature", 0.3),
        max_tokens=llm_data.get("max_tokens", 4096),
    )

    return WikiConfig(root=root, llm=llm)


def save_config(config: WikiConfig) -> None:
    data = {
        "llm": {
            "provider": config.llm.provider,
            "model": config.llm.model,
            "apiKey": config.llm.api_key,
            "baseUrl": config.llm.base_url,
            "temperature": config.llm.temperature,
            "max_tokens": config.llm.max_tokens,
        }
    }
    with open(config.config_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def init_wiki(root: Path) -> WikiConfig:
    root.mkdir(parents=True, exist_ok=True)

    raw_dir = root / RAW_DIR_NAME
    wiki_dir = root / WIKI_DIR_NAME

    for subdir in RAW_SUBDIRS:
        (raw_dir / subdir).mkdir(parents=True, exist_ok=True)

    for subdir in WIKI_SUBDIRS:
        (wiki_dir / subdir).mkdir(parents=True, exist_ok=True)

    config = load_config(root)
    save_config(config)

    if not config.index_path.exists():
        config.index_path.write_text(_default_index(), encoding="utf-8")

    if not config.log_path.exists():
        config.log_path.write_text(_default_log(), encoding="utf-8")

    if not config.overview_path.exists():
        config.overview_path.write_text(_default_overview(), encoding="utf-8")

    return config


def _default_index() -> str:
    return """# Wiki Index

This is the content catalog for your personal knowledge base.
The LLM updates this file on every ingest.

## Concepts

*(none yet)*

## Entities

*(none yet)*

## Sources

*(none yet)*

## Answers

*(none yet)*
"""


def _default_log() -> str:
    return """# Wiki Log

Chronological record of wiki operations.
Format: ## [YYYY-MM-DD] operation | description

"""


def _default_overview() -> str:
    return """# Wiki Overview

This is the evolving synthesis of everything in the wiki.
The LLM updates this page as new knowledge is integrated.

*(This overview will grow as you add sources.)*
"""
