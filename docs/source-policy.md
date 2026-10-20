# Sources and scope

[Home](../README.md) · [Source manifest](../data/source_manifest.json)

The first edition was assembled from 16 supplied PDFs and the official project/documentation pages linked in each card. It is a curated starting set, not an exhaustive literature search. The extraction date is **2026-10-20**.

## Evidence rules

- Paper-specific settings come from the supplied paper, with a section/table/page locator.
- Current installation/API links come from official repositories or documentation. A moving upstream branch is not a paper-pinned revision.
- A metadata label describes the supplied version or a primary record checked for this edition. No ongoing claim about the latest publication status is implied.
- Missing code URLs, budgets, seed IDs and unresolved implementations are left explicit. We do not generate repository names from paper titles.
- Editorial recommendations are labeled as recommendations. They are not reported experimental results.
- A paper label is not automatically a valid `make(...)` string or map filename.

## Public provenance

The source manifest records each supplied file's name, SHA-256 and evidence locator. The PDFs themselves are not distributed. Public links are provided when verified; some cards use the author repository as the available primary record. Original environment and paper authors retain credit and ownership.

## What is incomplete

This edition transcribes the complete Sable main task labels and main evaluation protocol. The other papers have checked environment-family mappings and selected important settings, but not a complete transcription of every hyperparameter or task. The Wildfire local action space, RAC Predator and Prey implementation identity, several paper code links and the open-credit publication year/venue remain unresolved.

The optional SMACv2 example has been checked against the official API example but has not been executed here. The exact source commits for paper-pinned Mava/Jumanji/JaxMARL experiments remain to be locked. Consult the [roadmap](../ROADMAP.md) before treating this as a complete reproduction suite.
