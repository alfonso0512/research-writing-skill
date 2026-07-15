# 发布到 GitHub 指南

> 将科研论文写作助手发布到 GitHub，供全球科研人使用

---

## 📋 发布前检查清单

- [x] ✅ `README.md` - 项目说明文档
- [x] ✅ `LICENSE` - MIT 许可证
- [x] ✅ `SKILL.md` - 完整 Prompt 模板
- [x] ✅ `QUICKSTART.md` - 快速上手指南
- [x] ✅ `.gitignore` - Git 忽略文件
- [x] ✅ Git 仓库已初始化并提交

---

## 🚀 发布步骤

### Step 1: 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 **+** → **New repository**
3. 填写仓库信息：

| 字段 | 建议值 | 说明 |
|------|--------|------|
| Repository name | `research-writing-skill` | 仓库名称 |
| Description | `🎓 AI 科研论文写作助手 - 30 个 Prompt 模板覆盖论文写作全流程` | 仓库描述 |
| Public/Private | **Public** | 选择公开 |
| Initialize with README | **不要勾选** | 我们已经有 README 了 |

4. 点击 **Create repository**

---

### Step 2: 推送代码到 GitHub

创建仓库后，GitHub 会显示推送指令。执行以下命令：

```bash
# 进入仓库目录
cd C:\Users\acer\.openclaw\workspace\skills\research-writing

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/research-writing-skill.git

# 推送代码
git branch -M main
git push -u origin main
```

**如果遇到认证问题**，使用 Personal Access Token：

```bash
# 使用 Token 推送（替换 TOKEN 为你的 GitHub Token）
git push https://YOUR_USERNAME:TOKEN@github.com/YOUR_USERNAME/research-writing-skill.git main
```

---

### Step 3: 获取 GitHub Token（如果需要）

1. 登录 GitHub
2. 点击右上角头像 → **Settings**
3. 左侧菜单 → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
4. 点击 **Generate new token (classic)**
5. 填写：
   - **Note**: `research-writing-skill deploy`
   - **Expiration**: `No expiration`（或选择合适的时间）
   - **Scopes**: 勾选 `repo`（完整控制私有仓库）
6. 点击 **Generate token**
7. **复制 Token**（只显示一次，妥善保存）

---

### Step 4: 完善仓库信息

推送成功后，在 GitHub 仓库页面：

#### 4.1 添加主题标签（Topics）

点击 **Manage topics**，添加：

```
ai-writing
research
academic-writing
prompt-engineering
openclaw
skill
paper-writing
scientific-writing
```

#### 4.2 设置网站预览（可选）

如果想让仓库更专业：

1. **Settings** → **Pages**
2. **Source**: `Deploy from a branch`
3. **Branch**: `main` / `/(root)`
4. 点击 **Save**

GitHub Pages 会生成一个预览网站。

#### 4.3 添加社交媒体预览（可选）

创建 `.github/social-preview.png` 文件，作为仓库封面图。

---

## 📢 推广建议

### 1. 分享到科研社区

| 平台 | 建议 |
|------|------|
| 知乎 | 写一篇文章介绍使用体验 |
| 小红书 | 发笔记分享科研工具 |
| 微博 | 简短介绍 + GitHub 链接 |
| 学术微信群 | 分享给同行 |
| 学校论坛 | 发帖推荐 |

### 2. 分享到开发者社区

| 平台 | 说明 |
|------|------|
| GitHub Trending | 争取上热门 |
| V2EX | 发到「程序员」节点 |
| 掘金 | 写技术文章介绍 |
| OpenCode 社区 | Discord / 微信群 |

### 3. 联系意见领袖

- 科研博主
- 学术大 V
- OpenClaw 官方账号

---

## 📊 维护建议

### 定期更新

- [ ] 收集用户反馈，改进 Prompt
- [ ] 添加新的使用场景
- [ ] 更新文档和示例
- [ ] 发布新版本（v2.1, v2.2...）

### 响应用户

- [ ] 及时回复 Issues
- [ ] 审核和合并 Pull Requests
- [ ] 在 Discussion 中回答问题

### 数据分析

- [ ] 查看 GitHub Insights（Star、Fork、克隆数）
- [ ] 了解用户分布（国家、时间）
- [ ] 根据数据优化推广策略

---

## 🎯 成功指标

| 指标 | 目标（3 个月） | 目标（1 年） |
|------|---------------|-------------|
| ⭐ Stars | 100+ | 500+ |
| 🍴 Forks | 20+ | 100+ |
| 👀 Views | 1000+ | 10000+ |
| 📥 Clones | 100+ | 1000+ |

---

## 🙏 发布后记得

1. **告诉雨哥**：发布成功！
2. **记录到 MEMORY.md**：记下发布时间和链接
3. **持续维护**：定期查看 Issues 和反馈
4. **收集案例**：整理用户成功案例

---

## 📬 需要帮助？

- GitHub 文档：https://docs.github.com
- OpenClaw 社区：https://discord.com/invite/clawd
- 遇到问题：在仓库中提 Issue

---

**祝发布成功！让更多人受益于这个工具！🚀✨**
