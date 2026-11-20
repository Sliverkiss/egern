---
name: writing-for-egern
description: >
  Build a native Egern module for a named app by absorbing the community's
  Surge, Loon, Quantumult X and Egern modules for that app — 去广告, 重写,
  移植, port, ad-block. Also fires when handing over any sgmodule / Loon
  plugin / QX rewrite conf for conversion.
---

# Writing for Egern

One job: turn every community module for one app into a single native
Egern module — YAML only where possible, a script only when the logic
earns it, nothing referencing someone else's runtime. Absorb, don't
translate: optimize while merging, or you're just moving formats.

Field-level truth lives in the `egern-docs` skill — load its page for any
section you emit. Everything below is the part `egern-docs` doesn't own:
where sources live, how they merge, and the ladder that decides what each
entry becomes.

## Pipeline

**Gather.** Derive keys: English name, Chinese name, and — after the first
find — the API domains inside it.

```bash
python3 agents/skills/writing-for-egern/scripts/fetch-sources.py '中国人保' --out /tmp/sources
```

Then manual GitHub code search per [reference/source-repos.md](reference/source-repos.md)
(repo map + search patterns). Done when Surge, Loon, QX and Egern each
have one module fetched or a recorded miss.

**Read.** Every file, end to end. Extract (pattern, action, comment)
tuples; note each source's date. Done when every fetched file has yielded
its tuples.

**Merge.** The merge policy in [reference/source-repos.md](reference/source-repos.md):
normalize, dedup, resolve conflicts fail-closed. Done when no two
entries share a normalized pattern.

**Convert.** Each entry passes the ladder in
[reference/conversion-tables.md](reference/conversion-tables.md) before it
becomes anything — fixed JSON edits become `response_jq` filters (verify
with `jq -f` against a sample payload first), conditionless string
surgery becomes `response_regex`, only real logic (branching, state,
storage) is ported to `export default async (ctx)`. Icon: the app's App
Store icon at 104×104, lookup rule in the tables. Done when every merged
entry appears in the module exactly once, as the ladder's verdict, not
the source's shape.

**Verify.** Every field matches the `egern-docs` page for that section;
regexes full-URL anchored; MITM hostnames = exactly the domains the
surviving entries touch. Report merged sources and anything dropped as
unportable, with the reason.

Module skeleton — the ladder's output shapes, most common first:

```yaml
name: <app> 去广告
description: <what it blocks; note if app cache must be cleared>
author: <original author(s) from the sources — we integrate, not originate>
homepage: <this repo>
icon: <source module's icon if one exists; else App Store 104×104 per the tables>
# merged from: <repo@date → what it contributed, repo@date → …>

url_rewrites:
  - match: '^https?://api\.example\.com/ads'
    location: http://reject-dict/
body_rewrites:
  - response_jq:
      match: '^https?://api\.example\.com/home'
      filter: '.data.ads = []'
map_locals:
  - match: '^https?://api\.example\.com/splash'
    status_code: 200
    headers: {Content-Type: application/json}
    body: '{}'
scriptings:        # only entries that survived the ladder's rung 3
  - http_response:
      name: <app> 主页
      match: '^https?://api\.example\.com/home'
      script_url: <ported script in this repo>
      body_required: true
mitm:
  hostnames:
    - api.example.com
```

Chinese app, Chinese sources → module comments in Chinese. A construct
with no Egern equivalent is dropped with a comment naming it, never
approximated.
