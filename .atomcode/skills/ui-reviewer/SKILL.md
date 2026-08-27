---
name: ui-reviewer
description: 审查静态 HTML 页面的响应式适配、可访问性和移动端兼容性。适合本项目（纯静态 HTML 知识库）的页面质量检查。
user-invocable: true
---

# UI Reviewer — 静态 HTML 页面审查

对本项目（fitness-brain 知识库）的 HTML 页面做只读审查，检查以下维度：

## 审查清单

### 1. 响应式适配（移动端兼容）
- 页面是否包含 `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- 是否使用 `@media (max-width: 600px)` 断点
- 表格在窄屏下是否溢出（应允许横向滚动或调整列布局）
- SVG/图片是否有 `max-width: 100%` 或按比例缩放
- 容器是否有 `overflow-x` 处理

### 2. 可访问性
- 标题层级是否合理（h1 → h2 → h3，不跳级）
- 链接是否有可读的文本内容
- 对比度是否足够（深色主题 `#1a1a2e` 背景 + `#e0e0e0` 文字为基准）
- 是否有 `lang="zh-CN"` 属性

### 3. 一致性（对照项目约定）
- 主题色是否统一（`#1a1a2e` / `#16213e` / `#e0e0e0`）
- 字体是否使用 `"PingFang SC","Microsoft YaHei",sans-serif`
- 样式是否内联 `<style>`（不引入外部 CSS/JS）

### 4. 结构正确性
- HTML 标签是否闭合
- 表格 `th`/`td` 数量是否一致
- 是否有未转义的特殊字符

## 输出格式

对每个页面输出：
- ✅ 通过项（简述）
- ⚠️ 问题项（具体行号/位置 + 修复建议）
- 总体结论（合格 / 需修复）

只读审查，不修改文件。发现问题后给出修复建议即可。
