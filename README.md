# Speech Lab

A modular lab for trying and comparing multiple speech engines in both directions:

- **Text to speech (TTS):** `text-to-speech/`
- **Speech to text (STT):** `speech-to-text/`

The shared [Speech Lab web interface](web-app/README.md) currently includes Kokoro for TTS and Needle / Whistle for STT. Provider implementations remain isolated so additional models can be added without creating a separate user interface for each one. Run it with `./run.sh`; use `./cleanup.sh` to remove local dependencies and optionally review model-cache cleanup.

Each modality has space for provider integrations, experiments, shared helpers, and tests. Shared audio fixtures and reference transcripts live in `samples/`; project-level guidance belongs in `docs/`. See [AGENTS.md](AGENTS.md) for repository structure, safety, and contribution guidance. Record measured runs in [docs/benchmarks.md](docs/benchmarks.md); generated outputs stay out of Git.
