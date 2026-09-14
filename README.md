# Yunzhuan Skill

个人 Codex skills 集合，收录本地 `~/.codex/skills` 中的 **41 个技能**，包含原始 `SKILL.md`、参考文档、脚本和资源。

适用于需求与方案、研发流程、前端设计与动效、文档与内容制作、项目测试等场景。完整列表见 [Skills 目录](SKILLS.md)。

## 目录结构

```text
skills/<技能目录>/SKILL.md   技能入口及配套文件
SKILLS.md                  技能与用途索引
manifest.json              导入文件清单与 SHA-256
THIRD_PARTY.md             第三方来源与许可说明
```

## 安装单个技能

在 PowerShell 中克隆仓库，从 [Skills 目录](SKILLS.md) 选择需要的技能并填写目录名，再复制完整目录。遇到同名目录会停止，避免覆盖已有版本。

```powershell
git clone https://github.com/Ratel-pwn/Yunzhuan-skill.git
Set-Location Yunzhuan-skill

$skillName = '<技能目录名>' # 选择并替换
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillRoot = Join-Path $codexRoot 'skills'
$destination = Join-Path $skillRoot $skillName
$source = Join-Path '.\skills' $skillName
if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) { throw '请填写有效的技能目录名' }
if (Test-Path -LiteralPath $destination) { throw "技能已存在：$destination" }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
Test-Path -LiteralPath (Join-Path $destination 'SKILL.md')
```

最后一条命令返回 `True` 表示入口文件已复制。按使用端的技能发现机制刷新或重新开启会话；是否能执行，还取决于技能所需的工具与依赖。

## 使用条件

- 每个技能的适用范围和前置条件见自己的 `SKILL.md`。安装技能不会自动安装 Node.js、Python、ADB、浏览器工具、MCP 或 API 服务。
- 按各自说明配置外部工具、项目环境、素材库和服务凭据。
- 部分技能有相互调用或宿主工具要求，选择安装时请同时检查其引用的技能。

## 收录范围与校验

快照日期：2026-09-14。仅收录 `~/.codex/skills` 中含 `SKILL.md` 的目录，排除系统内置、空目录和已确认不可用的项目；不包含 `.agents/skills`、插件缓存、账号配置或会话记录。

技能文件按原样收录，导入时逐文件校验 SHA-256。`.gitattributes` 禁用自动换行转换，以保留快照字节。此校验确认复制完整性，不代表每个技能已完成运行验证。

在仓库根目录可重新校验：

```powershell
$manifest = Get-Content -LiteralPath '.\manifest.json' -Raw | ConvertFrom-Json
$failures = @($manifest.files | Where-Object {
    -not (Test-Path -LiteralPath $_.path -PathType Leaf) -or
    (Get-FileHash -LiteralPath $_.path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $_.sha256
})
if ($failures.Count) { throw "校验失败：$($failures.Count) 个文件" }
"校验通过：$($manifest.file_count) 个文件"
```
