# Sable 的环境到底怎么选、怎么读

[首页](../README.zh-CN.md) · [45 个主任务表](sable-tasks.md) · [论文卡片](../papers/sable.md)

依据：提供的 Sable arXiv:2410.01706v5（2025-05-26），正文第 4 节、附录 B 与附录 C 表 2。这里介绍论文实际使用的实现；它不自动代表同名环境所有版本的行为。

## 六类环境在考什么

| 环境 | 可以直观理解为 | 关键协作难点 | 论文中的实现 |
| --- | --- | --- | --- |
| RWARE | 多个仓库机器人取货送货 | 拥堵、相互阻塞、稀疏配送奖励 | Jumanji |
| LBF | 多人一起搬不同重量的食物 | 单人等级不足时需要同时协作 | Jumanji |
| Connector | 在网格里给各自的起点终点连线 | 自己留下的路径会挡住别人 | Jumanji |
| SMAX | 轻量的星际战斗协作 | 选攻击目标、走位、异质兵种配合 | JaxMARL，无 SC2 引擎 |
| MaBrax | 多人共同控制一具机器人 | 各关节动作要形成整体运动 | JaxMARL + Brax |
| MPE simple_spread | 多个粒子覆盖所有地标 | 分配地标并避免碰撞 | JaxMARL，连续动作 |

## 任务名怎么读

| 例子 | 解释 |
| --- | --- |
| `tiny-2ag-hard` | RWARE：tiny 仓库、2 个智能体、hard 请求设置 |
| `2s-8x8-2p-2f-coop` | LBF：视野参数 2、8×8 网格、2 个智能体、2 个食物、强制合作 |
| `con-10x10x10a` | Connector：10×10 网格、10 条待连接路径；采用论文表中的标签写法 |
| `3s vs 5z` | SMAX：双方单位构成；是论文标签，不保证是可直接传给库的字符串 |
| `ant 4x2` | MaBrax：4 个智能体，每个控制 2 个关节动作 |
| `simple spread 5ag` | MPE：5 个智能体、5 个地标 |

RWARE 的 hard 请求数为 N/2，默认 N，easy 为 2N，N 是智能体数；请求更少会使稀疏奖励更难获得。LBF 中 `2s` 对应以自身为中心的 5×5 视野。这些含义来自附录 B。

## 45 个任务与额外扩展实验

主性能比较为 RWARE 15、LBF 7、Connector 4、SMAX 11、MaBrax 5、MPE 3，总计 45。额外的大规模 LBF 与 NEOM 用于人数扩展性，不属于这 45 个任务。

特别注意：`smacv2 5 units`、`smacv2 10 units`、`smacv2 20 units` 在主任务表中属于 **SMAX**。名字相近不代表运行在 SMACv2 的 SC2 引擎中。

## 论文怎样评估

| 项目 | Sable 主实验协议 |
| --- | --- |
| 每个任务独立重复 | 10 次 |
| 每次训练交互预算 | 20,000,000 environment timesteps |
| 评估间隔数量 | 122 个均匀分布的评估点 |
| 每个评估点 | 32 个 episode |
| 单任务聚合 | 均值与 95% 置信区间 |
| 环境套件聚合 | min-max 归一化 IQM 与 95% 分层 bootstrap 区间 |
| 其他指标 | 适用时记录 win rate；另外记录 absolute performance |

附录分别给出 mean-over-training、maximum、final、absolute 等回报表。不能把“训练期间最高值”和“训练结束值”都叫最终性能，也不能把作者的 absolute performance 自行定义成回报绝对值。

若六类全部跑满，单个算法仅主实验就有 45×10×20M = 9B 个 environment timesteps，尚未计入调参、额外评估或扩展实验。这个乘积是预算换算，不是 GPU 小时估计。入门先选择少数任务即可。

## 哪些部分不能直接搬到自己的实验

- Sable 的跨智能体序列处理与自回归动作选择涉及集中信息。要求严格局部执行时，应单独检查 actor 的输入和动作依赖。
- 本仓库 MPE2 与原版 LBF 示例用于接口验证，不能替代 Sable 的 JaxMARL／Jumanji 配置。
- 修改 episode 长度、奖励或碰撞处理之后，应创建新的任务配置，并重新跑相同配置下的基线。

完整任务标签见 [sable_tasks.csv](../data/sable_tasks.csv)；字段说明见 [数据目录说明](../data/README.md)。
