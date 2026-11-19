# 发布、安装与验收

## 公开仓库（已发布）

- GitHub：https://github.com/NPC-NICEPEOPLEC/ui-craft-guard
- 默认分支：`main`
- 核心 Skill 目录：`skills/ui-craft-guard/`
- 检查工作流：`.github/workflows/ci.yml`
- 截图生成工作流：`.github/workflows/screenshot-evidence.yml`
- 最新的实际测试证据见 [VALIDATION.md](VALIDATION.md) 和 [GitHub Actions](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions)。

这个仓库已创建并公开；不要重复执行 `gh repo create`，也不要覆盖 `main` 历史。

## 从公开仓库复制完整 Skill 到三个本机位置

在你自己的 Mac 终端运行以下命令。它会克隆公开仓库，把 **整个目录**复制到 `~/.dsh/skills/`、`~/.agents/skills/`、`~/.claude/skills/`，且遇到已安装的目录会跳过，不会覆盖既有版本：

```bash
git clone https://github.com/NPC-NICEPEOPLEC/ui-craft-guard.git
cd ui-craft-guard
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v

for root in "$HOME/.dsh/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$root"
  if [ -e "$root/ui-craft-guard" ]; then
    echo "SKIP (already exists): $root/ui-craft-guard"
  else
    cp -R skills/ui-craft-guard "$root/"
    echo "INSTALLED: $root/ui-craft-guard"
  fi
done
```

如需覆盖已有安装，请先备份、对比后再更新。仓库自带的 `scripts/install.sh` 也可用于单独安装至项目级 Codex/Claude Skills 目录。

验证：

```bash
for root in "$HOME/.dsh/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  test -f "$root/ui-craft-guard/SKILL.md" && \
  test -f "$root/ui-craft-guard/references/source-ledger.md" && \
  test -f "$root/ui-craft-guard/templates/AUDIT_REPORT.md" && \
  echo "PASS: $root/ui-craft-guard"
done
```

注意：GitHub 公开提交不等于自动复制到你的 Mac，也不等于安装成 ChatGPT Plugin。

## 本地运行验证

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/audit_ui.py examples/anti-pattern.html --format markdown
python3 scripts/audit_ui.py examples/revised.html --format markdown
```

`scripts/visual_smoke.py` 需另外安装 Playwright 与 Chromium；GitHub Actions 会在受支持的 Ubuntu 24.04 上安装运行，并把原创建模截图提交至 `examples/screenshots/`。

不要把静态规则扫描或 Chromium 冒烟测试表述为完整 WCAG 认证、真实用户测试或跨浏览器验证。
