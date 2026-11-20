---
name: egern-docs
description: >
  Egern (iOS/iPadOS/macOS proxy client) official documentation reference. Use when
  writing, modifying, explaining, reviewing or debugging Egern configuration —
  Profile YAML, proxies, policy groups, rules and rule sets, DNS, modules, URL /
  header / body rewrites, HTTP captures, widgets, or JavaScript scripting.
  Triggers on "Egern", "Profile.yaml", "policy_groups", "rule_set", "egern://".
---

# Egern Documentation Skill

## Goal

Answer from the documentation bundled in this skill. Egern is not Surge, Loon,
Quantumult X or mihomo — the syntax overlaps and does not match. Never substitute
another client's configuration for Egern's.

## How to look things up

1. Pick the topic from the navigation below. All paths are relative to this
   `SKILL.md`; `docs/` is a link to the snapshot in the parent repository.
2. Read only the pages the question needs. For cross-module work (for example a
   module that carries a script and a widget), read the dependent pages too.
3. For long pages, search for the field name, protocol name or section heading
   first, then read that section plus the shared fields it refers to.
4. When checking a profile, verify every cross-reference by name: proxies,
   policy groups, DNS upstream groups, rule sets, modules.
5. If the documentation does not cover a behaviour, say so. Do not guess, and do
   not infer support from the fact that a YAML key parses.

## Navigation

| Topic | Chinese | English |
| --- | --- | --- |
| Product overview | [intro](docs/zh-CN/intro.md) | [intro](docs/en/intro.md) |
| FAQ | [faq](docs/zh-CN/faq.md) | [faq](docs/en/faq.md) |
| URL Scheme | [url-scheme](docs/zh-CN/url-scheme.md) | [url-scheme](docs/en/url-scheme.md) |
| Complete example | [example](docs/zh-CN/configuration-example.md) | [example](docs/en/configuration-example.md) |
| Proxies and protocols | [proxies](docs/zh-CN/configuration-proxies.md) | [proxies](docs/en/configuration-proxies.md) |
| Policy groups | [policy_groups](docs/zh-CN/configuration-policy_groups.md) | [policy_groups](docs/en/configuration-policy_groups.md) |
| Rules and rule sets | [rules](docs/zh-CN/configuration-rules.md) | [rules](docs/en/configuration-rules.md) |
| DNS | [dns](docs/zh-CN/configuration-dns.md) | [dns](docs/en/configuration-dns.md) |
| Script configuration | [scriptings](docs/zh-CN/configuration-scriptings.md) | [scriptings](docs/en/configuration-scriptings.md) |
| JavaScript API | [javascript-api](docs/zh-CN/javascript-api.md) | [javascript-api](docs/en/javascript-api.md) |
| Environment variables | [env](docs/zh-CN/configuration-env.md) | [env](docs/en/configuration-env.md) |
| Widgets / Widget DSL | [widgets](docs/zh-CN/configuration-widgets.md) | [widgets](docs/en/configuration-widgets.md) |
| URL rewrites | [url_rewrites](docs/zh-CN/configuration-url_rewrites.md) | [url_rewrites](docs/en/configuration-url_rewrites.md) |
| Header rewrites | [header_rewrites](docs/zh-CN/configuration-header_rewrites.md) | [header_rewrites](docs/en/configuration-header_rewrites.md) |
| Body rewrites | [body_rewrites](docs/zh-CN/configuration-body_rewrites.md) | [body_rewrites](docs/en/configuration-body_rewrites.md) |
| HTTP captures | [http_captures](docs/zh-CN/configuration-http_captures.md) | [http_captures](docs/en/configuration-http_captures.md) |
| Modules and arguments | [modules](docs/zh-CN/configuration-modules.md) | [modules](docs/en/configuration-modules.md) |
| Proxy tutorial | [proxy](docs/zh-CN/example-proxy.md) | [proxy](docs/en/example-proxy.md) |
| Sniffer tutorial | [http-traffic-sniffer](docs/zh-CN/example-http-traffic-sniffer.md) | [http-traffic-sniffer](docs/en/example-http-traffic-sniffer.md) |

Writing a profile from scratch: read the complete example first, then the pages
for the modules it uses. Writing a script: read `scriptings` and `javascript-api`
together. A module that ships a script or widget: add `env` and `modules`.

## Answering

- Use the field names from the documentation. Configuration examples are Egern
  YAML; script examples use the documented JavaScript API.
- Say whether an example is a complete profile or a fragment. When editing an
  existing profile, keep unrelated settings and the user's own values intact.
- Separate three things: behaviour the documentation states, inference from the
  documentation, and behaviour that is not covered. If two pages conflict, point
  at the conflict instead of merging them into one confident answer.
- Cite the page you used. Version-sensitive behaviour: the snapshot date is in
  each file's frontmatter; the live page is `https://egernapp.com/docs/<page>`.
- Never claim a configuration was tested on a device unless it was.
