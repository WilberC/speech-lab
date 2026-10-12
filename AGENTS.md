# Speech Lab — Agent Guide

## Project purpose

Speech Lab is an experimental workspace for exploring, integrating, and comparing multiple text-to-speech (TTS) and speech-to-text (STT) engines. It is a lab, not a single production application: experiments should be easy to run, compare, and remove without coupling unrelated providers.

## Repository layout

- `text-to-speech/`: text-to-audio work. Keep provider integrations in `providers/`, runnable prototypes and comparisons in `experiments/`, modality-specific reusable helpers in `shared/`, and checks in `tests/`.
- `speech-to-text/`: audio-to-text work, organized using the same conventions as TTS.
- `samples/audio/`: small, non-sensitive audio fixtures used by experiments and tests.
- `samples/transcripts/`: reference transcripts and evaluation labels for sample audio.
- `docs/`: project-level notes, setup guidance, evaluation methodology, and decisions.

## Directions for contributors and coding agents

1. Keep TTS and STT implementations in their respective top-level directories; put genuinely cross-cutting material at the repository root or under `docs/`.
2. Keep each provider integration isolated under its own directory. Prefer explicit provider-specific experiments over abstractions that assume every engine has the same capabilities.
3. Record how to configure and run each experiment in its directory README (or equivalent documentation). Never commit API keys, credentials, private recordings, or other secrets.
4. Use only synthetic, licensed, or explicitly authorized audio. Do not add personal or sensitive recordings to samples.
5. Keep sample files small and suitable for version control. Document provenance, license, language, and expected transcript where relevant; use an external artifact store for large datasets.
6. Compare systems with reproducible inputs and state the relevant settings (such as language, voice, model, and decoding options). Avoid presenting results from unlike inputs as directly comparable.
7. Do not choose a shared programming language, framework, or dependency manager prematurely. Introduce tooling when an experiment needs it, and document the choice and setup.
8. Add tests for stable reusable behavior; exploratory work may remain a standalone experiment, but it should clearly state its purpose and how to run it.
9. Update this guide when the repository structure or contribution conventions materially change.
10. Every runnable scenario must document its input, language, provider/model, relevant settings, and how to run it. When adding or changing a scenario, run it and record the measured result in `docs/benchmarks.md` when execution is possible; label unrun scenarios as pending rather than inventing results.
11. Keep comparisons reproducible: compare the same input and equivalent settings, record the date and number of runs, and report elapsed time (plus a useful modality-specific measure such as real-time factor when available). Record quality/cost metrics only when measured, and note meaningful limitations.

## Security and generated artifacts

12. Never stage or commit `.env` files, credentials, API keys, access tokens, or private recordings. Keep local secrets in the configured external secret store; use a sanitized `.env.example` only when documenting required variable names.
13. Keep generated audio, exports, raw outputs, and bulky run artifacts out of Git by default. Store only small, explicitly authorized fixtures and reference transcripts under `samples/`; review provenance and licensing before adding them. Keep concise measured summaries and comparison tables in `docs/benchmarks.md`.
14. Before committing or pushing, inspect the staged file list and diff for secrets and generated artifacts. Do not assume `.gitignore` protects files that are already tracked.
