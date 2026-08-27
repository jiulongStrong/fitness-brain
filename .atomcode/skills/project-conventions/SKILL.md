---
name: project-conventions
description: 健身 · 脑科学知识库项目的代码约定和风格。
  AtomCode 编写或审阅代码时自动应用。
user-invocable: false
---

## 项目概览

- **类型**: 纯静态 HTML/CSS 知识库网站
- **部署**: GitHub Pages（`jiulongStrong/fitness-brain`）
- **主题**: 深色模式（`#1a1a2e` 背景 + `#16213e` 卡片 + `#e0e0e0` 文字）

## 代码约定

### HTML
- 语言: `zh-CN`
- 编码: `UTF-8`
- 样式: 内联 `<style>` 标签，不使用外部 CSS 文件
- 响应式: 使用 `@media (max-width: 600px)` 断点
- 字体: `"PingFang SC","Microsoft YaHei",sans-serif`

### CSS 命名约定
- 颜色变量直接使用色值，无 CSS 变量
- 类名: kebab-case（如 `.card-title`, `.section-title`）
- 状态类: `.active`, `.highlight`, `.green`, `.yellow`, `.red-cell`

### 交互模式
- SVG 动画使用 `<animate>` / `<animateMotion>` 标签
- 交互使用原生 JavaScript（无框架）
- 数据存储在 HTML 内或 JSON 文件中

## 禁止
- 不引入外部 JS 依赖（无 React/Vue/jQuery）
- 不修改 `.gitignore` 中已忽略的文件类型（xlsx, docx, .playwright-mcp/）