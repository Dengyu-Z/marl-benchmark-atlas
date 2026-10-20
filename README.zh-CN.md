<p align="center">
  <img src="assets/banner.svg" width="100%" alt="MARL Benchmark Atlas 多智能体强化学习环境与基准指南" />
</p>

<h1 align="center">多智能体强化学习环境与基准指南</h1>

<p align="center">
  选环境 · 找论文配置 · 查版本差异 · 从最小示例开始<br />
  <a href="README.md">English</a> ·
  <a href="docs/environment-index.md">环境总表</a> ·
  <a href="docs/paper-index.md">论文索引</a> ·
  <a href="docs/sable-guide.zh-CN.md">Sable 环境详解</a>
</p>

**这个仓库帮助你回答三个问题：我的研究适合什么环境？论文具体用了哪个版本？怎样开始一个可比较的实验？**

首版以 Sable 的六类环境为入口，收录 **18 条环境／数据资源记录、16 篇论文卡片，以及 Sable 的 45 个主实验任务**。每条内容都有来源或明确的待核查标记。

这里区分三类对象：在线交互环境、论文自定义任务、固定轨迹的离线数据。它们不能统一当作“数据集”来比较。

## 快速导航

| 你现在想做什么 | 对应入口 |
| --- | --- |
| 根据研究问题选环境 | [中文选型指南](docs/selection-guide.zh-CN.md) |
| 浏览环境、动作空间和实现 | [环境与数据资源总表](docs/environment-index.md) |
| 查看一篇论文用了什么环境 | [论文—环境—训练方式索引](docs/paper-index.md) |
| 看懂 Sable 的环境和任务名 | [中文详解](docs/sable-guide.zh-CN.md) / [45 个任务完整表](docs/sable-tasks.md) |
| 先跑一个小例子 | [MPE2 / LBF / SMACv2 示例](examples/README.md) |
| 确认哪些已经实际运行 | [验证记录](docs/verification.md) |
| 避免做出无法比较的结果 | [版本与协议差异](docs/comparability.md) |

## Sable 的六类主实验环境

| 环境 | 任务数 | 论文动作空间 | 主要研究对象 |
| --- | ---: | --- | --- |
| [RWARE](docs/environments/rware.md) | 15 | 离散 | 仓储搬运、稀疏奖励、拥堵与避碰 |
| [LBF](docs/environments/lbf.md) | 7 | 离散 | 等级配合、协同采集食物 |
| [Connector](docs/environments/connector.md) | 4 | 离散 | 路径连接、空间冲突与相互阻塞 |
| [SMAX](docs/environments/smax.md) | 11 | 离散 | 战斗配合与异质单位 |
| [MaBrax](docs/environments/mabrax.md) | 5 | 连续 | 多智能体共同控制机器人关节 |
| [MPE simple_spread](docs/environments/mpe.md) | 3 | 连续 | 3／5／10 个智能体覆盖地标并避碰 |

合计 **45 个主实验任务**。NEOM 和大规模 LBF 是额外的扩展性实验，单独记录。来源为 Sable v5 第 4 节、附录 B 与附录 C 表 2。

## 几个会直接影响结论的细节

1. **SMAX ≠ SMAC ≠ SMACv2。** Sable 任务名中的 `smacv2 ... units` 仍然属于 SMAX，不能和 SC2 引擎上的 SMACv2 混为一谈。
2. **同名环境可能有不同的碰撞与结束规则。** Sable 明确描述其 Jumanji RWARE 在碰撞时结束 episode，原版 RWARE 的处理不同。
3. **MPE 动作空间不能靠名字猜。** Sable 用连续动作；本仓库的入门例子采用 MPE2，可分别选择离散和连续动作，接口与 Sable 配置并不等价。
4. **MaBrax 与 MA-MuJoCo 的物理引擎不同。** 机器人关节划分相同，也不能直接沿用参考分数。
5. **策略熵不是协作多样性的充分指标。** 多样性研究还需行为、角色、覆盖或 SND 等与问题对应的指标。

## 无需安装训练框架即可查询

Python 3.10+，查询工具仅使用标准库：

```bash
git clone https://github.com/Dengyu-Z/marl-benchmark-atlas.git
cd marl-benchmark-atlas
python scripts/atlas.py --paper sable
python scripts/atlas.py --tag sparse-reward --action discrete
python scripts/atlas.py --kind offline-dataset --json
python scripts/validate_catalog.py
```

`--paper sable` 会列出 Sable 关联的全部资源，包括额外的 NEOM；只看主实验的 45 个任务请使用 [任务表](docs/sable-tasks.md)。JSON 与 CSV 可直接用于你自己的筛选工具。

## 跑通第一个环境

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements/smoke.txt
python examples/mpe_smoke.py --output runs/mpe.json
python examples/mpe_smoke.py --continuous --output runs/mpe-continuous.json
python examples/lbf_smoke.py --output runs/lbf.json
```

首版已实际验证 **MPE2 离散动作、MPE2 连续动作、原版 LBF**，每种配置使用随机策略运行 2 个 episode。记录包含版本和配置，见[验证页](docs/verification.md)。SMACv2 提供待验证示例，需要额外安装 SC2 与地图。

**随机动作能运行，只说明接口可用。** 它不代表算法复现成功，也不代表得到了论文中的回报。本仓库没有虚构训练曲线、性能提升或硬件耗时。

## 按什么标准持续维护

- 文献核对：提供原文节号、表号或页码。
- 接口验证：提供 reset/step 运行记录、版本和配置。
- 基线复现：还需完整训练日志、预算、独立训练种子与统计结果。

欢迎补充环境卡片、论文配置、安装经验和运行记录。请从 [贡献指南](CONTRIBUTING.md) 和 [路线图](ROADMAP.md) 开始。原始整理和工具代码采用 [MIT](LICENSE) 协议；论文、第三方代码与数据遵循各自协议。
