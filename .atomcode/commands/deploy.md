---
name: deploy
description: 提交并推送当前改动到 GitHub Pages
disable-model-invocation: true
---

执行一键发布到 GitHub Pages：

1. 运行 `git status` 确认当前改动
2. `git add -A`
3. 运行 `git diff --cached --stat` 确认将要提交的改动
4. 以中文提交信息执行 `git commit -m "<ARGUMENTS>"`（不添加 AI 标识）
5. `git push origin main`
6. 汇报：改动内容 + 预计 1-2 分钟生效的 Pages 链接
