# Connector

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents draw non-crossing paths from start to target without trapping each other. / 路径一旦走过就会阻塞，需协作连接起点与终点。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 各自画一条线的路径头 |
| 要完成什么 | 从各自起点连到各自终点；已经画过的线会挡住其他路径。 |
| 每一步做什么 | 从停止、上下左右中选一个。 |
| 动作到底是哪类 | 离散：5 个命令。 |
| 奖励何时出现 | Sable 设置中，接通给奖励，接通前有步数惩罚；不是纯粹零奖励直到成功。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX；要统一团队目标、局部观测 wrapper 和奖励聚合。 |

适用范围：Sable 附录 B.4 的局部观测与奖励设置。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Jumanji |
| Observations | Sable uses a local-view wrapper |
| Reward | connection reward plus step penalty in Sable |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Sable Appendix B.4 gives a paper-specific observation and reward description. Paper labels such as con-5x5x3a are not guaranteed to be registered environment IDs.

## What to measure

Report connected-agent fraction, return and time to completion. Distinguish reward aggregation per agent from team sums.

## Getting started

Use the smallest paper task before raising grid size and number of paths. Keep generator, wrapper and reward parameters with results.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Jumanji](https://github.com/instadeepai/jumanji)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `coordination`, `routing`, `jax`
