# Egern 官方文档快照 · LLM-ready

[Egern](https://egernapp.com)（iOS / iPadOS / macOS 代理客户端）官方文档的机器可读快照：
Markdown 原文、`llms.txt` 索引、单文件全文，以及一个 agent skill。

官方没有发布 `llms.txt`，Context7 也没有收录 Egern。这个仓库补上这两块，让任何
LLM 或 agent 能直接读到准确、可 diff 的文档，而不是靠猜 Surge / Clash 语法。

- 官方文档：https://egernapp.com/docs ・ [中文](https://egernapp.com/zh-CN/docs)
- 抓取来源：19 个文档页 × 中英双语，每次同步都重新生成
- 不 affiliated，文档内容版权归 Byte Crossing Ltd

## 用法

**直接喂给 LLM**

```
https://raw.githubusercontent.com/Sliverkiss/egern/main/llms-full.txt   # 全文，约 150 KB
https://raw.githubusercontent.com/Sliverkiss/egern/main/llms.txt        # 索引
```

**按需取单页** — `docs/zh-CN/configuration-dns.md`、`docs/en/configuration-proxies.md` 等。

**安装 skill**

```bash
git clone https://github.com/Sliverkiss/egern.git ~/code/egern-docs
mkdir -p ~/.claude/skills
ln -s ~/code/egern-docs/.agents/skills/egern-docs ~/.claude/skills/egern-docs
ln -s ~/code/egern-docs/docs ~/.claude/skills/egern-docs/docs
```

装好后在写 Egern 配置、脚本、模块时会自动按需读对应文档页。

**提交到 Context7**

Context7 的数据源就是公开 GitHub 仓库：

1. 打开 https://context7.com/add-library ，填 `https://github.com/Sliverkiss/egern`
2. 或在其 [upstash/context7](https://github.com/upstash/context7) 仓库提 issue / PR 添加数据源
3. 审核收录后，`resolve-library-id` 搜 `egern` 即可查到

## 结构

```
llms.txt                 索引（中英双语分组）
llms-full.txt            英文全文合并
docs/en/*.md             英文文档，19 页
docs/zh-CN/*.md          中文文档，19 页
.agents/skills/egern-docs/SKILL.md   agent skill
scripts/scrape.py        抓取 + 生成 llms.txt，零依赖
scripts/install-skill.sh 一键安装 skill
tests/test_scrape.py     转换器单元测试，零依赖
.github/workflows/sync-docs.yml  每周一自动同步
```

每个文档页都带 frontmatter：

```yaml
---
title: DNS
source: https://egernapp.com/docs/configuration/dns
language: en
fetched: 2026-11-20
---
```

## 维护

```bash
python3 scripts/scrape.py           # 重新抓取并重写所有文件
python3 scripts/scrape.py --check   # 只检查，有变化时退出码为 1
python3 -m unittest discover tests  # 跑测试
```

`--check` 比较时会忽略 `fetched` 日期，只对内容变化报警。CI 每周一跑一次，
有变化就自动提交 — 官方文档更新会在 commit diff 里直接看到。

## 已知限制

- 官方文档只有 19 页，`llms-full.txt` 因此很短；内容随官方站更新，不含 App 内
  未文档化的行为。
- 教程页的截图仍指向 egernapp.com 原图，未本地化。
- 文档没写的功能就是没写：skill 明确要求如实说明「文档未覆盖」，不要从 YAML
  能解析推断 Egern 支持该字段。
