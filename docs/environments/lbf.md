# Level-Based Foraging

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents combine levels to collect food that may be impossible to collect alone. / 智能体通过等级配合采集食物。

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
