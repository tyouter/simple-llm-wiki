from __future__ import annotations

import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Callable

import litellm

from .config import WikiConfig

_llm_callback: Callable[[str], str] | None = None

PROMPT_FILE = ".wiki_llm_prompt.json"
RESPONSE_FILE = ".wiki_llm_response.json"
BATCH_PROMPTS_FILE = ".wiki_llm_prompts.jsonl"
BATCH_RESPONSES_FILE = ".wiki_llm_responses.jsonl"


def set_llm_callback(callback: Callable[[str], str] | None) -> None:
    global _llm_callback
    _llm_callback = callback


def get_llm_callback() -> Callable[[str], str] | None:
    return _llm_callback


def _parse_jsonl(content: str) -> list[dict]:
    decoder = json.JSONDecoder()
    results = []
    pos = 0
    while pos < len(content):
        while pos < len(content) and content[pos] in " \t\r\n":
            pos += 1
        if pos >= len(content):
            break
        try:
            obj, end = decoder.raw_decode(content, pos)
            if isinstance(obj, dict):
                results.append(obj)
            pos += end
        except json.JSONDecodeError:
            next_brace = content.find("{", pos + 1)
            if next_brace == -1:
                break
            pos = next_brace
    return results


def call_llm(config: WikiConfig, prompt: str, retries: int = 3, timeout: int = 120) -> str:
    if _llm_callback is not None:
        return _llm_callback(prompt)

    callback_mode = os.getenv("WIKI_LLM_CALLBACK", "").lower()

    if callback_mode == "stdio":
        return _call_stdio(prompt)

    provider = config.llm.provider.lower()

    if provider == "agent":
        if callback_mode == "jsonl":
            return _call_agent_jsonl(config, prompt, retries)
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


def _call_stdio(prompt: str) -> str:
    prompt_data = {
        "prompt": prompt,
        "timestamp": time.time(),
    }
    sys.stdout.write(json.dumps(prompt_data, ensure_ascii=False) + "\n")
    sys.stdout.flush()

    line = sys.stdin.readline()
    if not line:
        raise RuntimeError("stdio callback: stdin closed unexpectedly")

    response_data = json.loads(line.strip())
    return response_data.get("response", "")


def _call_agent_file_protocol(config: WikiConfig, prompt: str, retries: int = 3) -> str:
    prompt_path = config.root / PROMPT_FILE
    response_path = config.root / RESPONSE_FILE

    if response_path.exists():
        response_path.unlink()

    prompt_id = uuid.uuid4().hex[:8]
    prompt_data = {
        "id": prompt_id,
        "prompt": prompt,
        "model": config.llm.model,
        "temperature": config.llm.temperature,
        "max_tokens": config.llm.max_tokens,
        "timestamp": time.time(),
    }
    prompt_path.write_text(json.dumps(prompt_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n[Agent LLM] Prompt #{prompt_id} written to {prompt_path}")
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


def _call_agent_jsonl(config: WikiConfig, prompt: str, retries: int = 3) -> str:
    prompts_path = config.root / BATCH_PROMPTS_FILE
    responses_path = config.root / BATCH_RESPONSES_FILE

    prompt_id = uuid.uuid4().hex[:8]
    prompt_entry = {
        "id": prompt_id,
        "prompt": prompt,
        "model": config.llm.model,
        "temperature": config.llm.temperature,
        "max_tokens": config.llm.max_tokens,
        "timestamp": time.time(),
    }

    with open(prompts_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(prompt_entry, ensure_ascii=True) + "\n")

    print(f"[Agent LLM] Prompt #{prompt_id} appended to {prompts_path}")

    max_wait = 600
    poll_interval = 2
    waited = 0

    while waited < max_wait:
        if responses_path.exists():
            try:
                content = responses_path.read_text(encoding="utf-8")
                entries = _parse_jsonl(content)
                for data in entries:
                    if data.get("id") == prompt_id:
                        response = data.get("response", "")
                        _cleanup_jsonl_entry(config, prompt_id)
                        return response
            except (json.JSONDecodeError, KeyError):
                pass

        time.sleep(poll_interval)
        waited += poll_interval

        if waited % 10 == 0:
            print(f"[Agent LLM] Still waiting for #{prompt_id}... ({waited}s / {max_wait}s)")

    _cleanup_jsonl_entry(config, prompt_id)
    raise TimeoutError(f"Agent LLM JSONL response for #{prompt_id} not received within {max_wait}s")


def _cleanup_jsonl_entry(config: WikiConfig, prompt_id: str) -> None:
    prompts_path = config.root / BATCH_PROMPTS_FILE
    responses_path = config.root / BATCH_RESPONSES_FILE

    remaining_prompts = []
    if prompts_path.exists():
        content = prompts_path.read_text(encoding="utf-8")
        entries = _parse_jsonl(content)
        for data in entries:
            if data.get("id") != prompt_id:
                remaining_prompts.append(json.dumps(data, ensure_ascii=True))

    if remaining_prompts:
        with open(prompts_path, "w", encoding="utf-8") as f:
            f.write("\n".join(remaining_prompts) + "\n")
    else:
        prompts_path.unlink(missing_ok=True)
        responses_path.unlink(missing_ok=True)
