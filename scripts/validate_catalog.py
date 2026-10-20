#!/usr/bin/env python3
"""Check catalog relationships, source provenance and local Markdown links."""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    def load(name):
        return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    envs, papers, tasks, sources = (load(x) for x in (
        'environments.json', 'papers.json', 'sable_tasks.json', 'source_manifest.json'))
    eids, pids = {e['id'] for e in envs}, {p['id'] for p in papers}
    require(len(eids) == len(envs), 'Duplicate environment id')
    require(len(pids) == len(papers), 'Duplicate paper id')
    algorithms = load('algorithms.json')
    require(len({a['id'] for a in algorithms}) == len(algorithms), 'Duplicate algorithm id')
    for a in algorithms:
        require(bool(a['actions']) and set(a['actions']) <= {'discrete','continuous'}, 'Invalid algorithm action list: ' + a['id'])
        require(bool(a['scope']) and a['source'].startswith('https://'), 'Missing implementation scope/source: ' + a['id'])
    require({s['paper_id'] for s in sources} == pids, 'Source manifest must cover every paper')
    for s in sources:
        require(bool(re.fullmatch(r'[0-9a-f]{64}', s['sha256'])), 'Invalid source hash: ' + s['paper_id'])
    for e in envs:
        require(e['action_space'] in {'discrete', 'continuous', 'both', 'unknown'}, 'Invalid action type: ' + e['id'])
        require(e['kind'] in {'online', 'offline-dataset', 'paper-specific'}, 'Invalid resource type: ' + e['id'])
        require(e['runtime_status'] in {'not_run', 'smoke_passed', 'baseline_reproduced'}, 'Invalid runtime state: ' + e['id'])
        require(e['evidence_status'] == 'literature_checked', 'Missing evidence label: ' + e['id'])
        b=e.get('beginner',{})
        require(all(isinstance(b.get(k),str) and b[k] for k in (
            'agents_zh','goal_zh','action_example_zh','action_scope_zh','scope_zh','baseline_candidates_zh')),
            'Missing plain-language explanation: ' + e['id'])
        require(b.get('reward_density') in {'sparse','dense','mixed','config-dependent','dataset-dependent','unknown'},
                'Invalid reward-density scope: ' + e['id'])
        require((ROOT / e['card']).is_file(), 'Missing environment card: ' + e['id'])
        require(set(e['papers']) <= pids, 'Unknown paper: ' + e['id'])
        for p in papers:
            require((p['id'] in e['papers']) == (e['id'] in p['environments']), 'Non-reciprocal mapping: ' + e['id'] + '/' + p['id'])
    for p in papers:
        require(set(p['environments']) <= eids, 'Unknown environment: ' + p['id'])
        require(bool(p['evidence_location']), 'Missing evidence locator: ' + p['id'])
        require((ROOT / 'papers' / (p['id'] + '.md')).is_file(), 'Missing paper card: ' + p['id'])
    expected = dict(rware=15, lbf=7, connector=4, smax=11, mabrax=5, mpe=3)
    require(Counter(t['environment_id'] for t in tasks) == expected, 'Sable suite/task count mismatch')
    require(len(tasks) == 45, 'Expected 45 Sable main tasks')
    require(len({(t['environment_id'],t['paper_task_label']) for t in tasks}) == len(tasks), 'Duplicate Sable task label')
    for t in tasks:
        require(t['paper_id'] == 'sable' and t['environment_id'] in eids, 'Invalid Sable task reference')
    # Resolve file targets, including images. GitHub-rendered heading anchors are not checked here.
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            target = target.split(' "', 1)[0]
            if re.match(r'^(https?://|mailto:|#)', target):
                continue
            rel = unquote(target.split('#', 1)[0])
            require((path.parent / rel).exists(), f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    ledger = load('validation.json')
    runs = ledger['environment_runs']
    for e in envs:
        if e['runtime_status'] != 'not_run':
            require(any(r.get('environment_id') == e['id'] and r.get('passed') is True
                        and r.get('record_path') and (ROOT/r['record_path']).is_file() for r in runs),
                    'Runtime claim lacks a checked-in evidence record: ' + e['id'])
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'PASS: {len(envs)} resource cards; {len(papers)} papers; 45 Sable tasks; mappings, hashes and local links.')


if __name__ == '__main__':
    main()
