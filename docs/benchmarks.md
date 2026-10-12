# Benchmark notes

Use this small log to keep measured comparisons with the repository. Keep audio, model output, and other generated artifacts out of Git; link only to stable sample IDs or external artifact locations when needed.

## How to record a run

- Run the same input with the settings being compared; record language, provider/model, and any important decoding or voice settings.
- Record date, run count, and elapsed time. Prefer the median of three runs when practical; if only one run is available, report `n=1` and do not imply it is representative.
- For STT, add real-time factor (processing time divided by input audio duration) when available. For TTS, note generated audio duration or time-to-first-audio when available.
- Add a quality or cost measure only when it was actually measured. State the metric and units; note differences or limitations that make results non-comparable.
- Mark scenarios that have not been run as `pending`. Never fill in estimates as measurements.

## Results

No scenarios have been measured yet.

| Date | Modality / scenario | Input | Provider / model | Settings (language, etc.) | Runs | Elapsed time | Extra metric (units) | Quality / cost | Notes |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
