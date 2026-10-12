"""Kokoro provider adapter for the shared Speech Lab UI."""

from functools import lru_cache

VOICES = {
    "Español latinoamericano": {
        "Dora — femenina": "ef_dora",
        "Alex — masculina": "em_alex",
        "Santa — masculina": "em_santa",
    },
    "English (US)": {
        "Heart — feminine": "af_heart",
        "Bella — feminine": "af_bella",
        "Michael — masculine": "am_michael",
    },
}
LANGUAGE_CODES = {"Español latinoamericano": "e", "English (US)": "a"}
SAMPLE_RATE = 24_000


@lru_cache(maxsize=len(LANGUAGE_CODES))
def _pipeline(language_code: str):
    import torch
    from kokoro import KPipeline

    device = "cuda" if torch.cuda.is_available() else "cpu"
    return KPipeline(lang_code=language_code, device=device)


def generate(text: str, language: str, voice: str):
    import numpy as np

    if not text or not text.strip():
        raise ValueError("Enter text before generating audio.")
    if language not in LANGUAGE_CODES or voice not in VOICES[language].values():
        raise ValueError("Choose a voice available for the selected language.")

    chunks = [
        audio
        for _, _, audio in _pipeline(LANGUAGE_CODES[language])(
            text.strip(), voice=voice, speed=1
        )
        if audio is not None
    ]
    if not chunks:
        raise ValueError("Kokoro did not generate audio for this input.")
    return SAMPLE_RATE, np.concatenate(chunks)
