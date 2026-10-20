# Paper → environment index

[Home](../README.md) · [中文](../README.zh-CN.md)

16 supplied papers: 15 benchmark-related mappings and one LLM-RL background paper. This is a curated starting set, not a systematic survey. Policy regimes describe the method or experiment, not the simulator. VMAS in the CAMAR paper is a simulator-speed comparison; RAC Predator and Prey remains paper-specific.

| Paper card | Year | Policy regime | Training / execution | Environment families |
| --- | --- | --- | --- | --- |
| [sable](../papers/sable.md) | 2025 | on-policy | centralized autoregressive execution | RWARE / Robot Warehouse, Level-Based Foraging, Connector, SMAX, MaBrax, MPE / MPE2, NEOM (Sable scalability task) |
| [entropy-mechanism](../papers/entropy-mechanism.md) | 2025 | background | single-agent language-model RL | Background only |
| [cee](../papers/cee.md) | 2026 | off-policy | CTDE; value decomposition | SMAC, SMACv2, Google Research Football |
| [r3dm](../papers/r3dm.md) | 2025 | off-policy | CTDE; QMIX backbone | SMAC, SMACv2 |
| [lazy-agents](../papers/lazy-agents.md) | 2023 | off-policy | CTDE; QMIX backbone | SMAC, Google Research Football |
| [g-mat](../papers/g-mat.md) | 2026 | on-policy | group communication; sequential policy | SMAC, Google Research Football |
| [communication-priors](../papers/communication-priors.md) | 2025 | off-policy | CC-MADDPG; constrained communication | MPE / MPE2 |
| [rac](../papers/rac.md) | 2025 | off-policy | fully decentralized; return-aware context | Didactic coordination games, SMAC |
| [magpo](../papers/magpo.md) | 2026 | on-policy | centralized guidance; decentralized actors | Didactic coordination games, Level-Based Foraging, Connector, MPE / MPE2, RWARE / Robot Warehouse, SMAX |
| [camar-paper](../papers/camar-paper.md) | 2026 | mixed | on-policy and off-policy baselines; planning | CAMAR, VMAS |
| [aggregate-advantage](../papers/aggregate-advantage.md) | 2026 | on-policy | PPO; graph-local aggregation | Didactic coordination games, SUMO-RL traffic signals |
| [open-credit](../papers/open-credit.md) | unresolved | mixed | DQN and MAPPO | Open-system Wildfire |
| [safe-marl](../papers/safe-marl.md) | 2025 | on-policy | constrained actor-critic; graph policy | MPE / MPE2 |
| [dico](../papers/dico.md) | 2024 | mixed | MADDPG/MAPPO through BenchMARL | VMAS |
| [mmq](../papers/mmq.md) | 2024 | off-policy | decentralized MaxMax Q-learning | Didactic coordination games, MPE / MPE2, Multi-Agent MuJoCo |
| [optimappo](../papers/optimappo.md) | 2024 | on-policy | optimistic MAPPO; CTDE | Didactic coordination games, Multi-Agent MuJoCo, Overcooked |
