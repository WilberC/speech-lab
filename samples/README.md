# Benchmark sample fixtures

These ten short clips form a small, fixed personal benchmark set: five US
English (`en_us`) and five Latin American Spanish (`es_419`). Each WAV is paired
with its reference transcript under `transcripts/` using the same sample ID.

## Provenance and license

The audio and transcripts are selected from the test splits of Google's
[FLEURS-R dataset](https://huggingface.co/datasets/google/fleurs-r), revision
`c621c0b7b569dcebcd50273a187a35d1a1fc895f` ([Spanish](https://huggingface.co/datasets/google/fleurs-r/tree/c621c0b7b569dcebcd50273a187a35d1a1fc895f/data/es_419),
[US English](https://huggingface.co/datasets/google/fleurs-r/tree/c621c0b7b569dcebcd50273a187a35d1a1fc895f/data/en_us)).
The source dataset is licensed under [Creative Commons Attribution 4.0
International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Attribution: Google, [FLEURS-R: A Restored Multilingual Speech Corpus for
Generation Tasks](https://huggingface.co/datasets/google/fleurs-r). Change made:
ten clips and their transcript rows were extracted from the source test splits;
the WAV audio itself is unmodified. This repository redistributes only these
ten clips, not the full dataset. Do not attempt to identify speakers.

## Selected clips

| Sample ID | Language | Source clip | Duration | Reference transcript |
| --- | --- | --- | ---: | --- |
| `fleurs-enus-01` | English (US) | `4496786334735634498.wav` | 10.96 s | `transcripts/fleurs-enus-01.txt` |
| `fleurs-enus-02` | English (US) | `14210445503617137582.wav` | 7.68 s | `transcripts/fleurs-enus-02.txt` |
| `fleurs-enus-03` | English (US) | `5106380017322065030.wav` | 8.52 s | `transcripts/fleurs-enus-03.txt` |
| `fleurs-enus-04` | English (US) | `6873447881355850328.wav` | 5.64 s | `transcripts/fleurs-enus-04.txt` |
| `fleurs-enus-05` | English (US) | `5922110980503615373.wav` | 6.72 s | `transcripts/fleurs-enus-05.txt` |
| `fleurs-es419-01` | Spanish (Latin America) | `10615442135828084492.wav` | 10.84 s | `transcripts/fleurs-es419-01.txt` |
| `fleurs-es419-02` | Spanish (Latin America) | `355675141573691135.wav` | 12.16 s | `transcripts/fleurs-es419-02.txt` |
| `fleurs-es419-03` | Spanish (Latin America) | `16036386228143006078.wav` | 15.28 s | `transcripts/fleurs-es419-03.txt` |
| `fleurs-es419-04` | Spanish (Latin America) | `10891154757063940475.wav` | 7.08 s | `transcripts/fleurs-es419-04.txt` |
| `fleurs-es419-05` | Spanish (Latin America) | `9213540287672010926.wav` | 10.96 s | `transcripts/fleurs-es419-05.txt` |
