# Level-Based Foraging

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents combine levels to collect food that may be impossible to collect alone. / 智能体通过等级配合采集食物。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 有不同等级的采集者 |
| 要完成什么 | 在网格里找食物；单人搬不动时，多人靠近并共同 LOAD。 |
| 每一步做什么 | 从停止、上下左右、LOAD 中选一个。 |
| 动作到底是哪类 | 离散：每个智能体 6 个命令。 |
| 奖励何时出现 | 采集到食物才有奖励；是不是必须合作由食物等级和 force_coop 决定。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX／VDN；HASAC 需使用 HARL 的离散动作分支和适配环境。 |

适用范围：原版 LBF 与 Sable 采集任务；参数和奖励归一化仍需分别记录。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Jumanji / lb-foraging |
| Observations | full or sight-limited, by task |
| Reward | food collection; normalization depends on implementation |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Smoke passed for the specific MPE2/Python LBF recipe; see [ledger](../verification.md) |

## What changes comparability

force_coop, sight, food levels, normalization and episode limits change the task. Sable also modifies observation packing in its additional scalability experiment; do not silently apply that modification to all LBF runs.

## What to measure

Report return and food completion; define any joint-load event and its denominator. A positive conditional load-success rate does not imply higher total episode return.

## Getting started

Use the original Python API for a small reset/step check; use the paper-pinned Jumanji/Mava configuration for a Sable comparison.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Jumanji](https://github.com/instadeepai/jumanji)
- [Original LBF](https://github.com/semitable/lb-foraging)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `sparse-reward`, `coordination`, `heterogeneity`, `jax`
