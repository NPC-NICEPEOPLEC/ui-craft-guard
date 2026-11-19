# 中文 UI 的独立验收清单

中文 UI 不是英文 UI 的简单翻译。中英混排的字体回退、字重、标点和长文本会改变布局。

## Font stack（示例，不要求照抄）

```css
:root {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", "Source Han Sans SC",
    sans-serif;
}
```

这一写法体现系统优先、中文覆盖、generic fallback；并不保证所有用户系统上同一字形。字体文件要确认授权、缓存和体积；有特定自托管字体时考虑子集化、动态字符覆盖、fallback 稳健性。不要直接引用缺乏长期保障的第三方字体 CDN。

## 必测内容

- 6 字 / 14 字 / 28 字中文标题是否自然换行；卡片高是否被拉断、按钮是否挤压。
- 例如“11月19日 19:30｜￥1,299.00”中数字和中文的基线、空格、标点和宽度。
- 手机常见尺寸下二级说明是否可读；字号放大、浏览器字体替换是否破版。
- 加粗标题是否发生系统合成字重、中文字形变化；全角标点在两端是否突兀。
- 禁止仅为美观删掉格式说明或状态反馈；“无意义文案”需以任务上下文认定。

**取材：** @ricouii 字体栈与字体子集讨论，见 source-ledger；工程补充为本仓库整理。
