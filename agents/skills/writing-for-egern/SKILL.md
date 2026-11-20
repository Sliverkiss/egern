---
name: writing-for-egern
description: >
  Build Egern modules by absorbing community Surge, Loon, Quantumult X and
  Egern modules for the same app. Fire on requests to write, port, or
  collect an Egern module for a named app or domain — 去广告, 重写, 模块,
  ad-block, rewrite. Matches: Egern 模块, sgmodule,loon plugin, qx conf 转
  Egern.
---

# Writing for Egern — module absorption

Absorb: gather every community module for the target app across Surge,
Loon, QX and Egern, merge them, convert to one native Egern module, verify
against the docs. The output is always a native Egern module — YAML plus
ported scripts, self-contained, no converter references, no links to
someone else's module.

Companion: the `egern-docs` skill owns every right-hand column of the
conversion. Load its pages for the sections you emit.

## Steps

### 1. Gather

Derive the search keys: English app name, Chinese name, and — after the
first find — the API domains inside it. Then:

```bash
python3 <skill-dir>/scripts/fetch-sources.py '中国人保' --out /tmp/picc-sources
```

Supplement with manual GitHub code search per
[reference/source-repos.md](reference/source-repos.md) (repo map + search
patterns). Done when every client format has at least one hit or a
documented miss: for each of Surge / Loon / QX / Egern, one module fetched
or "no module exists" recorded.

### 2. Read

Read every fetched file end to end. Extract each entry as a (pattern,
action, comment) tuple. Note each source's date — newest entries usually
track the current app version.

### 3. Merge

Apply the merge policy in
[reference/source-repos.md](reference/source-repos.md) — normalize, dedup,
resolve conflicts fail-closed, keep a provenance comment line per source.
Done when the merged tuple list has no two entries with the same normalized
pattern.

### 4. Convert

Map every tuple to Egern fields using
[reference/conversion-tables.md](reference/conversion-tables.md). Absorb,
not translate: run the decision ladder on every script before it can
become a script — fixed structure edits become `response_jq` filters,
conditionless string surgery becomes `response_regex`, only real logic
(branching, state, storage) gets ported to `export default async (ctx)`.
Icon: the app's App Store icon at 104×104 (lookup rule in the tables).
No Script-Hub or external converter URLs in the output: the module is
self-contained native Egern.

Native module skeleton:

```yaml
name: <app> 去广告
description: <what it blocks; note if app cache must be cleared>
author: <you>
homepage: <this repo>
icon: <SF Symbol or icon URL>
# merged from: <repo@date, repo@date, ...>

url_rewrites:
  - match: '^https?://api\.example\.com/ads'
    location: http://reject-dict/
map_locals:
  - match: '^https?://api\.example\.com/splash'
    status_code: 200
    headers: {Content-Type: application/json}
    body: '{}'
scriptings:
  - http_response:
      name: <app> 主页
      match: '^https?://api\.example\.com/home'
      script_url: <local ported script path or repo raw URL>
      body_required: true
mitm:
  hostnames:
    - api.example.com
```

Done when every tuple from step 3 appears in the module exactly once.

### 5. Verify

Check the wiring against the `egern-docs` skill: every field name matches
the page for that section; `match` regexes are full-URL anchored; MITM
hostnames cover exactly the domains the rewrites and scripts touch (no
more); ported scripts use only `ctx.*` APIs documented in the
javascript-api page. Report which sources were merged and any tuple or
script dropped as unportable, with the reason.

## Answering

- The module is written in Chinese when the app and sources are Chinese.
- Every converted module carries provenance comments — the absorbed repos
  and dates — so a later refresh knows what to re-gather.
- A construct with no Egern equivalent is dropped with a comment naming
  it, never silently, never approximated.
