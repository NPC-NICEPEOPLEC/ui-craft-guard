# 发布、更新及本机验证

公开仓库：https://github.com/NPC-NICEPEOPLEC/ui-craft-guard  
完整 Skill 位于 `skills/ui-craft-guard/`，版本以其 `VERSION` 为准。GitHub `main` 不会自动同步到本地 DSH、Codex、Claude，也不等同安装 ChatGPT Plugin。

## 推荐：浏览器 ZIP 下载 + 本地安全更新

如果终端的 `git clone` 报 `HTTP2 framing layer` 或 `Empty reply from server`，无需重复克隆。

1. 浏览器访问 https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/archive/refs/heads/main.zip ，下载完整 ZIP。
2. 在 Finder 解压并打开 `ui-craft-guard-main` 文件夹（若重名被自动加后缀，请使用实际文件夹）。
3. 在该**仓库根目录**的终端运行：

```bash
bash scripts/update_user_skills.sh
```

该脚本不联网；先检查完整 Skill 来源并读取 `VERSION`，再分别安装到（务必下载最新 ZIP，旧 ZIP 仍会安装它自身对应的旧版本）：

```text
~/.dsh/skills/ui-craft-guard/
~/.agents/skills/ui-craft-guard/
~/.claude/skills/ui-craft-guard/
```

已存在的同名目录会被备份为 `ui-craft-guard.backup-<时间戳>-<进程号>`，仍保留在原 skills 目录，不触碰其他 Skill。在拷贝阶段失败时旧版保持原样。macOS 使用 `ditto`；Linux 测试环境使用 `cp -R` 回退。

## 本机版本检查

```bash
for root in "$HOME/.dsh/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  echo "$root/ui-craft-guard:"
  cat "$root/ui-craft-guard/VERSION"
  test -f "$root/ui-craft-guard/SKILL.md"
  test -f "$root/ui-craft-guard/references/design-principles.md"
  test -f "$root/ui-craft-guard/references/evidence-protocol.md"
  test -f "$root/ui-craft-guard/scripts/validate_report.py"
done
```

当前 Skill 版本请核对仓库的 [`VERSION`](skills/ui-craft-guard/VERSION)（本次文档更新为 `0.2.2`）；重新启动客户端后实际验证其发现与调用能力。审计 JSON 版本 `0.2.1` 是独立契约，不能误当 Skill 版本。

## 可选 Git / 首次安装

如果 Git HTTPS 正常，可从仓库根目录运行 `bash scripts/install.sh dsh /path/to/project`（Codex、Claude 分别将 `dsh` 替换为 `codex` 或 `claude`）。`install.sh` 遇到已有目标会拒绝覆盖；更新已有版本用 `update_user_skills.sh`。

## 质量边界

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_report.py examples/audit-cases/*.json
python3 -m unittest discover -s tests -v
```

真实 CI、合成 JSON 案例、旧版截图冒烟的证据见 [VALIDATION.md](VALIDATION.md) 与 [GitHub Actions](https://github.com/NPC-NICEPEOPLEC/ui-craft-guard/actions)。它们不会自动证明网站的审美质量、完整 WCAG 合规或真实用户满意度。
