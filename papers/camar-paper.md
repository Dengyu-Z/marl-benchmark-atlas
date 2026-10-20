# CAMAR: Continuous Actions Multi-Agent Routing

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | AAAI 2026 |
| Policy regime | mixed |
| Training / execution | on-policy and off-policy baselines; planning |
| Evidence locator | Experimental Evaluation and Evaluation Protocols, PDF pp.5–7 |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

Continuous routing benchmark; VMAS is also used for a simulator scalability comparison. Simulator throughput and trained policy quality are separate measurements.

[CAMAR](../docs/environments/camar.md), [VMAS](../docs/environments/vmas.md)

## Protocol details retained

Includes IPPO, MAPPO, IDDPG, MADDPG, ISAC and MASAC plus planning baselines. Record success, path quality and collisions; throughput depends on workload and hardware.

## Source and implementation

[Paper / primary record](https://ojs.aaai.org/index.php/AAAI/article/view/40209)

[Author code](https://github.com/AIRI-Institute/CAMAR)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
