# CAMAR

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Continuous multi-agent routing with obstacles and configurable dynamics. / 含障碍和不同动力学的连续多智能体路径规划。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | CAMAR |
| Observations | local vector observations |
| Reward | goal, path and collision terms |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Holonomic versus other dynamics, maps, agent sizes and collision handling define different tasks. Reported simulator SPS is not a claim about learner end-to-end speed.

## What to measure

Use goal-reaching success, time/path quality and collision metrics together; retain the benchmark's tiered evaluation protocol.

## Getting started

This edition provides a literature card and upstream links, without a local installation or a performance claim.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official CAMAR](https://github.com/AIRI-Institute/CAMAR)
- [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/40209)

## Papers in this edition

- [CAMAR: Continuous Actions Multi-Agent Routing](../../papers/camar-paper.md)

Tags: `routing`, `continuous-control`, `heterogeneity`
