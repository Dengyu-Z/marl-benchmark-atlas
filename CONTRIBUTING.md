# Contributing

The most useful addition is a claim someone else can verify: an exact task setting, a meaningful version difference, or a runnable example with evidence.

1. Start from an [environment template](templates/environment-card.md) or a [reproduction record](templates/reproduction-record.json).
2. Cite an official source or a paper section/table/page. Describe exactly which implementation and configuration you mean.
3. Update canonical JSON and the matching curated card. Preserve stable IDs and distinguish null/unresolved fields from negative findings.
4. Run the catalog checks below and include the relevant output in your pull request.

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
python scripts/build_catalog.py --check
```

For runtime claims, attach a versioned record. A reset/step check can earn `smoke_passed`; it cannot earn `baseline_reproduced`. Training results need budgets, independent training seeds, evaluation definitions, raw logs and a named reference configuration.

Use original prose. Link papers, datasets and upstream projects instead of uploading third-party PDFs, game binaries, datasets or checkpoints. Please keep hardware timing labeled as either a paper-reported value or a measured local result.

Chinese and English improvements are welcome. A new entry can start in either language with the factual JSON and source locators kept consistent.
