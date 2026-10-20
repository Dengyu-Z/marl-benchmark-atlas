# Scalable Safe Multi-Agent Reinforcement Learning for Multi-Agent System

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | supplied arXiv:2501.13727v2 |
| Policy regime | on-policy |
| Training / execution | constrained actor-critic; graph policy |
| Evidence locator | Section 5; safety and scalability appendices |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

SS-MARL modifies MPE for safety-aware cooperative navigation. Each agent has its own goal and costs are tracked separately from rewards.

[MPE / MPE2](../docs/environments/mpe.md)

## Protocol details retained

The paper uses 100-step episodes in the discussed safety experiment. Safety costs, thresholds, obstacle counts and population-size transfer must accompany reported return.

## Source and implementation

[Paper / primary record](https://arxiv.org/abs/2501.13727)

Author code URL not verified; no guessed repository is listed.

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
