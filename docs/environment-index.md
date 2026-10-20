# Environment and dataset index

[Home](../README.md) · [中文](../README.zh-CN.md)

Generated from `data/environments.json`. Each row is scoped to named implementations. `both` means the family supports discrete and continuous actions; a specific task may support only one. `unknown` is unresolved, not an assumption. Runtime labels must be read with the [verification ledger](verification.md).

| Resource | Kind | Actions | Implementations | Research tags | Runtime |
| --- | --- | --- | --- | --- | --- |
| [RWARE / Robot Warehouse](environments/rware.md) | online | discrete | Jumanji / original Python | sparse-reward, coordination, congestion, jax | not_run |
| [Level-Based Foraging](environments/lbf.md) | online | discrete | Jumanji / lb-foraging | sparse-reward, coordination, heterogeneity, jax | smoke_passed |
| [Connector](environments/connector.md) | online | discrete | Jumanji | coordination, routing, jax | not_run |
| [SMAX](environments/smax.md) | online | discrete | JaxMARL | coordination, heterogeneity, jax | not_run |
| [MaBrax](environments/mabrax.md) | online | continuous | JaxMARL + Brax | continuous-control, heterogeneity, jax | not_run |
| [MPE / MPE2](environments/mpe.md) | online | both | JaxMARL / MPE2 / historical MPE | coordination, communication, continuous-control | smoke_passed |
| [SMAC](environments/smac.md) | online | discrete | StarCraft II + SMAC | coordination, heterogeneity, combat | not_run |
| [SMACv2](environments/smacv2.md) | online | discrete | StarCraft II + SMACv2 | coordination, heterogeneity, population-generalization, combat | not_run |
| [Multi-Agent MuJoCo](environments/mamujoco.md) | online | continuous | MA-MuJoCo / Gymnasium-Robotics variants | continuous-control, heterogeneity | not_run |
| [VMAS](environments/vmas.md) | online | both | PyTorch vectorized simulator | coordination, behavioral-diversity, continuous-control, vectorized | not_run |
| [Google Research Football](environments/grf.md) | online | discrete | Football engine + Python wrappers | sparse-reward, coordination, sports | not_run |
| [Overcooked](environments/overcooked.md) | online | discrete | overcooked_ai and paper wrappers | coordination, role-specialization, partner-generalization | not_run |
| [CAMAR](environments/camar.md) | online | continuous | CAMAR | routing, continuous-control, heterogeneity | not_run |
| [Didactic coordination games](environments/coordination-games.md) | paper-specific | both | paper-specific implementations | mechanism-diagnosis, relative-overgeneralization, credit-assignment | not_run |
| [Open-system Wildfire](environments/open-wildfire.md) | paper-specific | unknown | openness_CAP / Wildfire WS1 | agent-openness, task-openness, credit-assignment | not_run |
| [SUMO-RL traffic signals](environments/sumo-rl.md) | online | discrete | SUMO + sumo-rl | graph-coupling, credit-assignment, traffic | not_run |
| [OG-MARL](environments/og-marl.md) | offline-dataset | both | offline dataset collection + baseline code | offline-rl, dataset-quality, coverage | not_run |
| [NEOM (Sable scalability task)](environments/neom.md) | paper-specific | discrete | Sable paper/code | scalability, coordination | not_run |
