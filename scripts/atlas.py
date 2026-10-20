#!/usr/bin/env python3
"""Query the atlas offline. Uses only the Python standard library."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--action', choices=['discrete', 'continuous', 'both', 'unknown'])
    parser.add_argument('--kind', choices=['online', 'offline-dataset', 'paper-specific'])
    parser.add_argument('--tag', action='append', default=[], help='repeat for AND matching')
    parser.add_argument('--paper', help='paper id, e.g. sable, r3dm, optimappo')
    parser.add_argument('--search', default='', help='case-insensitive full-record search')
    parser.add_argument('--json', action='store_true', help='emit machine-readable records')
    args = parser.parse_args()
    records = json.loads((ROOT / 'data/environments.json').read_text(encoding='utf-8'))
    papers = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    if args.paper and args.paper not in {p['id'] for p in papers}:
        parser.error('Unknown paper id; see docs/paper-index.md.')
    selected = [e for e in records
                if (not args.action or e['action_space'] == args.action
                    or (args.action in ('discrete', 'continuous') and e['action_space'] == 'both'))
                and (not args.kind or e['kind'] == args.kind)
                and all(t in e['tags'] for t in args.tag)
                and (not args.paper or args.paper in e['papers'])
                and args.search.lower() in json.dumps(e, ensure_ascii=False).lower()]
    if args.json:
        print(json.dumps(selected, indent=2, ensure_ascii=False))
    else:
        print(f'{len(selected)} matching resources')
        for e in selected:
            print(f"  {e['id']:<20} {e['name']} [{e['action_space']}; {e['kind']}]")
            print(f"    {e['card']}")


if __name__ == '__main__':
    main()
