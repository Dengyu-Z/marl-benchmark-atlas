# Open-system Wildfire

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents and tasks can change during a wildfire-management episode. / 智能体或任务可在野火管理过程中变化。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 野火管理场景中的协作智能体 |
| 要完成什么 | 应对火情，同时处理智能体加入／离开或任务变化。 |
| 每一步做什么 | 具体局部动作集合尚未在本版核对。 |
| 动作到底是哪类 | 待核查；不能因为论文用了 DQN 就直接填整个环境的动作定义。 |
| 奖励何时出现 | 本版尚未完整抄录 WS1 的奖励细节。 |
| 可先比较的算法 | 先核对动作、动态人数接口和任务变更，再匹配算法；此条暂不自动推荐。 |

适用范围：Wildfire WS1 和开放性机制需从作者实现补充。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | paper-specific |
| Actions | unknown |
| Implementations | openness_CAP / Wildfire WS1 |
| Observations | open-agent-system configuration dependent |
| Reward | wildfire configuration dependent |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

WS1 and openness mechanisms must be preserved. Do not infer the local action space or independent training seed count from the prose alone.

## What to measure

Record entry/exit rules, task changes, time of changes and return. Fixed-seed evaluation episodes are not independent training replications.

## Getting started

Paper mapping only. Action-space details and install instructions are intentionally unresolved in this edition.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Paper code](https://github.com/bboyfury/openness_CAP)

## Papers in this edition

- [Challenges in Credit Assignment for Multi-Agent Reinforcement Learning in Open Agent Systems](../../papers/open-credit.md)

Tags: `agent-openness`, `task-openness`, `credit-assignment`
