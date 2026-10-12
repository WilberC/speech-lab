"""Checks that the Needle adapter only passes supported language codes."""

import sys
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from providers.needle.adapter import transcribe


class TranscriptionLanguageTests(unittest.TestCase):
    def test_transcribe_passes_selected_english_language_to_needle(self):
        needle_transcribe = Mock(return_value={"text": "Hello world."})
        fake_needle = SimpleNamespace(transcribe=needle_transcribe)

        with patch.dict(sys.modules, {"needle": fake_needle}):
            result = transcribe("sample.wav", "en")

        self.assertEqual(result, "Hello world.")
        needle_transcribe.assert_called_once_with("sample.wav", language="en")

    def test_transcribe_passes_selected_spanish_language_to_needle(self):
        needle_transcribe = Mock(return_value={"text": "Hola mundo."})
        fake_needle = SimpleNamespace(transcribe=needle_transcribe)

        with patch.dict(sys.modules, {"needle": fake_needle}):
            result = transcribe("sample.wav", "es")

        self.assertEqual(result, "Hola mundo.")
        needle_transcribe.assert_called_once_with("sample.wav", language="es")

    def test_transcribe_rejects_languages_outside_the_lab_scope(self):
        with self.assertRaisesRegex(ValueError, "English or Spanish"):
            transcribe("sample.wav", "fr")


if __name__ == "__main__":
    unittest.main()
