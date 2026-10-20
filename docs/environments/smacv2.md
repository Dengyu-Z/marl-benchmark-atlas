# SMACv2

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Randomized unit teams and starting conditions extend SMAC. / 随机化队伍与初始条件的战斗协作基准。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | StarCraft II + SMACv2 |
| Observations | local sight; configuration-dependent |
| Reward | configuration-dependent combat reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Do not confuse engine-based SMACv2 with SMAX tasks named smacv2_*_units. Race, team generator, unit distribution and field of view must be recorded.

## What to measure

Report win rate and return over held-out episode seeds; separate training seeds from evaluation seeds.

## Getting started

Run the provided optional protoss_5_vs_5 smoke recipe only after SC2 and the required maps are installed. Install cost is not a measured runtime estimate.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official SMACv2](https://github.com/oxwhirl/smacv2)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [R3DM: Enabling Role Discovery and Diversity Through Dynamics Models in Multi-agent Reinforcement Learning](../../papers/r3dm.md)

Tags: `coordination`, `heterogeneity`, `population-generalization`, `combat`
