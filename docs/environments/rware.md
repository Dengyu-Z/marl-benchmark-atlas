# RWARE / Robot Warehouse

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Robots fetch shelves, deliver requested goods, and avoid blocking one another. / 机器人搬运货架、配送并避免相互阻塞。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 搬货机器人 |
| 要完成什么 | 在仓库里取出指定货架，送到配送口，再继续取货。 |
| 每一步做什么 | 从停止、前进、左转、右转、装卸货架中选一个。 |
| 动作到底是哪类 | 离散：5 个命令；不是输出前进距离。 |
| 奖励何时出现 | 配送成功才得到任务奖励；长时间没有成功配送就可能没有正奖励。 |
| 可先比较的算法 | MAPPO／HAPPO；使用合作团队目标与相应接口时也可比较 QMIX／VDN。 |

适用范围：RWARE 配送任务；Sable 附录 B.1。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Jumanji / original Python |
| Observations | partial grid view |
| Reward | sparse delivery reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Sable Appendix B.1 explicitly says its Jumanji implementation terminates on a collision, unlike the original collision-resolution logic. Check the exact revision and wrapper before transferring scores.

## What to measure

Use delivery count/return, collision and early-termination rates. A time limit and a collision terminal are different outcomes.

## Getting started

Start with tiny tasks; add warehouse size, number of robots and request difficulty separately. The original Python environment and Sable Jumanji setup are separate configurations.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Jumanji](https://github.com/instadeepai/jumanji)
- [Original RWARE](https://github.com/semitable/robotic-warehouse)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `sparse-reward`, `coordination`, `congestion`, `jax`
