# Benchmark notes

Use this small log to keep measured comparisons with the repository. Keep audio, model output, and other generated artifacts out of Git; link only to stable sample IDs or external artifact locations when needed.

## Scope and disclaimer

Speech Lab is a personal hobby lab for learning and experimentation, not professional research. Benchmark results are informal and exploratory. A small sample set is not statistically representative, and results should not be treated as scientific conclusions, general model rankings, or production recommendations.

The starter set contains five short, fixed clips each for US English (`en_us`) and Latin American Spanish (`es_419`), with reference transcripts, selected from the test splits of [Google's FLEURS-R dataset](https://huggingface.co/datasets/google/fleurs-r), licensed CC BY 4.0. Only these ten clips are stored under `samples/`; the full corpus is not included. See [sample provenance and attribution](../samples/README.md). Use the same transcripts as fixed TTS prompts and their paired clips as STT inputs. The app intentionally supports only English and Spanish. This tiny set supports repeatable hobby experiments, not statistically robust conclusions. No inference benchmark has been run yet, so measured rows remain pending.

## How to record a run

- Run the same input with the settings being compared; record language, provider/model, and any important decoding or voice settings.
- Record date, run count, and elapsed time. Prefer the median of three runs when practical; if only one run is available, report `n=1` and do not imply it is representative.
- For STT, add real-time factor (processing time divided by input audio duration) when available. For TTS, note generated audio duration or time-to-first-audio when available.
- Add a quality or cost measure only when it was actually measured. State the metric and units; note differences or limitations that make results non-comparable.
- Mark scenarios that have not been run as `pending`. Never fill in estimates as measurements.

## Results

No scenarios have been measured yet.

The shared web interface and its Kokoro and Whistle scenarios are documented
but have not been run end-to-end in this environment. Their benchmark rows
remain pending until model inference is performed with a documented input and
settings.

| Date | Modality / scenario | Input | Provider / model | Settings (language, etc.) | Runs | Elapsed time | Extra metric (units) | Quality / cost | Notes |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| pending | TTS / shared Speech Lab UI | transcripts `fleurs-es419-01` through `fleurs-es419-05` | Kokoro | Spanish Latin American; `ef_dora`; speed 1; 24 kHz | pending | pending | generated duration / RTF | pending | Five fixed text inputs; inference not run yet. |
| pending | TTS / shared Speech Lab UI | transcripts `fleurs-enus-01` through `fleurs-enus-05` | Kokoro | English (US); `af_heart`; speed 1; 24 kHz | pending | pending | generated duration / RTF | pending | Five fixed text inputs; inference not run yet. |
| pending | STT / shared Speech Lab UI | `samples/audio/fleurs-es419-01.wav` through `fleurs-es419-05.wav` | Cactus Needle / Whistle | Spanish (`es`); explicitly selected; package defaults | pending | pending | RTF | pending | Five fixed clips with paired reference transcripts; inference not run yet. |
| pending | STT / shared Speech Lab UI | `samples/audio/fleurs-enus-01.wav` through `fleurs-enus-05.wav` | Cactus Needle / Whistle | English (`en`); explicitly selected; package defaults | pending | pending | RTF | pending | Five fixed clips with paired reference transcripts; inference not run yet. |
