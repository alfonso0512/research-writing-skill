# AI Research Writing Skill - 科研论文写作助手

> 🎓 基于 AI 的科研论文写作助手，提供 30 个 Prompt 模板覆盖论文写作全流程
> 
> **版本**: 3.0 | **License**: MIT | **语言**: 中文/英文

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0-blue)](https://github.com/alfonso0512/research-writing-skill)
[![OpenCode Skill](https://img.shields.io/badge/OpenCode-Skill-green)](https://opencode.ai)

---

## 📖 项目简介

这是一个专为科研工作者设计的 AI 辅助写作工具集，包含 **30 个精心设计的 Prompt 模板**，覆盖从**文献调研→大纲撰写→初稿写作→润色修改→图表制作→投稿回复→基金申请**的完整科研写作流程。

无论你是：
- 🎓 正在写第一篇论文的研究生
- 👨‍🏫 需要指导学生的高校教师
- 🔬 准备投稿顶刊的科研人员
- 💰 正在申请科研基金的学者

这个工具都能帮你提高写作效率，提升论文质量。

---

## ✨ 核心功能

### 📚 文献调研阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #18 文献总结与笔记 | 快速提取论文核心信息 | 阅读大量文献时做结构化笔记 |
| #19 文献对比分析 | 多篇论文对比分析 | 写 Related Work 时梳理研究脉络 |
| #20 找到研究空白 | 识别 Research Gap | 确定自己的研究方向 |

### 📝 论文写作阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #21 论文大纲生成 | 生成详细论文大纲 | 开始写作前规划结构 |
| #22 章节内容扩展 | 将要点扩展为完整章节 | 从笔记到正式论文 |
| #23 摘要写作 | 撰写精炼的 Abstract | 投稿前最后完善 |
| #24 引言写作 | 撰写引人入胜的 Introduction | 论文开篇 |
| #25 方法章节写作 | 清晰描述技术方法 | Method 章节 |

### 🔧 润色修改阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #1 中译英 | 中文草稿翻译为英文 | 中文思路→英文论文 |
| #2 英译中 | 英文论文翻译为中文 | 阅读英文文献 |
| #3 中文润色 | 优化学术中文表达 | 中文论文/基金申请 |
| #4 英文缩写 | 精简英文文本 | 控制字数 |
| #5 英文扩写 | 强化逻辑连接 | 论证不够充分时 |
| #6 英文润色 | 达到 TOP 期刊标准 | 投稿前润色 |
| #7 中文去 AI 味 | 去除 AI 生成痕迹 | AI 辅助写作后 |
| #8 英文去 AI 味 | 去除 AI 生成痕迹 | AI 辅助写作后 |
| #9 逻辑检查 | 挑逻辑漏洞 | 投稿前自查 |

### 📊 图表制作阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #11 绘制架构图 | 设计系统架构图 | Method 章节配图 |
| #12 实验图推荐 | 推荐合适的图表类型 | 数据可视化 |
| #13 图片标题说明 | 生成规范的 Figure 标题 | 图片说明 |
| #14 表格标题说明 | 生成规范的 Table 标题 | 表格说明 |
| #15 实验结果分析 | 撰写实验分析段落 | Results 章节 |

### 📬 投稿回复阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #16 模拟审稿人 | 模拟审稿意见 | 投稿前自查 |
| #17 模型选择推荐 | 推荐 AI 模型 | 选择合适工具 |
| #26 回复审稿人 | 撰写 Rebuttal | 回复审稿意见 |
| #27 Cover Letter | 撰写投稿信 | 投稿时使用 |

### 💰 基金申请阶段
| Prompt | 功能 | 适用场景 |
|--------|------|----------|
| #28 基金申请书 | 撰写基金本子 | 国自然等基金申请 |
| #29 研究计划 | 撰写 Research Proposal | 博士/博士后申请 |
| #30 学术演讲 PPT | 设计学术报告 | 会议演讲/组会汇报 |

---

## 🚀 快速开始

### 方式一：OpenCode / Claude Code 用户（推荐）

1. **克隆或下载** 本仓库到本地
2. **复制**整个 `research-writing/` 文件夹到 skills 目录：
   - OpenCode: `~/.config/opencode/skills/research-writing/`
   - Claude Code: `~/.claude/skills/research-writing/`
3. **重启** AI 工具或发送 `/reload` 命令
4. **开始使用**：直接说"帮我润色这段论文"即可自动触发

### 方式二：手动使用 Prompt

1. **浏览** `references/prompts/` 目录，找到需要的 Prompt 文件
2. **复制** 文件内容（Markdown 格式）
3. **粘贴** 到你使用的 AI 工具（Claude、ChatGPT、Cursor、OpenCode 等）
4. **替换** 模板中的 `{{变量}}` 为你的内容

### 方式三：其他 AI 工具

本技能的 Prompt 模板兼容主流 AI 工具：
- ✅ OpenCode / Claude Code（自动触发 + 按需加载）
- ✅ Claude / Anthropic
- ✅ ChatGPT / GPT-4
- ✅ Cursor / VS Code
- ✅ Cherry Studio
- ✅ 任何支持 Markdown 的 AI 工具

---

## 📋 使用示例

### 示例 1：文献总结

**输入**：
```
请帮我总结这篇论文：
[粘贴论文摘要或全文]
```

**输出**：
```markdown
## 📖 基本信息
- **标题**: Deep Learning for Scientific Computing
- **作者/机构**: Zhang et al. / MIT
- **发表 venue**: Nature Machine Intelligence, 2025

## 🎯 核心贡献
提出了一种新的神经网络架构，将计算效率提升 10 倍...

## ❓ 研究问题
现有方法在处理大规模科学计算问题时效率低下...

## 🔑 关键方法
- 使用稀疏注意力机制...
- 引入多尺度特征融合...
...
```

### 示例 2：中译英

**输入**：
```
请帮我把这段中文翻译成英文：
"本文提出了一种基于深度学习的余热回收系统优化方法，
通过引入自适应控制算法，实现了能效提升 15%。"
```

**输出**：
```
This paper proposes a deep learning-based optimization 
method for waste heat recovery systems. By introducing 
an adaptive control algorithm, we achieve a 15% 
improvement in energy efficiency.
```

### 示例 3：模拟审稿人

**输入**：
```
请帮我审阅这篇论文：
[粘贴论文全文]
投稿目标：IEEE Transactions on Industrial Informatics
```

**输出**：
```markdown
## Summary
This paper presents a novel approach to...

## Strengths
1. The proposed method shows significant improvement...
2. Experimental validation is comprehensive...

## Weaknesses (Critical)
1. Missing comparison with recent SOTA methods (2024-2025)
2. The ablation study lacks analysis on...
3. Computational complexity analysis is insufficient...

## Rating: 6/10

## Strategic Advice
1. Add comparison with [recent papers]...
2. Include ablation study on...
...
```

---

## 📁 项目结构

```
research-writing/
├── README.md              # 本文件
├── LICENSE                # MIT 许可证
├── SKILL.md               # 完整 Prompt 模板（OpenClaw 格式）
├── prompts/               # 独立 Prompt 文件（可选）
│   ├── 01-translate-cn-en.md
│   ├── 02-translate-en-cn.md
│   └── ...
└── examples/              # 使用示例（可选）
    ├── before-after.md
    └── case-studies.md
```

---

## 🎯 最佳实践

### 1. 组合使用
多个 Prompt 可以串联使用：
```
#21 生成大纲 → #22-25 扩展章节 → #6 润色 → #16 模拟审稿
```

### 2. 迭代优化
对 AI 生成的内容进行多轮优化：
```
初稿 → #7/#8 去 AI 味 → #6 润色 → #9 逻辑检查
```

### 3. 保持批判
使用 #16 模拟审稿人视角，提前发现问题

### 4. 数据真实
⚠️ **重要**：所有实验数据必须基于真实研究，AI 仅辅助表达

---

## 🔧 自定义与扩展

### 添加自己的 Prompt

在 `SKILL.md` 文件末尾添加新的 Prompt 模板：

```markdown
### 31. 你的自定义 Prompt

```markdown
# Role
[角色定义]

# Task
[任务描述]

# Constraints
[约束条件]

# Output Format
[输出格式]
```
```

### 调整现有 Prompt

根据自己领域的需求，修改 Prompt 中的：
- 专业术语
- 输出格式
- 约束条件

---

## 🤝 贡献指南

欢迎贡献！你可以通过以下方式帮助改进本项目：

1. **提交 Issue**：报告问题或建议新功能
2. **提交 PR**：改进现有 Prompt 或添加新模板
3. **分享案例**：提交使用案例和最佳实践
4. **翻译文档**：帮助翻译为其他语言

### 贡献流程

```bash
# 1. Fork 本仓库
# 2. 创建分支
git checkout -b feature/your-feature

# 3. 提交更改
git commit -m "Add: new prompt for XXX"

# 4. 推送到分支
git push origin feature/your-feature

# 5. 创建 Pull Request
```

---

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。你可以：
- ✅ 自由使用、修改、分发
- ✅ 用于商业目的
- ✅ 用于学术研究

需保留原作者署名和许可证声明。

---

## 🙏 致谢

- 基于 [awesome-ai-research-writing](https://github.com/awesome-ai-research-writing) 整理
- 感谢所有贡献者和用户
- 灵感来源于科研工作者的真实需求

---
**Happy Writing! 📝✨**
