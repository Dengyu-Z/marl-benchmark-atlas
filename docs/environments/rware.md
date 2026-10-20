# RWARE / Robot Warehouse

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Robots fetch shelves, deliver requested goods, and avoid blocking one another. / 机器人搬运货架、配送并避免相互阻塞。

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
