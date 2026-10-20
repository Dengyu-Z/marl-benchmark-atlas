# Didactic coordination games

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Small games isolate coordination failures and relative overgeneralization. / 用可控小博弈隔离协作与相对过度泛化机制。

| Field | This entry |
| --- | --- |
| Resource type | paper-specific |
| Actions | both |
| Implementations | paper-specific implementations |
| Observations | constant, phase or context observation |
| Reward | explicit payoff/coupling design |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

RAC matrix games, MAGPO CoordSum, MMQ differential games and MAPO graph-coupled games are distinct tasks. This grouping is for discovery, not for pooling numerical results.

## What to measure

Publish payoff table, horizon, initial-state distribution, observation and optimal joint solution. A toy-game effect does not establish general benchmark improvement.

## Getting started

Use for a fast mechanism check before a larger simulator. Select the exact game and retrieve the original implementation from the relevant paper card.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

See the linked paper cards for each game implementation.

## Papers in this edition

- [In-Context Fully Decentralized Cooperative Multi-Agent Reinforcement Learning](../../papers/rac.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)
- [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](../../papers/aggregate-advantage.md)
- [Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning](../../papers/mmq.md)
- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `mechanism-diagnosis`, `relative-overgeneralization`, `credit-assignment`
