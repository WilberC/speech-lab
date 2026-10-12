"""Whistle (Cactus Needle) provider adapter for the shared Speech Lab UI."""

from pathlib import Path

SUPPORTED_LANGUAGES = {"Español": "es", "English": "en"}


def transcribe(audio_path: str | None, language: str) -> str:
    if not audio_path:
        raise ValueError("Record or upload an audio file first.")
    if language not in SUPPORTED_LANGUAGES.values():
        raise ValueError("Choose English or Spanish for transcription.")

    import needle

    result = needle.transcribe(str(Path(audio_path)), language=language)
    return result.get("text", "")
