"""Shared local web interface for Speech Lab experiments."""

import gradio as gr

from providers.kokoro.adapter import VOICES, generate
from providers.needle.adapter import transcribe


def update_voices(language: str):
    choices = list(VOICES[language].items())
    return gr.Dropdown(choices=choices, value=choices[0][1])


def run_tts(provider: str, text: str, language: str, voice: str):
    if provider != "Kokoro":
        raise gr.Error("Choose an available text-to-speech provider.")
    try:
        return generate(text, language, voice)
    except (ImportError, ModuleNotFoundError) as error:
        raise gr.Error(
            "Kokoro dependencies are missing. From web-app/, run: uv sync --extra kokoro."
        ) from error
    except ValueError as error:
        raise gr.Error(str(error)) from error


def run_stt(provider: str, audio_path: str | None):
    if provider != "Needle / Whistle":
        raise gr.Error("Choose an available speech-to-text provider.")
    try:
        return transcribe(audio_path)
    except (ImportError, ModuleNotFoundError) as error:
        raise gr.Error(
            "Needle dependencies are missing. From web-app/, run: uv sync --extra needle."
        ) from error
    except ValueError as error:
        raise gr.Error(str(error)) from error


with gr.Blocks(title="Speech Lab") as app:
    gr.Markdown("# Speech Lab")
    gr.Markdown(
        "A shared local interface for independent speech provider experiments. "
        "Models run on this machine; the first use may download model assets."
    )

    with gr.Tabs():
        with gr.Tab("Text to speech"):
            tts_provider = gr.Dropdown(
                choices=["Kokoro"], value="Kokoro", label="Model / provider"
            )
            gr.Markdown(
                "Kokoro · Spanish voices are general Latin American, "
                "not specifically trained for Peruvian Spanish."
            )
            tts_language = gr.Dropdown(
                choices=list(VOICES), value="Español latinoamericano", label="Language"
            )
            tts_voice = gr.Dropdown(
                choices=list(VOICES["Español latinoamericano"].items()),
                value="ef_dora",
                label="Voice",
            )
            tts_language.change(update_voices, inputs=tts_language, outputs=tts_voice)
            tts_text = gr.Textbox(label="Text", lines=5, placeholder="Type what you want to hear…")
            tts_button = gr.Button("Generate audio", variant="primary")
            tts_output = gr.Audio(label="Generated audio")
            tts_button.click(
                run_tts,
                inputs=[tts_provider, tts_text, tts_language, tts_voice],
                outputs=tts_output,
            )

        with gr.Tab("Speech to text"):
            stt_provider = gr.Dropdown(
                choices=["Needle / Whistle"],
                value="Needle / Whistle",
                label="Model / provider",
            )
            gr.Markdown(
                "Needle / Whistle · Automatic language detection; documented support "
                "includes Spanish and English."
            )
            stt_audio = gr.Audio(
                label="Audio", sources=["upload", "microphone"], type="filepath"
            )
            stt_button = gr.Button("Transcribe", variant="primary")
            stt_output = gr.Textbox(label="Transcript", lines=8)
            stt_button.click(
                run_stt, inputs=[stt_provider, stt_audio], outputs=stt_output
            )


if __name__ == "__main__":
    app.launch()
