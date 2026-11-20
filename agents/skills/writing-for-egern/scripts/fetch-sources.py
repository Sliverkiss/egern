#!/usr/bin/env python3
"""Collect community proxy-client modules for one app from GitHub.

    python3 fetch-sources.py <name-or-domain> [--out DIR]

Searches GitHub code search for Surge/Loon/QX/Egern modules matching the
query, downloads each raw file, and writes a manifest.json describing what
was fetched. Requires gh (authenticated) — code search does not work anon.

This is the gather step of the writing-for-egern skill; the absorb step
(merging + converting) is agent work, not scriptable dedup.
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import time
from pathlib import Path

GITHUB_RAW = "https://raw.githubusercontent.com"
RATE_SLEEP_SECONDS = 2
MAX_PER_QUERY = 8

QUERIES = [
    '"{q}" extension:sgmodule',
    '"{q}" extension:plugin',
    '"{q}" extension:conf 去广告',
    '"{q}" Egern extension:yaml',
]


def gh_api(endpoint: str) -> dict:
    result = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh api {endpoint}: {result.stderr.strip()}")
    return json.loads(result.stdout)


def code_search(query: str) -> list[dict]:
    import urllib.parse

    encoded = urllib.parse.quote(query)
    try:
        data = gh_api(f"search/code?q={encoded}&per_page={MAX_PER_QUERY}")
    except RuntimeError as error:
        print(f"  search failed: {error}", file=sys.stderr)
        return []
    return data.get("items", [])


def raw_url(item: dict) -> str:
    return f"{GITHUB_RAW}/{item['repository']['full_name']}/{item['repository'].get('default_branch', 'main')}/{item['path']}"


def fetch_raw(url: str) -> str:
    import urllib.request

    request = urllib.request.Request(url, headers={"User-Agent": "writing-for-egern/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="app name, Chinese name, or API domain")
    parser.add_argument("--out", default="sources", help="output directory")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict] = []
    seen_paths: set[str] = set()

    for template in QUERIES:
        query = template.format(q=args.query)
        print(f"search: {query}")
        items = code_search(query)
        for item in items:
            key = f"{item['repository']['full_name']}:{item['path']}"
            if key in seen_paths:
                continue
            seen_paths.add(key)
            url = raw_url(item)
            print(f"  fetch {key}")
            try:
                content = fetch_raw(url)
            except Exception as error:  # noqa: BLE001 — record and continue
                print(f"    error: {error}", file=sys.stderr)
                continue
            slug = key.replace("/", "-").replace(":", "-")
            target = out_dir / f"{slug}.{item['path'].rsplit('.', 1)[-1]}"
            target.write_text(content, encoding="utf-8")
            manifest.append(
                {
                    "repo": item["repository"]["full_name"],
                    "path": item["path"],
                    "raw_url": url,
                    "local": target.name,
                    "html_url": item["html_url"],
                }
            )
            time.sleep(RATE_SLEEP_SECONDS)

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nfetched {len(manifest)} files -> {out_dir}/ (manifest.json)")
    return 0 if manifest else 1


if __name__ == "__main__":
    sys.exit(main())
