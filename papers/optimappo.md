# Optimistic Multi-Agent Policy Gradient

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | ICML 2024 |
| Policy regime | on-policy |
| Training / execution | optimistic MAPPO; CTDE |
| Evidence locator | Sections 5.1–5.5; Appendix C |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

Repeated matrix games, Multi-Agent MuJoCo and Overcooked. Task-specific penalties in the didactic games probe relative overgeneralization.

[Didactic coordination games](../docs/environments/coordination-games.md), [Multi-Agent MuJoCo](../docs/environments/mamujoco.md), [Overcooked](../docs/environments/overcooked.md)

## Protocol details retained

Do not replace MA-MuJoCo with MaBrax and retain the same reference scores. Preserve Overcooked layouts and sparse/shaped reward settings.

## Source and implementation

[Paper / primary record](https://proceedings.mlr.press/v235/zhao24v.html)

[Author code](https://github.com/wenshuaizhao/optimappo)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
