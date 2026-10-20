# Controlling Behavioral Diversity in Multi-Agent Reinforcement Learning

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | ICML 2024 |
| Policy regime | mixed |
| Training / execution | MADDPG/MAPPO through BenchMARL |
| Evidence locator | Sections 6–7; Appendix A |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

VMAS tasks include multi-agent navigation and cooperative/competitive diversity studies. Parameter sharing and desired System Neural Diversity are experimental factors.

[VMAS](../docs/environments/vmas.md)

## Protocol details retained

BenchMARL and TorchRL are the reported training stack. Diversity is measured behaviorally; policy entropy alone is not the diversity metric.

## Source and implementation

[Paper / primary record](https://proceedings.mlr.press/v235/bettini24a.html)

[Author code](https://github.com/proroklab/ControllingBehavioralDiversity)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
