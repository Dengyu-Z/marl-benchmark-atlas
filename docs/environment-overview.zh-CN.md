# 这些环境到底是什么？

[中文首页](../README.zh-CN.md) · [算法适配指南](algorithm-fit.zh-CN.md)

多数条目是能反复 reset 和 step 的交互世界。每一步，各智能体读取观测、输出动作，环境返回新观测和奖励。OG-MARL 是例外：它提供固定轨迹数据。

![六类环境的原理示意图，非真实环境渲染](../assets/environments-at-a-glance.svg)

图中是帮助理解规则的示意画，不代表真实地图、物理尺寸、传感范围或渲染效果。具体配置及证据见各卡片。

| 环境／资源 | 智能体是谁 | 要完成什么 | 动作类型 | 奖励频率（有范围限定） |
| --- | --- | --- | --- | --- |
| [RWARE / Robot Warehouse](environments/rware.md) | 搬货机器人 | 在仓库里取出指定货架，送到配送口，再继续取货。 | 离散 | 稀疏任务奖励 |
| [Level-Based Foraging](environments/lbf.md) | 有不同等级的采集者 | 在网格里找食物；单人搬不动时，多人靠近并共同 LOAD。 | 离散 | 稀疏任务奖励 |
| [Connector](environments/connector.md) | 各自画一条线的路径头 | 从各自起点连到各自终点；已经画过的线会挡住其他路径。 | 离散 | 过程反馈 + 完成奖励 |
| [SMAX](environments/smax.md) | 战斗小队中的己方单位 | 配合走位、集火和攻击时机，击败敌方队伍。 | 离散 | 过程反馈 + 完成奖励 |
| [MaBrax](environments/mabrax.md) | 同一个机器人不同关节的控制器 | 多个控制器共同让机器人前进，并控制能耗与姿态。 | 连续 | 通常逐步反馈 |
| [MPE / MPE2](environments/mpe.md) | 二维平面上移动的小圆点 | 以 simple_spread 为例：分工覆盖所有地标，同时减少相互碰撞。 | 依版本可离散／连续 | 通常逐步反馈 |
| [SMAC](environments/smac.md) | SC2 游戏引擎中的己方作战单位 | 协同击败内置 AI 控制的敌军；训练的是己方团队。 | 离散 | 依具体任务／奖励配置 |
| [SMACv2](environments/smacv2.md) | 随机生成队伍中的己方作战单位 | 在随机单位构成和初始位置下击败敌队，学习更稳健的配合。 | 离散 | 依具体任务／奖励配置 |
| [Multi-Agent MuJoCo](environments/mamujoco.md) | MuJoCo 机器人各部分的控制器 | 共同控制一个机器人运动；例如不同智能体控制不同腿或关节组。 | 连续 | 通常逐步反馈 |
| [VMAS](environments/vmas.md) | 二维模拟器里的机器人或移动实体 | 不是一个固定游戏；任务可以是导航、搬运、协作覆盖或竞争。 | 依版本可离散／连续 | 依具体任务／奖励配置 |
| [Google Research Football](environments/grf.md) | 足球场上由算法控制的球员 | 通过跑位、传球、配合和射门，在指定足球场景中完成目标。 | 离散 | 依具体任务／奖励配置 |
| [Overcooked](environments/overcooked.md) | 合作厨房里的两名厨师 | 分工拿食材、做汤、装盘和送餐，减少互相挡路。 | 离散 | 依具体任务／奖励配置 |
| [CAMAR](environments/camar.md) | 要穿过障碍到达终点的移动机器人 | 让多个机器人分别到达目标，同时控制碰撞、路径和耗时。 | 连续 | 依具体任务／奖励配置 |
| [Didactic coordination games](environments/coordination-games.md) | 选择数字或小博弈动作的决策者 | 通过联合动作获得高收益，用可控例子分析协调失败。 | 依版本可离散／连续 | 依具体任务／奖励配置 |
| [Open-system Wildfire](environments/open-wildfire.md) | 野火管理场景中的协作智能体 | 应对火情，同时处理智能体加入／离开或任务变化。 | 待核查 | 待核查 |
| [SUMO-RL traffic signals](environments/sumo-rl.md) | 道路网络中控制信号灯的路口控制器 | 调节交通灯，让网络里的排队和等待下降。 | 离散 | 依具体任务／奖励配置 |
| [OG-MARL](environments/og-marl.md) | 已经记录好的多智能体轨迹中的行为主体 | 用已有轨迹学习新策略；训练时未必允许重新向环境采样。 | 依版本可离散／连续 | 依所选离线数据 |
| [NEOM (Sable scalability task)](environments/neom.md) | 共同拼出一维数值图案的位置／决策者 | 让所有人的离散选择拼成指定的周期图案，用于人数扩展实验。 | 离散 | 过程反馈 + 完成奖励 |

## 用 LBF 举例读懂一行

你控制的是采集者；目标是采集食物；每个采集者每步选择 6 个命令之一。食物等级和 force_coop 决定是否必须多人一起 LOAD。坐标和等级可以编码成数字向量，这并不改变动作的离散性质。采集到食物才有任务奖励，所以它可以检验探索和合作发现。

标准 QMIX 可以作为离散合作候选；MAPPO／HAPPO 可使用类别策略；HARL HASAC 也有离散分支。它们是否表现更好，还需要相同环境配置和预算下的训练评估。

## 不要从环境名字推断的事

- MPE 和 VMAS 是场景家族：先选具体场景、动作开关和奖励设置。
- 与脚本敌军作战，仍可以是己方智能体之间的全合作学习。
- on-policy／off-policy 描述算法如何使用数据，不是环境固有属性。
- 奖励密度不是难度评分；塑形、结束条件和探索分布都能改变学习难度。
- 接口支持、实际跑通和取得更好回报是三种不同结论。
