#!/usr/bin/env python3
"""Build Markdown indexes and CSV exports from the checked-in JSON catalog."""
import argparse
import csv
import io
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def table(headers, rows):
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join('| ' + ' | '.join(map(cell, row)) + ' |'
                     for row in [headers, ['---'] * len(headers), *rows]) + '\n'


def csv_text(headers, rows):
    f = io.StringIO(newline='')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(headers)
    writer.writerows(rows)
    return f.getvalue()


def outputs():
    envs, papers, tasks = (load(x) for x in ('environments.json', 'papers.json', 'sable_tasks.json'))
    names = {e['id']: e['name'] for e in envs}
    counts = Counter(t['environment_id'] for t in tasks)
    docs = {}
    rows = [[f"[{e['name']}](environments/{e['id']}.md)", e['kind'], e['action_space'],
             e['implementation'], ', '.join(e['tags']), e['runtime_status']] for e in envs]
    docs['docs/environment-index.md'] = (
        '# Environment and dataset index\n\n[Home](../README.md) · [中文](../README.zh-CN.md)\n\n'
        'Generated from `data/environments.json`. Each row is scoped to named implementations. '
        '`both` means the family supports discrete and continuous actions; a specific task may support only one. '
        '`unknown` is unresolved, not an assumption. Runtime labels must be read with the [verification ledger](verification.md).\n\n'
        + table(['Resource', 'Kind', 'Actions', 'Implementations', 'Research tags', 'Runtime'], rows))
    action_zh = dict(discrete='离散', continuous='连续', both='依版本可离散／连续', unknown='待核查')
    density_zh = {'sparse':'稀疏任务奖励', 'dense':'通常逐步反馈', 'mixed':'过程反馈 + 完成奖励',
                  'config-dependent':'依具体任务／奖励配置', 'dataset-dependent':'依所选离线数据', 'unknown':'待核查'}
    beginner_rows = [[f"[{e['name']}](environments/{e['id']}.md)",
        e['beginner']['agents_zh'], e['beginner']['goal_zh'], action_zh[e['action_space']],
        density_zh[e['beginner']['reward_density']]] for e in envs]
    docs['docs/environment-overview.zh-CN.md'] = (
        '# 这些环境到底是什么？\n\n[中文首页](../README.zh-CN.md) · [算法适配指南](algorithm-fit.zh-CN.md)\n\n'
        '多数条目是能反复 reset 和 step 的交互世界。每一步，各智能体读取观测、输出动作，环境返回新观测和奖励。'
        'OG-MARL 是例外：它提供固定轨迹数据。\n\n'
        '![六类环境的原理示意图，非真实环境渲染](../assets/environments-at-a-glance.svg)\n\n'
        '图中是帮助理解规则的示意画，不代表真实地图、物理尺寸、传感范围或渲染效果。'
        '具体配置及证据见各卡片。\n\n'
        + table(['环境／资源','智能体是谁','要完成什么','动作类型','奖励频率（有范围限定）'], beginner_rows)
        + '\n## 用 LBF 举例读懂一行\n\n'
        '你控制的是采集者；目标是采集食物；每个采集者每步选择 6 个命令之一。'
        '食物等级和 force_coop 决定是否必须多人一起 LOAD。坐标和等级可以编码成数字向量，'
        '这并不改变动作的离散性质。采集到食物才有任务奖励，所以它可以检验探索和合作发现。\n\n'
        '标准 QMIX 可以作为离散合作候选；MAPPO／HAPPO 可使用类别策略；HARL HASAC 也有离散分支。'
        '它们是否表现更好，还需要相同环境配置和预算下的训练评估。\n\n'
        '## 不要从环境名字推断的事\n\n'
        '- MPE 和 VMAS 是场景家族：先选具体场景、动作开关和奖励设置。\n'
        '- 与脚本敌军作战，仍可以是己方智能体之间的全合作学习。\n'
        '- on-policy／off-policy 描述算法如何使用数据，不是环境固有属性。\n'
        '- 奖励密度不是难度评分；塑形、结束条件和探索分布都能改变学习难度。\n'
        '- 接口支持、实际跑通和取得更好回报是三种不同结论。\n')
    rows = [[f"[{p['id']}](../papers/{p['id']}.md)", p['year'] or 'unresolved', p['policy'],
             p['paradigm'], ', '.join(names[x] for x in p['environments']) or 'Background only'] for p in papers]
    docs['docs/paper-index.md'] = (
        '# Paper → environment index\n\n[Home](../README.md) · [中文](../README.zh-CN.md)\n\n'
        '16 supplied papers: 15 benchmark-related mappings and one LLM-RL background paper. '
        'This is a curated starting set, not a systematic survey. Policy regimes describe the method or experiment, not the simulator. '
        'VMAS in the CAMAR paper is a simulator-speed comparison; RAC Predator and Prey remains paper-specific.\n\n'
        + table(['Paper card', 'Year', 'Policy regime', 'Training / execution', 'Environment families'], rows))
    rows = [[f"[{names[e]}](environments/{e}.md)", n] for e, n in counts.items()]
    docs['docs/sable-tasks.md'] = (
        '# Sable: the 45-task main benchmark\n\n[Paper card](../papers/sable.md) · [中文说明](sable-guide.zh-CN.md)\n\n'
        'Source: supplied Sable arXiv:2410.01706v5, Section 4 and Appendix C Table 2 (PDF p.25), with task semantics in Appendix B. '
        'Task labels below are typographically normalized paper labels, not tested environment registration strings. '
        'The printed humanoid partition is normalized as `9|8`; Connector labels retain the table form (`con-5x5x3a`).\n\n'
        + table(['Suite', 'Main tasks'], rows)
        + '\n**Total: 45.** NEOM and the extra 32/64/128-agent LBF scalability configurations are outside this table.\n\n'
        + table(['Suite', 'Paper task label', 'Actions', 'Implementation'],
                [[names[t['environment_id']], '`' + t['paper_task_label'] + '`',
                  t['action_space'], t['implementation']] for t in tasks]))
    docs['data/environments.csv'] = csv_text(
        ['id', 'name', 'kind', 'action_space', 'implementation', 'tags', 'runtime_status',
         'agents_zh', 'goal_zh', 'reward_density'],
        [[e[k] if k != 'tags' else ';'.join(e[k]) for k in
          ('id', 'name', 'kind', 'action_space', 'implementation', 'tags', 'runtime_status')]
         + [e['beginner']['agents_zh'],e['beginner']['goal_zh'],e['beginner']['reward_density']] for e in envs])
    docs['data/papers.csv'] = csv_text(
        ['id', 'title', 'year', 'policy', 'paradigm', 'environments', 'paper_url', 'code_url', 'evidence_location'],
        [[p['id'], p['title'], p['year'], p['policy'], p['paradigm'], ';'.join(p['environments']),
          p['paper_url'], p['code_url'], p['evidence_location']] for p in papers])
    docs['data/sable_tasks.csv'] = csv_text(
        ['paper_id', 'environment_id', 'paper_task_label', 'action_space', 'implementation', 'source_location'],
        [[t[k] for k in ('paper_id', 'environment_id', 'paper_task_label', 'action_space',
                         'implementation', 'source_location')] for t in tasks])
    return docs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail if generated files have drifted')
    args = parser.parse_args()
    stale = []
    for rel, content in outputs().items():
        path = ROOT / rel
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    if stale:
        parser.exit(1, 'Regenerate with python scripts/build_catalog.py:\n' + '\n'.join(stale) + '\n')
    print('Generated indexes and CSV exports are current.' if args.check else 'Built 4 indexes and 3 CSV exports.')


if __name__ == '__main__':
    main()
