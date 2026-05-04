from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Callable

import litellm

from .config import WikiConfig

_llm_callback: Callable[[str], str] | None = None

PROMPT_FILE = ".wiki_llm_prompt.json"
RESPONSE_FILE = ".wiki_llm_response.json"


def set_llm_callback(callback: Callable[[str], str] | None) -> None:
    global _llm_callback
    _llm_callback = callback


def get_llm_callback() -> Callable[[str], str] | None:
    return _llm_callback


def call_llm(config: WikiConfig, prompt: str, retries: int = 3, timeout: int = 120) -> str:
    if _llm_callback is not None:
        return _llm_callback(prompt)

    provider = config.llm.provider.lower()

    if provider == "agent":
        return _call_agent_file_protocol(config, prompt, retries)
    else:
        return _call_api_llm(config, prompt, retries, timeout)


def _call_api_llm(config: WikiConfig, prompt: str, retries: int = 3, timeout: int = 120) -> str:
    last_error = None
    for attempt in range(retries):
        try:
            response = litellm.completion(
                model=config.llm.model,
                messages=[{"role": "user", "content": prompt}],
                api_key=config.llm.api_key or None,
                api_base=config.llm.base_url,
                temperature=config.llm.temperature,
                max_tokens=config.llm.max_tokens,
                timeout=timeout,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    raise last_error


def _call_agent_file_protocol(config: WikiConfig, prompt: str, retries: int = 3) -> str:
    prompt_path = config.root / PROMPT_FILE
    response_path = config.root / RESPONSE_FILE

    if response_path.exists():
        response_path.unlink()

    prompt_data = {
        "prompt": prompt,
        "model": config.llm.model,
        "temperature": config.llm.temperature,
        "max_tokens": config.llm.max_tokens,
        "timestamp": time.time(),
    }
    prompt_path.write_text(json.dumps(prompt_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n[Agent LLM] Prompt written to {prompt_path}")
    print(f"[Agent LLM] Waiting for response at {response_path} ...")
    print(f"[Agent LLM] Run: wiki agent-respond")
    print(f"[Agent LLM] Or manually write JSON {{\"response\": \"...\"}} to {response_path}\n")

    max_wait = 600
    poll_interval = 2
    waited = 0

    while waited < max_wait:
        if response_path.exists():
            try:
                data = json.loads(response_path.read_text(encoding="utf-8"))
                response = data.get("response", "")
                prompt_path.unlink(missing_ok=True)
                response_path.unlink(missing_ok=True)
                return response
            except (json.JSONDecodeError, KeyError):
                if waited > 10:
                    print(f"[Agent LLM] Invalid response file, retry {retries}...")
                    break

        time.sleep(poll_interval)
        waited += poll_interval

        if waited % 10 == 0:
            print(f"[Agent LLM] Still waiting... ({waited}s / {max_wait}s)")

    prompt_path.unlink(missing_ok=True)
    response_path.unlink(missing_ok=True)
    raise TimeoutError(f"Agent LLM response not received within {max_wait}s")
