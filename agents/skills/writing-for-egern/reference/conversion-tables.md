# Conversion tables

Source-client syntax → Egern field, for every construct a community module
carries. Egern docs (`egern-docs` skill) are the authority on the right-hand
column; this file is the authority on the left-hand column and the mapping
itself. When the mapping and the docs disagree, the docs win — fix this file.

## Metadata headers

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge module | `#!name=` `#!desc=` `#!author=` `#!homepage=` `#!icon=` `#!category=` | `name` `description` `author` `homepage` `icon` (category has no Egern field; fold it into description if informative) |
| Loon plugin | `#!name = ` `#!desc = ` `#!icon = ` `#!author = ` | same fields |
| QX conf | `#!name=` or bare comments | same fields; a bare `# > App - Tag` first comment is the name |

## URL rewrites

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `pattern - reject` | `url_rewrites: - match: pattern` + `location: http://reject/` |
| Surge/Loon | `pattern - reject-dict` | `location: http://reject-dict/` |
| any | `reject-array` / `reject-200` / `reject-img` / `reject-video` | `http://reject-array/` / `http://reject-200/` / `http://reject-img/` / `http://reject-video/` |
| Surge | `pattern target` (302) | `location: target` + `status_code: 302` |
| Surge | `pattern header-location target` (header mode) | `location: target`, omit `status_code` |
| QX | `pattern url 302 target` | same as Surge redirect |
| QX | `pattern url reject` | reject mapping above |
| Loon v2 | `pattern reject` / `pattern reject-dict` | same mapping |

Egern `match` is a regex matched against the **full URL** including scheme.

## Map Local

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `pattern data-type=text data="{}" status-code=200 header="Content-Type:application/json"` | `map_locals: - match: pattern` + `status_code: 200` + `body: '{}'` + `headers: {Content-Type: application/json}` |
| Loon reject with body | `reject-dict` when a body is needed | prefer `map_locals` over reject-dict when the source pins a status or headers |

QX `response-body` rewrites (`pattern url response-body re re`) are **body
rewrites**, not map locals: map to `body_rewrites: - response_regex:` with
`find`/`replace`.

## Scripts

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `type=pattern, pattern=…, script-path=…` (`http-request`/`http-response`) | `scriptings: - http_request:` / `- http_response:` with `name` `match` `script_url` |
| Surge | `requires-body=true` | `body_required: true` |
| Loon | `http-response pattern script-path=…, requires-body=true, tag=名称` | `http_response:` + `name: 名称` + `body_required: true` |
| QX | `pattern url script-response-body url` | `http_response:` + `script_url` |
| QX | `pattern url script-request-header url` | `http_request:` |
| Surge | `argument=…` | `arguments:` map |
| Surge cron | `type=cron, cronexp="…"`, event scripts | `schedule:` with `cron`; `event network-changed` → `network:` |
| Loon generic | `generic script-path=…` | `generic:` |

### Script runtime — the hard part

Egern scripts run `export default async function(ctx)` with a Fetch-style
`ctx` object (see `egern-docs` javascript-api page). Community scripts target
QX (`$task`, `$prefs`, `$notify`, `$done`) or Surge/Loon (`$httpClient`,
`$persistentStore`, `$notification`, `$done`).

Every script gets ported natively — no Script-Hub references, no external
conversion hosting. The module must be self-contained Egern YAML + Egern
scripts.

Port map:

| Legacy | Egern native |
| --- | --- |
| `$httpClient.get/post(opts, cb)` / `$task.fetch` | `await ctx.http.get/post(url, opts)` → `resp.json()` / `resp.text()` |
| `$persistentStore.read/write` / `$prefs.valueForKey/setValueForKey` | `ctx.storage.get/set` (string) / `getJSON/setJSON` (object) |
| `$notification.post(t, s, b)` / `$notify(t, s, b)` | `ctx.notify({title, subtitle, body})` |
| `$done({body, headers, status})` (response) | `return {body, headers, status}` |
| `$done({})` / `$done()` (pass through) | return nothing |
| `$request.url` / `$response.body` | `ctx.request.url` / `await ctx.response.text()` / `.json()` |
| `$argument` string | `ctx.env` (via scriptings `env:` or module `compat_arguments`) |
| Env detection (`$.isQuanX()` etc.) | delete — single runtime, no branching |

Porting procedure: read the script, list every legacy API call it makes,
map each with the table above, then rewrite as one async function with
early returns. Fetch-style details that bite: `body` streams are consumed
once — read to text/json once and reuse the variable; `ctx.notify` takes a
single object, not positional args.

A script too tangled to port (obfuscated, WASM, >300 lines of dense logic)
is dropped from the module with a comment naming it and why — never
referenced through a converter.

## MITM

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `[MITM] hostname = %APPEND% a.com, b.com` | `mitm: hostnames: [a.com, b.com]` (module merge handles the append) |
| Loon | `[MitM] hostname = a.com` | same |
| QX | `hostname = a.com` (last line) | same |

`%APPEND%` / `%INSERT%` have no Egern equivalent — modules merge by union, so
plain hostnames are correct.

## Rule sets / rules

A community ad-block module rarely carries routing rules; when it does:

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `DOMAIN-SUFFIX,example.com,REJECT` | `rules: - domain_suffix: {match: example.com, policy: REJECT}` |
| any | remote rule-set URL `.list` | `rules: - rule_set: {…}` per the `rules` page in `egern-docs` |

## Panels / widgets

| Source | Syntax | Egern |
| --- | --- | --- |
| Surge | `[Panel] …` | `widgets:` with a `generic` script returning Widget DSL JSON |
| Loon tile | `tile` section | same |

Panel scripts need a real port: Surge panel HTML does not map to Widget DSL.
Write a fresh `generic` script and return the DSL (`type: 'widget'` root).

## Unsupported / drop

- `[Argument]` platform-specific keys with no Egern meaning → drop unless
  they feed `compat_arguments`.
- `#!tg-channel`, `#!raw-url`, `#!date` headers → drop (provenance goes in
  the module's `homepage`/`description` or the module's repo README).
- QX `hostname` inside `[MITM]` sections that the rewrites never touch →
  keep only hostnames the surviving rewrites/scripts actually match. Tight
  hostname lists are a correctness feature: MITM is global for the client.
