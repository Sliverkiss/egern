<div align="center">

# Egern 模块仓库

**声明式重写的去广告与解锁模块，零脚本、零正则手术，每条规则注明来源与解锁内容。**

[![Egern](https://img.shields.io/badge/App-Egern-blue?logo=protonmail&logoColor=white&labelColor=0A0A0A)](https://egernapp.com)
[![Telegram](https://img.shields.io/badge/Telegram-@sliverkiss__blog-26A5E4?logo=telegram&logoColor=white&labelColor=0A0A0A)](https://t.me/silverkiss_blog)
[![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20macOS%20%7C%20tvOS-8E8E93?logo=apple&logoColor=white&labelColor=0A0A0A)](https://egernapp.com/docs)
[![License](https://img.shields.io/badge/License-仅供参考-green?labelColor=0A0A0A)](#免责声明)

[![Modules](https://img.shields.io/badge/模块-8%20个-FF9F0A?labelColor=0A0A0A)](#模块列表)
[![Rules](https://img.shields.io/badge/规则-570%2B%20条-FF375F?labelColor=0A0A0A)](#模块列表)
[![Zero Scripts](https://img.shields.io/badge/Zero-scriptings-30D158?labelColor=0A0A0A)](#设计原则)
[![Docs](https://img.shields.io/badge/llms.txt-官方文档快照-5E5CE6?labelColor=0A0A0A)](agents/skills/egern-docs/)

</div>

---

## 模块列表

订阅方式：复制下表 Raw 链接，Egern → 模块 → 从 URL 安装。

| 模块 | 内容 | 规模 | 作者（原作者） |
|---|---|---|---|
| **[叮当猫解锁](modules/ddm-unlocks.yaml)** | chxm1023/Rewrite 全量脚本移植：226 个 App 的订阅解锁、会员、界面净化 | 383 条 · 259 mitm | [chxm1023](https://github.com/chxm1023/Rewrite) |
| **[毒奶去网页广告](modules/adblock4limbo.yaml)** | 搜索引擎、视频、漫画、小说站点的网页广告与弹窗移除 | 51 条 | [limbopro](https://github.com/limbopro/Adblock4limbo) |
| **[小红书去广告](modules/xiaohongshu-ads.yaml)** | 开屏、信息流、搜索、关注页广告及运营弹窗 | 30 条 | fmz200, RuCu6, zirawell, blackmatrix7, ddgksf2013 |
| **[起点读书去广告](modules/qidian-ads.yaml)** | 开屏、书架悬浮、每日导读、活动弹窗及推广位 | 21 条 | app2smile, zirawell |
| **[腾讯视频净化](modules/txvideo-ads.yaml)** | 开屏、贴片、暂停广告及底部短剧/好物 tab | 5 条 | ZenmoFeiShi |
| **[广告联盟去广告](modules/ad-alliance.yaml)** | 穿山甲、优量汇、快手联盟三家广告 SDK 拦截 | 8 条 | app2smile, NobyDa |
| **[RevenueCat 通用解锁](modules/revenuecat-unlock.yaml)** | RevenueCat 计费类 App 通用解锁 | 1 条 | Sliverkiss |
| **[中国人保去广告](modules/picc-ads.yaml)** | 开屏、弹窗及页面推广位移除 | 5 条 | Sliverkiss |

> 大部分去广告/解锁规则**需清缓存或重装 App** 才能生效。

## 设计原则

- **零 scriptings、零 response_regex** —— 所有 JS 脚本逐个读源码后手写转换为声明式
  规则：`response_jq`（固定 JSON 改写）、`map_locals`（固定回执）、`url_rewrites`
  （reject / 302）。
- **原文靠全文正则手术（`body.replace(/.../g, ...)`）的脚本整脚本不收** —— 那种写法
  塞不进 jq，硬译只是把 JS 正则语义搬进另一套引擎再赌它等价。出局名单写在模块头部。
- **每条规则上方注明**：解锁了什么、原脚本地址、要 MITM 的域名。
- **mitm.hostnames 逐字照抄原作者的 `[mitm]` 声明**，不推导、不补域名；
  上游 pattern 写了自家 mitm 没声明的死分支，收窄 pattern 而不是替它救活。
- **author 只写原作者**，不写仓库搬运者。
- 提交前过 [`verify.py`](agents/skills/writing-for-egern/scripts/verify.py)：
  元数据完整、match 全部 `^` 锚定、reject token 合法、jq filter 用 jq 二进制实跑解析。

## llms.txt 官方文档快照

Egern 官方没有发布 `llms.txt`，Context7 收录的条目只有 471 tokens 的摘要。本仓库
补齐了机器可读的文档快照，任何 LLM / agent 可直接读到准确、可 diff 的官方文档：

- 索引：[`agents/skills/egern-docs/llms.txt`](agents/skills/egern-docs/llms.txt)
- 全文：[`llms-full.txt`](agents/skills/egern-docs/llms-full.txt)（英文 19 页合并）
- 中文文档：[`docs/zh-CN/`](agents/skills/egern-docs/docs/zh-CN/)
- 每周一 CI 自动同步官方文档，diff 即更新日志

## 免责声明

本仓库所有模块仅供学习与交流，**请勿用于任何商业用途**。模块内容版权归原作者
所有，本仓库只做声明式格式转换。下载使用即表示你理解并同意：解锁类规则仅用于
测试自己的订阅逻辑，请在 24 小时内删除。

**Telegram 频道**：[@sliverkiss_blog](https://t.me/silverkiss_blog) · 更新与讨论都在这里。
