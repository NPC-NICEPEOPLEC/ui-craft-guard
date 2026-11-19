# 几何、色彩和字级的校准方法

## 1. 同心圆角是关系，不是死公式

当外容器内侧均匀 inset `p`，两个圆角共享圆心且子容器有实底/描边时，常见近似是 `r_inner = max(0, r_outer - p)`。例如外 20、内距 8 → 内 12。CSS `border-radius`、边框盒模型、内外边距不均以及真实视觉曲率会使机械公式失效，应在截图中核对。对于透明、不同形状或多层卡片，以视觉对齐和功能边界优先。

```
:root { --radius-container: 20px; --card-inset: 8px; }
.card { border-radius: var(--radius-container); padding: var(--card-inset); }
.card__inner { border-radius: max(0px, calc(var(--radius-container) - var(--card-inset))); }
```

CSS `corner-shape: superellipse(...)` 可以表达连续曲率，但支持情况可能不一致：只能渐进增强、保留 `border-radius` 回退。不要承诺完全复刻 Apple iOS 曲率。

## 2. 用角色规定间距

- 宏观：页面左右 gutter / section gap / grid columns。先按内容密度决定，不是整个页面都是 16px。
- 中观：组件之间的逻辑关系，标题与描述通常比两组内容的距离更近。
- 微观：图标文字、标签胶囊、控件内部 padding，保持同一族的比例。
- 设置 token（如 4/8/12/16/24/32/48）是起点而非绝对刻度；光学修正要写明理由。

## 3. 颜色先分角色，再选数值

必需角色通常有：canvas、surface、text、muted、border、interactive、focus、success/warning/error。允许借用 Radix Scale 的色阶作为基准，但不能认为“使用了 Radix”就自动满足对比度。验证真实背景前景对、不同状态与两个主题。颜色是否强烈看任务：交易红字/风险警示与照片展示不是同一层面。

## 4. 字级少而清楚

建立 display、heading、body、meta 等语义角色；同一屏频繁出现近似字号通常是不必要的视觉噪声。不要因为“字号不超过四种”而把代码、图表、帮助文字强挤同一种尺寸。控制行长、中文断行、行高与权重。所有真实长文案要重新截图。

## 5. 视觉精修检查

1. 容器边缘、基线、图标/文本重心；
2. radius 家族；嵌套关系；
3. 同类边框粗细、阴影扩散与底色；
4. 卡片是否只是把原本连续的信息无意义地盒子化；
5. 对齐结果在 100%、125%、200% 缩放和常规/高 DPI 是否仍可用。

**参考：** https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape ； https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale
