"""Whistle (Cactus Needle) provider adapter for the shared Speech Lab UI."""

from pathlib import Path


def transcribe(audio_path: str | None) -> str:
    if not audio_path:
        raise ValueError("Record or upload an audio file first.")

    import needle

    result = needle.transcribe(str(Path(audio_path)))
    return result.get("text", "")
