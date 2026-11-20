# egern

个人 Egern 工作仓库 + 机器可读的官方文档快照。

根目录留给实际的 Egern 配置工作（Profile、模块、规则集、脚本）。所有 agent 相关
的东西 — skill、文档快照、llms 索引、维护脚本 — 收在 `agents/skills/egern-docs/`
里，一个自包含的目录，可整体拷走或链接进任何 skills 目录。

官方没有发布 `llms.txt`，Context7 也没认真收录 Egern（官方那个条目只有 471 tokens
的 intro 摘要）。这里补上，让任何 LLM 或 agent 读到准确、可 diff 的文档。

- 官方文档：https://egernapp.com/docs ・ [中文](https://egernapp.com/zh-CN/docs)
- 非官方镜像，文档内容版权归 Byte Crossing Ltd

## 结构

```
agents/skills/egern-docs/
  SKILL.md                          egern-docs skill 定义
  llms.txt                          LLM 索引
  llms-full.txt                     英文全文合并，约 150 KB
  docs/en/                          英文文档，19 页
  docs/zh-CN/                       中文文档，19 页
  scripts/scrape.py                 抓取 + 生成 llms.txt，零依赖
  scripts/tests/test_scrape.py      转换器单元测试
  scripts/install-skill.sh          把 skill 装进任意 skills 目录
context7.json                       Context7 索引范围配置（需在仓库根）
.github/workflows/sync-docs.yml     每周一自动同步
```

根目录的 `Profile.yaml`、`modules/`、`rulesets/` 之类的实际配置按需添加 —
文档快照不占根目录。

每个文档页带 frontmatter，方便判断新鲜度：

```yaml
---
title: DNS
source: https://egernapp.com/docs/configuration/dns
language: en
fetched: 2026-11-20
---
```

## 用法

**喂给 LLM**

```
https://raw.githubusercontent.com/Sliverkiss/egern/main/agents/skills/egern-docs/llms-full.txt   # 全文
https://raw.githubusercontent.com/Sliverkiss/egern/main/agents/skills/egern-docs/llms.txt        # 索引
```

**拿单页** — `agents/skills/egern-docs/docs/zh-CN/configuration-dns.md` 等。

**安装 skill**

```bash
./agents/skills/egern-docs/scripts/install-skill.sh ~/.claude/skills
```

skill 目录自包含（`SKILL.md` + `docs/` + llms 文件），可以直接拷进任何支持
SKILL.md 的 agent 工具里，不依赖本仓库路径。

**提交到 Context7**

1. 打开 https://context7.com/add-library ，GitHub tab，填
   `https://github.com/Sliverkiss/egern`
2. 收录后 `resolve-library-id` 搜 `egern` 即可

`context7.json` 已把索引范围锁在 `agents/skills/egern-docs/docs/en` —
Context7 只索引英文为主的页面，中文那半边会被跳过。

## 维护

```bash
python3 agents/skills/egern-docs/scripts/scrape.py           # 重新抓取
python3 agents/skills/egern-docs/scripts/scrape.py --check   # 只检查，有变化退出码 1
cd agents/skills/egern-docs && python3 -m unittest discover scripts/tests   # 跑测试
```

`--check` 比较时忽略 `fetched` 日期，只对内容变化报警。CI 每周一跑一次，有变化
自动提交 — 官方文档更新会直接出现在 commit diff 里。

## 已知限制

- 官方文档只有 19 页，`llms-full.txt` 很短；内容随官网更新，不含 App 内未文档化的行为。
- 教程页截图仍指向 egernapp.com 原图，未本地化。
- 文档没写的功能就是没写 — skill 明确要求如实说明「文档未覆盖」，不要从 YAML
  能解析推断 Egern 支持该字段。
