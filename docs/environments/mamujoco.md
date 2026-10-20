# Multi-Agent MuJoCo

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Split a MuJoCo robot's actuators among collaborating agents. / 将 MuJoCo 机器人执行器分配给多个智能体。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | MA-MuJoCo / Gymnasium-Robotics variants |
| Observations | joint-partition and observation-radius dependent |
| Reward | robot-specific locomotion reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Original MA-MuJoCo, newer wrappers and MaBrax must be tracked as separate implementations. Match partition, MuJoCo version and observation configuration.

## What to measure

Report episode return, robot, partition and evaluation noise. Do not compare values across different reward normalizations.

## Getting started

Relevant for OptiMAPPO and MMQ. Use the implementation referenced by each paper rather than substituting a similarly named environment.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Original repository](https://github.com/schroederdewitt/multiagent_mujoco)
- [Gymnasium-Robotics](https://robotics.farama.org/)

## Papers in this edition

- [Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning](../../papers/mmq.md)
- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `continuous-control`, `heterogeneity`
