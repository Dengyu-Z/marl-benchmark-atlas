# 从研究问题出发选环境

[首页](../README.zh-CN.md) · [完整环境表](environment-index.md)

以下是选型建议，不是实测难度或耗时排名。环境支持某种配置，不等于你已经设计好了泛化实验。

| 研究问题 | 优先考虑 | 必须明确的变量 |
| --- | --- | --- |
| 稀疏奖励下如何形成合作 | [LBF](environments/lbf.md)、[RWARE](environments/rware.md)、稀疏奖励 [GRF](environments/grf.md) | 是否强制合作、奖励塑形、结束条件、成功定义 |
| 角色分工与行为多样性 | [SMACv2](environments/smacv2.md)、[VMAS](environments/vmas.md)、[Overcooked](environments/overcooked.md) | 异质性、参数共享、行为或角色指标，不能只看策略熵 |
| 消息丢失是否破坏协作 | 有通信动作的 [MPE](environments/mpe.md) 场景 | 通信通道、拓扑、丢包／噪声过程，训练与测试通信条件 |
| 选择性同伴学习是否有效 | MPE、LBF、Overcooked | 教师冻结、学生适应预算、情境与队友划分、no-transfer 对照 |
| 是否真的发生相对过度泛化 | [可控小博弈](environments/coordination-games.md)、MMQ／OptiMAPPO 的具体任务 | 已知最优联合动作、单独行动惩罚、奖励表 |
| 图结构能否改善信用分配 | [SUMO-RL](environments/sumo-rl.md)、图耦合小博弈 | 每个 agent 的奖励、真实耦合图、advantage 和 ratio 的聚合范围 |
| 人数变化后的泛化 | SMACv2、VMAS、修改后的 MPE | 未见人数、观测与 actor 接口、零样本测试或重新训练 |
| 大规模吞吐与显存 | SMAX、Jumanji、[NEOM](environments/neom.md)、[CAMAR](environments/camar.md) | 编译与稳态运行分开，区分环境吞吐和端到端训练吞吐 |
| 连续控制中的协作 | [MaBrax](environments/mabrax.md)、[MA-MuJoCo](environments/mamujoco.md)、CAMAR | 物理引擎、关节划分、动作维度、奖励项 |
| 安全约束与扩展性 | SS-MARL 的修改版 MPE、含碰撞的连续规划 | 独立 cost、阈值、障碍分布；仅减小碰撞惩罚不等于约束满足 |
| 固定数据上的离线学习 | [OG-MARL](environments/og-marl.md) | 数据质量、行为覆盖、数据版本、是否额外在线交互 |
| 智能体进出与任务变化 | [Open Wildfire](environments/open-wildfire.md) | 进入／离开规则、变化时间、封闭系统对照 |

研究同伴迁移时，可以先在 MPE 或 LBF 固定一个小配置，比较不迁移、直接迁移、选择性迁移，并保留独立的能力保持测试。这个方案是实验建议，不是环境原生自带的评测协议。

一条可靠的结果链是：**机制诊断 → 一个确切环境的公平比较 → 多任务与独立种子验证**。不要把不同奖励、不同动作空间和不同仿真版本的分数直接拼在同一张排名表。
