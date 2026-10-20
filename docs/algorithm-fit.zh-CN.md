# 看懂环境，再选择算法

[中文首页](../README.zh-CN.md) · [18 条直观介绍](environment-overview.zh-CN.md) · [English](algorithm-fit.md)

**先看动作接口能否兼容，再看观测和训练／执行条件，最后看这个任务是否适合检验你的研究问题。** 这里的表是兼容性筛选，不是算法成绩排名。

## 离散和连续到底看什么

- **离散动作**：从有限个命令里选一个。例如 LBF 的停止、上、下、左、右、LOAD，actor 可以输出 6 个动作的概率。
- **连续动作**：输出实数控制向量。例如关节力矩 `[0.13, -0.47]`；数值可在允许范围内连续变化，维度和边界由任务决定。
- **MultiDiscrete**：同时选择多个离散分量，例如移动方向与通信符号。它不等于连续向量；也不保证所有只接受一个 `Discrete` 的实现都能直接处理。
- **观测类型另算**：LBF 的坐标、等级可编码成数字向量，动作仍然是离散的。SMAC 的位置是实数，也不意味着算法要输出连续动作。
- **小数不代表连续**：NEOM 若只能从 `{0.2, 0.3, 0.5, 0.7, 0.8}` 中选，仍然是有限集合上的离散动作。

## 最有用的八项属性

| 属性 | 应记录什么 | 为什么影响算法选择 |
| --- | --- | --- |
| 动作类型、维度和边界 | Discrete(n)、MultiDiscrete(nvec)、Box(shape, low, high) | 先决定策略头和 Q 网络是否能处理该接口 |
| 观测范围与历史 | 全局／局部视野，单帧／历史，向量／图像 | 局部单帧不一定足够；可比较循环网络或记忆模型，不能直接假定必须 RNN |
| 合作关系与奖励归属 | 全合作／竞争／混合；团队奖励还是个人奖励 | 标准 QMIX／VDN 的合作目标不能原样替代任意竞争博弈目标 |
| 奖励频率与延迟 | 仅成功有奖，还是距离／伤害等逐步反馈 | 稀疏奖励更适合检验探索与协作发现；不据此保证某算法效果好 |
| 智能体数量与异质性 | 人数是否变化；观测、动作维度和能力是否相同 | 检查共享网络、padding／mask、分组或独立网络能否处理 |
| 训练与执行信息 | critic 能否看到联合信息；actor 部署时能看到什么 | CTDE 与严格分散执行要分开检查；集中 critic 不等于集中 actor |
| 数据采集条件 | 能否在线互动；只有固定历史数据吗 | on-policy／off-policy 是算法用数据的方式；off-policy 不自动等于离线 RL |
| 交互与计算成本 | 单步成本、并行能力、训练步数、编译和显存 | 决定预算是否可承受；JAX／GPU 速度需在同一硬件和工作负载下测量 |

这是**结构属性**。回报、胜率、成功率、碰撞率、样本效率和泛化落差是**运行后测量的结果**；不能用一个无依据的“适配分数”把两者混在一起。

## 常见算法可以处理哪些动作

| 算法／本文指的实现 | 离散 | 连续 | 数据方式 | 需要特别核对 |
| --- | --- | --- | --- | --- |
| 标准 QMIX／VDN | 是 | 不能直接用 | off-policy | 合作团队目标、动作枚举、mask；连续扩展不在本表内 |
| MAPPO | 是 | 是 | on-policy | Categorical／Gaussian 策略头、critic 与 actor 输入 |
| HARL HAPPO | 是 | 是 | on-policy | 环境 wrapper、顺序更新、异质接口 |
| HARL HASAC | 是 | 是 | off-policy | 离散与连续分支不同；确认 replay、actor、critic 和 mask 一致 |
| 标准 MADDPG | 不能直接用 | 是 | off-policy | 本表指常见连续实现；离散扩展需另外说明 |
| BenchMARL MASAC | 是 | 是 | off-policy | 使用相应动作类型的实现；不能照搬连续 SAC 分支 |

依据：[HARL 的 Application Scope of Algorithms](https://github.com/PKU-MARL/HARL#application-scope-of-algorithms)、[BenchMARL 的算法兼容表](https://github.com/facebookresearch/BenchMARL#concept)。核对日期：2026-10-20。具体安装版本和 wrapper 仍需验证。**原先 Sable 表里的 MASAC／HASAC 连续实验范围，不是这些算法所有实现的理论限制。**

“支持两类”不代表同一组网络输出和超参数直接复用，也不代表已经在本仓库训练验证。

## 用六个环境练习选择

| 环境／版本 | 动作 | 可以先比较的基线 | 这个任务在考什么 |
| --- | --- | --- | --- |
| LBF 合作采集 | 离散，6 个命令 | MAPPO、HAPPO、QMIX；也可用适配后的 HARL 离散 HASAC | 是否学会共同采集；稀疏任务奖励与协作时机 |
| RWARE 配送 | 离散，5 个命令 | MAPPO、HAPPO、合作目标下的 QMIX | 配送、拥堵、稀疏奖励 |
| Connector 的 Sable 配置 | 离散，5 个命令 | MAPPO、HAPPO、合作目标下的 QMIX | 避免自己的路径挡住别人 |
| SMAX 战斗小队 | 离散，含攻击目标 | MAPPO、HAPPO、QMIX | 集火、走位、单位配合与可用动作 |
| MaBrax 关节控制 | 连续，按关节分组 | MAPPO、HAPPO、HASAC、MADDPG 的连续实现 | 多个控制器形成稳定整体运动 |
| MPE2 simple_spread | 离散或连续，由 continuous_actions 指定 | 两类均可用 MAPPO／HAPPO／HARL HASAC；QMIX 选离散版、MADDPG 选连续版 | 地标分工、距离与碰撞 |

这只是第一步候选。比如在 MPE 中选择 QMIX，还需把具体场景设为合作目标，确定共享奖励与集中混合网络的输入；仅仅把 `continuous_actions=False` 设好并不充分。

## 如何判断是否适合研究同伴学习或泛化

先确定可独立变化的情境：食物等级、队友策略、初始位置、人数或通信条件。再把训练与测试分布分开，保留不迁移对照和相同总预算。环境动作兼容只回答“能不能运行”；不能替代这些实验设计。

## 直接从配置检查

MPE2 Parallel API（先 `reset`，选一个智能体）通常读取 `env.action_space(agent)` 和 `env.observation_space(agent)`；LBF 的 Gymnasium 接口通常读取 `env.action_space` 和 `env.observation_space`；SMAC 需读取 `get_env_info()` 与每个 agent 的可用动作。

具体数值以[本仓库运行记录](verification.md)和你自己安装的版本为准。不要只靠环境名字或论文画面判断离散／连续。
