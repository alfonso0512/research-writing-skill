---
name: research-writing
description: |
  科研论文写作助手，提供 30 个 Prompt 模板覆盖论文写作全流程。
  当用户提到：论文写作、润色、翻译、文献综述、摘要、引言、方法章节、回复审稿人、
  基金申请、研究计划、学术演讲 PPT、LaTeX 编辑、学术图表、实验结果分析、模拟审稿、
  去 AI 味、文献对比、找研究空白、论文大纲时使用。
  不要用于：非学术写作、创意写作、博客、商业文案、求职信、小说等场景。
license: MIT
compatibility: opencode, claude-code
metadata:
  author: alfonso0512
  version: "3.0.0"
---

# Research Writing Skill - 科研论文写作助手

> **版本**: 3.0 | **更新时间**: 2026-07-15 | **Prompt 总数**: 30

## 技能概述

30 个论文写作场景的 Prompt 模板，覆盖**文献调研→大纲撰写→初稿写作→润色修改→图表制作→投稿回复→基金申请**全流程。每个 Prompt 独立存储在 `references/prompts/` 目录下，按需加载。

**触发词**: 论文写作、润色、翻译、文献综述、去 AI 味、回复审稿人、基金申请、学术图表、模拟审稿 等。

## 🎯 快速索引

| 阶段 | Prompt | 文件 | 用途 |
|------|--------|------|------|
| 🔧 翻译润色 | #1 | `01-zh2en.md` | 中译英 |
| 🔧 翻译润色 | #2 | `02-en2zh.md` | 英译中 |
| 🔧 润色优化 | #3 | `03-zh-polish.md` | 中文润色 |
| 🔧 润色优化 | #4 | `04-en-shorten.md` | 英文缩写 |
| 🔧 润色优化 | #5 | `05-en-expand.md` | 英文扩写（逻辑强化） |
| 🔧 润色优化 | #6 | `06-en-polish.md` | 英文润色（TOP 期刊标准） |
| 🔧 去 AI 味 | #7 | `07-zh-deai.md` | 中文去 AI 味 |
| 🔧 去 AI 味 | #8 | `08-en-deai.md` | 英文去 AI 味 |
| 🔧 检查 | #9 | `09-logic-check.md` | 逻辑检查（挑刺王） |
| 🔧 检查 | #10 | `10-abbrev-check.md` | 缩写检查 |
| 📊 图表制作 | #11 | `11-architecture-diagram.md` | 绘制架构图 |
| 📊 图表制作 | #12 | `12-chart-recommend.md` | 实验图推荐 |
| 📊 图表制作 | #13 | `13-figure-caption.md` | 图片标题说明 |
| 📊 图表制作 | #14 | `14-table-caption.md` | 表格标题说明 |
| 📈 结果分析 | #15 | `15-experiment-analysis.md` | 实验结果写作 |
| 🔍 审稿 | #16 | `16-simulate-reviewer.md` | 模拟审稿人 |
| 🛠 工具 | #17 | `17-ai-tool-select.md` | AI 写作工具选择 |
| 📚 文献调研 | #18 | `18-lit-summary.md` | 文献总结与笔记 |
| 📚 文献调研 | #19 | `19-lit-compare.md` | 文献对比分析 |
| 📚 文献调研 | #20 | `20-research-gap.md` | 找研究空白 |
| 📝 大纲撰写 | #21 | `21-outline-gen.md` | 论文大纲生成 |
| 📝 大纲撰写 | #22 | `22-section-expand.md` | 章节内容扩展 |
| ✍️ 初稿写作 | #23 | `23-abstract.md` | 摘要写作 |
| ✍️ 初稿写作 | #24 | `24-introduction.md` | 引言写作 |
| ✍️ 初稿写作 | #25 | `25-method.md` | 方法章节写作 |
| 📬 投稿回复 | #26 | `26-rebuttal.md` | 回复审稿人 |
| 📬 投稿回复 | #27 | `27-cover-letter.md` | Cover Letter |
| 💰 基金申请 | #28 | `28-grant-proposal.md` | 基金申请书 |
| 💰 基金申请 | #29 | `29-research-proposal.md` | 研究计划 |
| 💰 基金申请 | #30 | `30-academic-talk.md` | 学术演讲 PPT |

---

## 决策树：我该用哪个 Prompt？

### 场景 1：写新论文
```
文献调研 → 大纲 → 写章节 → 润色 → 图表 → 审稿自查
  #18-20    #21    #22-25    #3-6   #11-15   #16
```

### 场景 2：修改已有论文
```
去 AI 味 → 润色 → 逻辑检查 → 模拟审稿 → 缩写检查
  #7/#8     #3/#6    #9        #16        #10
```

### 场景 3：回复审稿人
```
审稿分析 → Rebuttal → Cover Letter
   #16       #26         #27
```

### 场景 4：申请基金
```
文献调研 → 基金申请书 → 研究计划 → 演讲 PPT
  #18-20     #28           #29         #30
```

### 场景 5：快速翻译润色
```
中译英 → 去 AI 味 → 缩写检查
  #1       #7/#8      #10
```

---

## 使用方式

### 自动触发（推荐）
当你使用支持 Skill 的 AI 工具（OpenCode / Claude Code）时，提到论文写作相关关键词会自动加载本 Skill。AI 会根据你的意图自动选择最合适的 Prompt 模板。

**安装路径**: `~/.config/opencode/skills/research-writing/`

### 手动使用
1. 浏览 `references/prompts/` 目录，找到需要的 Prompt 文件
2. 复制文件内容到聊天窗口
3. 替换模板中的 `{{变量}}` 为实际内容

---

## 工具脚本

| 脚本 | 用途 |
|------|------|
| `scripts/escape_latex.py` | LaTeX 特殊字符转义（% _ & 等） |
| `scripts/title_case.py` | Title Case / Sentence case 转换 |

---

## 最佳实践

1. **组合使用**: Prompt 可以串联——先用 #21 生成大纲，再用 #22-25 扩展各章节
2. **迭代优化**: 对 AI 输出用 #3-10 进行多轮润色
3. **保持批判**: 用 #16 模拟审稿，提前发现论文问题
4. **数据真实**: 所有实验数据和结论必须基于真实研究，AI 仅辅助表达
