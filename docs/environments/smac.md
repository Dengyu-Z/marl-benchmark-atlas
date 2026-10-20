# SMAC

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Control allied combat units against the built-in opponent. / 控制己方单位协同作战。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | StarCraft II + SMAC |
| Observations | local sight and available-action masks |
| Reward | dense or sparse; paper-specific |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Pin the StarCraft II build, maps, SMAC revision and reward mode. R3DM records SC2 4.10; another build is not automatically comparable.

## What to measure

Report win rate, return, map and evaluation action mode. Keep action-availability masks during evaluation.

## Getting started

Requires external game installation. Validate one process before parallel workers; a learner GPU is not the same as the simulator process.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official SMAC](https://github.com/oxwhirl/smac)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [R3DM: Enabling Role Discovery and Diversity Through Dynamics Models in Multi-agent Reinforcement Learning](../../papers/r3dm.md)
- [Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning](../../papers/lazy-agents.md)
- [Learning group collaboration for efficient multi-agent reinforcement learning](../../papers/g-mat.md)
- [In-Context Fully Decentralized Cooperative Multi-Agent Reinforcement Learning](../../papers/rac.md)

Tags: `coordination`, `heterogeneity`, `combat`
