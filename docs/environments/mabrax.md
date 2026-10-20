# MaBrax

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents control different joint groups of one robot. / 多个智能体共同控制机器人的不同关节。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | JaxMARL + Brax |
| Observations | local joint and root-body information |
| Reward | forward progress minus control costs |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

MaBrax uses Brax physics. Matching a MA-MuJoCo joint partition does not make simulation dynamics or reference returns identical.

## What to measure

Record robot, joint partition, observation radius, simulator backend and reward components; compare continuous-action-compatible baselines.

## Getting started

Sable uses five robot/partition tasks. Start with a small partition; benchmark compilation and rollout separately.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)

Tags: `continuous-control`, `heterogeneity`, `jax`
