# Speech Lab

A modular lab for trying and comparing multiple speech engines in both directions:

- **Text to speech (TTS):** `text-to-speech/`
- **Speech to text (STT):** `speech-to-text/`

Each modality has space for provider integrations, experiments, shared helpers, and tests. Shared audio fixtures and reference transcripts live in `samples/`; project-level guidance belongs in `docs/`.

This repository is intentionally stack-neutral. See [AGENTS.md](AGENTS.md) for repository structure, safety, and contribution guidance. No providers or runtime dependencies have been selected yet.

When adding runnable scenarios, record actual measurements and comparable settings in [docs/benchmarks.md](docs/benchmarks.md). Keep generated outputs out of Git; commit only concise, reproducible result summaries.
