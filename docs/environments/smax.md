# SMAX

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

A JAX combat simulator inspired by SMAC, without the StarCraft II engine. / 无需星际争霸引擎的 JAX 战斗协作环境。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | JaxMARL |
| Observations | local combat observations |
| Reward | combat shaping plus victory reward in Sable |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

SMAX is not SMAC or engine-based SMACv2. The three smacv2_*_units labels in Sable are still SMAX tasks. Never merge their win-rate or return tables.

## What to measure

Record win rate and return separately, unit composition, opponent generator, attack availability and reward settings.

## Getting started

Useful for accelerator-based combat experiments; separate compile time from steady-state throughput.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `coordination`, `heterogeneity`, `jax`
