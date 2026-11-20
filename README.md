# egern

个人 Egern 工作仓库 + 机器可读的官方文档快照。

根目录留给实际的 Egern 配置工作（Profile、模块、规则集、脚本），所有 agent 相关的
东西收在 `.agents/skills/skills/egern-docs/` 里：一个自包含的 skill，加上官方文档
快照、`llms.txt` 和全文。

官方没有发布 `llms.txt`，Context7 也没收录 Egern。这里补上，让任何 LLM 或 agent
读到准确、可 diff 的文档，而不是靠猜 Surge / Clash 语法。

- 官方文档：https://egernapp.com/docs ・ [中文](https://egernapp.com/zh-CN/docs)
- 抓取范围：19 个文档页 × 中英双语
- 非官方镜像，文档内容版权归 Byte Crossing Ltd

## 结构

```
llms.txt                          LLM 索引入口（指向下面 docs 里的页面）
llms-full.txt                     英文全文合并，约 150 KB
.agents/skills/skills/egern-docs/
  SKILL.md                        egern-docs skill 定义
  docs/en/*.md                    英文文档，19 页
  docs/zh-CN/*.md                 中文文档，19 页
scripts/scrape.py                 抓取 + 生成 llms.txt，零依赖
scripts/install-skill.sh          把 skill 装进任意 skills 目录
tests/test_scrape.py              转换器单元测试，零依赖
context7.json                     Context7 索引范围配置
.github/workflows/sync-docs.yml   每周一自动同步
```

根目录的 `Profile.yaml`、`modules/`、`rulesets/`、`scripts/` 之类的实际配置
按需添加 — 文档快照不占根目录。

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
https://raw.githubusercontent.com/Sliverkiss/egern/main/llms-full.txt   # 全文
https://raw.githubusercontent.com/Sliverkiss/egern/main/llms.txt        # 索引
```

**拿单页** — `.agents/skills/skills/egern-docs/docs/zh-CN/configuration-dns.md` 等。

**安装 skill**

```bash
./scripts/install-skill.sh                    # -> ~/.claude/skills/egern-docs
./scripts/install-skill.sh ~/.agents/skills   # 或任意 skills 目录
```

skill 目录自包含（`SKILL.md` + `docs/`），可以直接拷进任何支持 SKILL.md 的
agent 工具里，不依赖本仓库路径。

**提交到 Context7**

1. 打开 https://context7.com/add-library ，GitHub tab，填
   `https://github.com/Sliverkiss/egern`
2. 或到 [upstash/context7](https://github.com/upstash/context7) 提 issue / PR
3. 收录后 `resolve-library-id` 搜 `egern` 即可

`context7.json` 已经把索引范围锁在 `.agents/skills/skills/egern-docs/docs/en` —
Context7 只索引英文为主的页面，中文那半边会被跳过。

## 维护

```bash
python3 scripts/scrape.py           # 重新抓取并重写所有文件
python3 scripts/scrape.py --check   # 只检查，有变化时退出码 1
python3 -m unittest discover tests  # 跑测试
```

`--check` 比较时忽略 `fetched` 日期，只对内容变化报警。CI 每周一跑一次，有变化
自动提交 —— 官方文档更新会直接出现在 commit diff 里。

## 已知限制

- 官方文档只有 19 页，`llms-full.txt` 很短；内容随官网更新，不含 App 内未文档化的行为。
- 教程页截图仍指向 egernapp.com 原图，未本地化。
- 文档没写的功能就是没写 — skill 明确要求如实说明「文档未覆盖」，不要从 YAML
  能解析推断 Egern 支持该字段。
