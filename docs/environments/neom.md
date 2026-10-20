# NEOM (Sable scalability task)

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

A synthetic cooperative task for scaling to many agents. / 用于大规模智能体扩展实验的合成协作任务。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 共同拼出一维数值图案的位置／决策者 |
| 要完成什么 | 让所有人的离散选择拼成指定的周期图案，用于人数扩展实验。 |
| 每一步做什么 | 从图案允许的有限数值集合中选一个。 |
| 动作到底是哪类 | 离散；即使选项写成 0.2、0.5 等小数，有限选项仍然是离散动作。 |
| 奖励何时出现 | 按图案偏差给反馈，正确匹配还有与时间有关的额外奖励。 |
| 可先比较的算法 | 论文测试 Sable 等扩展性；一般算法还需任务接口。不要将算法已发表结果当作本仓库复现。 |

适用范围：Sable 附录 B.7；额外扩展任务，不在 45 个主任务中。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | paper-specific |
| Actions | discrete |
| Implementations | Sable paper/code |
| Observations | position target and action-history description in paper |
| Reward | paper-defined coordination reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

NEOM belongs to the additional scalability study, not the six-suite 45-task main performance benchmark. A current public API path is not verified in this edition.

## What to measure

Record agent count, solved coordination criteria, memory and throughput; distinguish recurrent context scaling from agent scaling.

## Getting started

Consult Sable Section 4.2 and Appendix B.7. No local smoke recipe or current upstream API is asserted.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Sable / Mava](https://github.com/instadeepai/Mava)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)

Tags: `scalability`, `coordination`
