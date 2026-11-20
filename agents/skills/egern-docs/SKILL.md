---
name: egern-docs
description: >
  Egern proxy client official documentation. Fire on any Egern configuration
  work — Profile YAML (proxies, policy groups, rules, DNS, modules, rewrites,
  HTTP captures, widgets) or Egern JavaScript scripting. Matches: Egern,
  Profile.yaml, policy_groups, rule_set, egern://.
---

# Egern Documentation Skill

## The rule

Support = documented in this snapshot. A YAML key that parses is still
unsupported until a page here documents it; when you hit that case, say
"not documented" and write only what the pages cover. Egern's fields look
like Surge, Loon or mihomo and differ from all three — take every field
from these pages, checked against the page for the section you are writing.

## Lookup

1. Pick a page per section the task touches, from the navigation below.
   Each slug exists under `docs/en/` and `docs/zh-CN/` with the same name —
   read the language the answer will be written in.
2. Long page: search the field, protocol or section heading, then read that
   section plus the shared fields it references. You are done when every
   field you emit appears on the page for that section.
3. Cross-module work — a module carrying a script or a widget — read each
   part's page plus `env` and `modules`.

## Profiles

From scratch: read the complete `example` first, then the pages for the
sections it uses. Editing an existing profile: keep unrelated settings and
the user's own values untouched.

Then check the wiring: every referenced name — proxy, policy group, DNS
upstream group, rule set, module — resolves to a definition in the profile.

## Answering

- Label every claim as documented, inferred, or uncovered. Two pages in
  conflict: report the conflict, never merge it away.
- Say whether an example is a complete profile or a fragment.
- Cite the page used. Each page's frontmatter `fetched` date marks the
  snapshot; the live version is `https://egernapp.com/docs/<slug>`.
- Claim device testing only if it actually happened.

## Navigation

| Topic | Page |
| --- | --- |
| Product overview | [intro](docs/en/intro.md) |
| FAQ | [faq](docs/en/faq.md) |
| URL Scheme | [url-scheme](docs/en/url-scheme.md) |
| Complete example | [example](docs/en/configuration-example.md) |
| Proxies and protocols | [proxies](docs/en/configuration-proxies.md) |
| Policy groups | [policy_groups](docs/en/configuration-policy_groups.md) |
| Rules and rule sets | [rules](docs/en/configuration-rules.md) |
| DNS | [dns](docs/en/configuration-dns.md) |
| Script configuration | [scriptings](docs/en/configuration-scriptings.md) |
| JavaScript API | [javascript-api](docs/en/javascript-api.md) |
| Environment variables | [env](docs/en/configuration-env.md) |
| Widgets / Widget DSL | [widgets](docs/en/configuration-widgets.md) |
| URL rewrites | [url_rewrites](docs/en/configuration-url_rewrites.md) |
| Header rewrites | [header_rewrites](docs/en/configuration-header_rewrites.md) |
| Body rewrites | [body_rewrites](docs/en/configuration-body_rewrites.md) |
| HTTP captures | [http_captures](docs/en/configuration-http_captures.md) |
| Modules and arguments | [modules](docs/en/configuration-modules.md) |
| Proxy tutorial | [proxy](docs/en/example-proxy.md) |
| Sniffer tutorial | [http-traffic-sniffer](docs/en/example-http-traffic-sniffer.md) |

Chinese mirror: the same slugs under `docs/zh-CN/`.
