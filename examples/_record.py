"""Shared smoke-record writer. Records are runtime evidence, never training results."""
import importlib.metadata
import json
import platform
from datetime import datetime, timezone
from pathlib import Path


def save_record(path, environment_id, implementation, config, episodes, packages):
    versions = {}
    for package in packages:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = 'not installed / source checkout'
    record = dict(record_type='random_policy_smoke', environment_id=environment_id,
                  implementation=implementation, passed=True, config=config,
                  episodes=episodes, versions=versions, python=platform.python_version(),
                  platform=platform.system() + ' ' + platform.machine(),
                  timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  scope='reset/step/action-space compatibility only; no policy trained')
    text = json.dumps(record, indent=2)
    print(text)
    if path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text + '\n', encoding='utf-8')
