"""Shared local web interface for Speech Lab experiments."""

import gradio as gr

from providers.kokoro.adapter import VOICES, generate
from providers.needle.adapter import transcribe
from ui import ERROR_COPY_JS, LAB_CSS, TRANSCRIPT_COPY_JS, build_theme


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
    gr.HTML(
        '<header class="lab-header">'
        '<p class="lab-eyebrow">Local speech experiments</p>'
        '<h1>Speech Lab</h1>'
        '<p>A small space to explore speech models.<br>'
        'Turn text into audio, or audio into text.</p>'
        '</header>',
        apply_default_css=False,
    )

    with gr.Tabs(elem_id="lab-tabs"):
        with gr.Tab("Text to speech"):
            with gr.Row(elem_classes="lab-workspace"):
                with gr.Column(
                    scale=3, min_width=360, variant="panel", elem_classes="lab-panel"
                ):
                    gr.Markdown("## Input", elem_classes="lab-section")
                    with gr.Column(min_width=0, elem_classes="lab-config"):
                        gr.Markdown("### Model settings", elem_classes="lab-config-title")
                        tts_provider = gr.Dropdown(
                            choices=["Kokoro"], value="Kokoro", label="Model / provider"
                        )
                        with gr.Column(elem_classes="lab-settings"):
                            tts_language = gr.Dropdown(
                                choices=list(VOICES),
                                value="Español latinoamericano",
                                label="Language",
                                min_width=0,
                            )
                            tts_voice = gr.Dropdown(
                                choices=list(VOICES["Español latinoamericano"].items()),
                                value="ef_dora",
                                label="Voice",
                                min_width=0,
                            )
                    tts_language.change(
                        update_voices, inputs=tts_language, outputs=tts_voice
                    )
                    tts_text = gr.Textbox(
                        label="Text", lines=6, placeholder="Type what you want to hear…"
                    )
                    tts_button = gr.Button(
                        "Generate audio", variant="primary", elem_classes="lab-action"
                    )
                with gr.Column(
                    scale=2,
                    min_width=280,
                    variant="panel",
                    elem_classes=["lab-panel", "lab-result"],
                ):
                    gr.Markdown("## Audio output", elem_classes="lab-section")
                    tts_output = gr.Audio(label="Generated audio", interactive=False)
                    gr.Markdown(
                        "Kokoro · 24 kHz · Speed 1.0", elem_classes="lab-note"
                    )
            tts_button.click(
                run_tts,
                inputs=[tts_provider, tts_text, tts_language, tts_voice],
                outputs=tts_output,
            )

        with gr.Tab("Speech to text"):
            with gr.Row(elem_classes="lab-workspace"):
                with gr.Column(
                    scale=3, min_width=360, variant="panel", elem_classes="lab-panel"
                ):
                    gr.Markdown("## Input", elem_classes="lab-section")
                    with gr.Column(min_width=0, elem_classes="lab-config"):
                        gr.Markdown("### Model settings", elem_classes="lab-config-title")
                        stt_provider = gr.Dropdown(
                            choices=["Needle / Whistle"],
                            value="Needle / Whistle",
                            label="Model / provider",
                        )
                    stt_audio = gr.Audio(
                        label="Audio",
                        sources=["upload", "microphone"],
                        type="filepath",
                        format="wav",
                    )
                    gr.Markdown(
                        "Upload or record audio you are authorized to use.",
                        elem_classes="lab-note",
                    )
                    stt_button = gr.Button(
                        "Transcribe", variant="primary", elem_classes="lab-action"
                    )
                with gr.Column(
                    scale=2,
                    min_width=280,
                    variant="panel",
                    elem_classes=["lab-panel", "lab-result"],
                ):
                    gr.Markdown("## Transcript", elem_classes="lab-section")
                    stt_output = gr.Textbox(
                        label="Transcript",
                        lines=10,
                        interactive=False,
                        placeholder="Your transcript will appear here.",
                    )
                    gr.HTML(
                        '<button type="button" class="lab-copy-transcript" '
                        'aria-label="Copy transcript text">Copy transcript</button>',
                        apply_default_css=False,
                        js_on_load=TRANSCRIPT_COPY_JS,
                    )
                    gr.Markdown(
                        "Automatic language detection. Supports Spanish, English, "
                        "and other documented Whistle languages.",
                        elem_classes="lab-note",
                    )
            stt_button.click(
                run_stt, inputs=[stt_provider, stt_audio], outputs=stt_output
            )
    gr.HTML(
        '<p class="lab-footer">Models run on this machine. '
        'First use may download model assets.</p>',
        apply_default_css=False,
        js_on_load=ERROR_COPY_JS,
    )


if __name__ == "__main__":
    app.launch(theme=build_theme(), css=LAB_CSS, show_error=True, footer_links=[])
