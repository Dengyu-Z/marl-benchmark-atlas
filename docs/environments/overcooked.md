# Overcooked

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Two cooks coordinate ingredient preparation, cooking and delivery. / 两名厨师协同备料、烹饪与送餐。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 合作厨房里的两名厨师 |
| 要完成什么 | 分工拿食材、做汤、装盘和送餐，减少互相挡路。 |
| 每一步做什么 | 从走动、等待、交互等命令中选一个。 |
| 动作到底是哪类 | 离散；任务由布局和规则决定。 |
| 奖励何时出现 | 最终送餐奖励与训练时的辅助塑形奖励要分开记录。 |
| 可先比较的算法 | MAPPO／HAPPO；离散价值分解方法也需合作奖励与对应 wrapper。适合显式设计队友泛化实验。 |

适用范围：Overcooked-AI 布局任务；不等同于 OvercookedV2。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | overcooked_ai and paper wrappers |
| Observations | layout/featurizer dependent |
| Reward | sparse deliveries; optional shaping |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Different layouts, shaping schedules and wrappers change the problem. Overcooked and OvercookedV2 are distinct implementations.

## What to measure

Report sparse delivery score, shaped training reward separately, layout, horizon and partner protocol.

## Getting started

Useful for role/partner experiments, but held-out partners and layouts must be designed explicitly; they are not guaranteed by a single training run.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official Overcooked-AI](https://github.com/HumanCompatibleAI/overcooked_ai)

## Papers in this edition

- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `coordination`, `role-specialization`, `partner-generalization`
