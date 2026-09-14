# idea-to-design

以 PM/TM 身份，通过结构化对话帮助用户验证想法并产出完整的设计文档。

## 功能

- 自动检测项目上下文（已有项目 vs 全新项目）
- 引导用户经历完整流程：澄清需求 → 塑造 PRD → 技术设计 → 交付计划
- 每个阶段都通过针对性提问帮助用户理清思路
- 产出可直接用于开发的 PRD + 技术设计文档

## 适用场景

- 有一个模糊的想法，想变成具体可执行的方案
- 需要为新功能写 PRD 或技术设计文档
- 想验证一个想法是否值得做
- 在已有项目上迭代，需要规划下一个功能

## 输出

- Markdown 设计文档（保存到 `docs/` 目录或直接在对话中展示）
- 包含：需求、验收标准、架构决策、API 设计、数据模型、风险、待确认问题

## 安装

**本地项目：**
```bash
cp -r skills/idea-to-design .claude/skills/idea-to-design
```

**全局安装：**
```bash
cp -r skills/idea-to-design ~/.claude/skills/idea-to-design
```
