# Speech Lab web interface

One local Gradio interface exposes the currently integrated TTS and STT labs. Provider-specific processing remains isolated in `providers/`; the UI owns shared interaction and dispatch.

## Included providers

- **TTS — Kokoro:** general Latin American Spanish (`ef_dora`, `em_alex`, `em_santa`) and US English (`af_heart`, `af_bella`, `am_michael`), speed 1, 24 kHz output. Spanish voices are not specifically trained for Peruvian Spanish. Listen to samples from the [original Kokoro model](https://huggingface.co/hexgrad/Kokoro-82M) before choosing.
- **STT — Needle / Whistle:** local transcription via `needle.transcribe`. This lab exposes only English and Spanish and passes the selected language to Whistle; the package's other supported languages are intentionally not offered. Non-WAV uploads and recordings are converted to WAV, then resampled to 16 kHz mono. Audio longer than 30 seconds is windowed.

Both providers run on the local machine. The first inference may download model assets; generated audio is not a repository fixture. Use only synthetic, licensed, or explicitly authorized recordings.

## Requirements

- Python 3.10 or newer.
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) to install and manage Python dependencies.
- **FFmpeg is required for the speech-to-text audio workflow.** Install it before running the app; it is used to normalize uploaded and recorded audio, especially non-WAV files. Verify the installation with `ffmpeg -version`.
- `espeak-ng` is needed only when using the Kokoro text-to-speech provider.

## Setup (Ubuntu)

The project uses **uv** for dependency management and commits `uv.lock` so the shared UI and provider resolutions are reproducible. Install uv using its [official instructions](https://docs.astral.sh/uv/getting-started/installation/). Provider dependencies are optional extras, so you do not need to install every model runtime.

```sh
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
# Required for non-WAV uploads and recordings in the STT interface:
sudo apt install -y ffmpeg
# Kokoro requires espeak-ng (skip this if using only Needle / Whistle):
sudo apt install -y espeak-ng

cd web-app
uv sync --extra kokoro --extra needle
```

FFmpeg decodes non-WAV STT uploads and recordings. The Needle extra includes `soxr` for resampling and mono conversion before transcription.

To install only the shared UI and one provider, use `uv sync --extra kokoro` or `uv sync --extra needle`. For just the shared UI, run `uv sync`. These commands create and manage the local `.venv`.

Kokoro's extra includes PyTorch, and uv installs the version resolved in `uv.lock`. Check CUDA with `uv run python -c 'import torch; print(torch.cuda.is_available())'`. Kokoro selects CUDA when PyTorch detects it and otherwise runs on CPU. If the locked build does not support the host GPU, use the [official PyTorch selector](https://pytorch.org/get-started/locally/) to choose a compatible build, then update the project's dependency configuration and lockfile rather than making an untracked one-off install.

## Run

From the repository root, start the full lab with one command. The Gradio
development runner watches the app for changes and reloads it automatically:

```sh
./run.sh
```

The script synchronizes both provider extras, then starts the app. It uses `mise exec -- uv` when mise is available and falls back to `uv` on `PATH`. To install just one provider, follow the `uv sync --extra ...` setup above and run `uv run python app.py` from this directory instead.

Open the local Gradio URL (typically `http://127.0.0.1:7860`). Choose the **Text to speech** or **Speech to text** tab. The UI reports which optional package to install if a selected provider is missing.

## Interface development

`ui.py` defines the cream/coral theme and responsive layout. It uses native Gradio
theme tokens, with matching light and dark token values so system preferences
cannot introduce dark components. `app.py` passes the theme and CSS to `launch()`
(the Gradio 6 API). The development runner watches both Python files.

The input and result panels sit side by side on desktop and stack on mobile.
Runtime errors appear in a compact, scrollable alert with a button to copy the
full error details.
Theme integration checks do not run inference or download models:

```sh
cd web-app
mise exec -- uv run python -m unittest discover -s tests -v
```

## Cleanup

From the repository root, `./cleanup.sh` removes the web app's `.venv` and its installed dependencies. Run `./cleanup.sh --prune-uv-cache` to also ask uv to prune globally cached files that are no longer needed; this can make future installs download packages again.

Model assets are downloaded on first inference, not by `run.sh`. To review and optionally remove their shared cache directories, run `./cleanup.sh --models`; the script asks before deleting them. This includes the Hugging Face entries for Kokoro and Whistle, plus Needle's cached v3 engine used by Whistle. Other projects may use these same caches and need to download them again. A custom file set with `NEEDLE_WHISTLE_WEIGHTS` is not removed.
