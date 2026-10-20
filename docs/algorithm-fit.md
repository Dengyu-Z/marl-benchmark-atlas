# Match algorithms to environment requirements

[Home](../README.md) · [中文详解](algorithm-fit.zh-CN.md) · [Visual task overview](environment-overview.zh-CN.md)

**Start with action-space compatibility, then check the information and data assumptions.** Compatibility is not a performance ranking or a reproduced result.

| Implementation scope | Discrete | Continuous | Training regime |
| --- | --- | --- | --- |
| Standard QMIX / VDN | Yes | Not directly | Off-policy |
| MAPPO | Yes | Yes | On-policy |
| HARL HAPPO | Yes | Yes | On-policy |
| HARL HASAC | Yes | Yes | Off-policy |
| Standard MADDPG in HARL / BenchMARL | Not directly | Yes | Off-policy |
| BenchMARL MASAC | Yes | Yes | Off-policy |

Sources checked 2026-10-20: [HARL algorithm scope](https://github.com/PKU-MARL/HARL#application-scope-of-algorithms) and [BenchMARL algorithm table](https://github.com/facebookresearch/BenchMARL#concept). HARL explicitly also lists MultiDiscrete support for HAPPO, HASAC and MAPPO. A finite multi-component action is not a continuous control vector. Other implementations may support fewer action types.

For each exact task, record action type/shape/bounds/masks, observation scope/history, cooperative versus competitive objectives, reward timing, agent count/heterogeneity, training versus execution information, online versus fixed-data access, and compute cost. Partial observability motivates checking memory models; it does not by itself prove an RNN is necessary. Centralized critics can use joint information while actors remain local. A centralized autoregressive joint actor has different deployment requirements.

Discrete actions select a member of a finite set; continuous actions output a real-valued control vector. Numeric or continuous observations do not determine the action type. For example, LBF can present numeric positions while its actions remain six discrete commands. NEOM's finite decimal-valued options also remain discrete.

The environment does not have an intrinsic on-policy/off-policy label. Off-policy learning with a replay buffer also does not automatically provide a sound offline-RL method for a fixed dataset.

Sable's continuous-action MASAC/HASAC experiments do not define the capabilities of every implementation of those methods. In particular, HARL HASAC has discrete and continuous branches. Keep the chosen implementation, actor and critic branches, masks, environment adapter and evaluation protocol together.

The [catalog CLI](../scripts/atlas.py) now supports candidate filtering:

```bash
python scripts/atlas.py --algorithm qmix --action discrete --explain
python scripts/atlas.py --algorithm hasac --action continuous --explain
```

These filters check the catalog's action types and exclude offline-only resources for these online training recipes. Families marked `both` require selecting the compatible task variant. Cooperative objectives, actor/critic inputs and wrappers still require manual inspection. No return or win-rate prediction is made.
