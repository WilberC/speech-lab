"""Regression checks for theme integration without loading speech models."""

import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

import gradio as gr
from gradio.data_classes import FileData

from ui import ERROR_COPY_JS, LAB_CSS, build_theme


class ThemeTests(unittest.TestCase):
    def test_system_dark_mode_uses_the_same_light_tokens(self):
        theme = build_theme()
        for name in vars(theme):
            if name.endswith("_dark"):
                with self.subTest(token=name):
                    self.assertEqual(
                        getattr(theme, name),
                        getattr(theme, name.removesuffix("_dark")),
                    )
        self.assertEqual(theme.body_background_fill, "#faf9f5")
        self.assertEqual(theme.input_background_fill, "#fffdf9")
        self.assertEqual(theme.block_border_width, "0px")
        self.assertEqual(theme.panel_border_width, "0px")
        self.assertEqual(theme.block_border_color, "#c8b9a7")
        self.assertEqual(theme.input_border_color, "#b9a895")
        self.assertIn("#faf9f5", theme._get_theme_css())

    def test_launch_receives_css_and_theme_using_gradio_6_api(self):
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        with patch.object(gr.Blocks, "launch") as launch:
            namespace = runpy.run_path(str(app_path), run_name="__main__")
        launch.assert_called_once()
        self.assertEqual(launch.call_args.kwargs["css"], LAB_CSS)
        self.assertIsInstance(launch.call_args.kwargs["theme"], gr.themes.Base)
        self.assertTrue(launch.call_args.kwargs["show_error"])
        self.assertEqual(namespace["ERROR_COPY_JS"], ERROR_COPY_JS)
        self.assertIn("navigator.clipboard.writeText(content)", ERROR_COPY_JS)
        self.assertIn("Copy all error details", ERROR_COPY_JS)
        self.assertIn("Error details copied", ERROR_COPY_JS)
        self.assertIn("max-block-size: min(32vh, 16rem)", LAB_CSS)
        self.assertFalse(namespace["tts_output"].interactive)
        self.assertFalse(namespace["stt_output"].interactive)
        self.assertEqual(
            namespace["stt_language"].choices,
            [("Español", "es"), ("English", "en")],
        )
        self.assertEqual(namespace["stt_language"].value, "es")
        self.assertEqual(namespace["stt_audio"].format, "wav")
        for source_path in ("/tmp/uploaded.mp3", "/tmp/recorded.webm"):
            with self.subTest(source=source_path):
                with (
                    patch(
                        "gradio.components.audio.processing_utils.audio_from_file",
                        return_value=(44_100, [0]),
                    ),
                    patch("gradio.components.audio.processing_utils.audio_to_file") as convert,
                ):
                    normalized_path = namespace["stt_audio"].preprocess(
                        FileData(path=source_path)
                    )
                self.assertEqual(normalized_path, source_path.rsplit(".", 1)[0] + ".wav")
                convert.assert_called_once()
        blocks = namespace["app"].blocks.values()
        settings_sections = [
            block
            for block in blocks
            if isinstance(block, gr.Column) and "lab-config" in block.elem_classes
        ]
        self.assertEqual(len(settings_sections), 2)
        self.assertFalse(
            any(
                isinstance(block, gr.Markdown)
                and "not specifically trained for Peruvian Spanish" in block.value
                for block in blocks
            )
        )


if __name__ == "__main__":
    unittest.main()
