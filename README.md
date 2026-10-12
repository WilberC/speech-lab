# Speech Lab

A modular lab for trying and comparing multiple speech engines in both directions:

- **Text to speech (TTS):** `text-to-speech/`
- **Speech to text (STT):** `speech-to-text/`

The shared [Speech Lab web interface](web-app/README.md) currently includes Kokoro for TTS and Needle / Whistle for STT. Provider implementations remain isolated so additional models can be added without creating a separate user interface for each one. Run it with `./run.sh`; use `./cleanup.sh` to remove local dependencies and optionally review model-cache cleanup.

> **Disclaimer:** Speech Lab is a personal hobby project for learning and experimentation. Its small, hand-picked test set and results are informal; they are not professional research, a statistically representative evaluation, or a basis for production decisions.

Each modality has space for provider integrations, experiments, shared helpers, and tests. Ten paired English and Spanish benchmark fixtures and their attribution live under [`samples/`](samples/README.md); project-level guidance belongs in `docs/`. See [AGENTS.md](AGENTS.md) for repository structure, safety, and contribution guidance. Record measured runs in [docs/benchmarks.md](docs/benchmarks.md); generated outputs stay out of Git.
