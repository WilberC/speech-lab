"""Light-only editorial theme and layout styles for the local lab."""

import gradio as gr


def build_theme() -> gr.themes.Base:
    """Use native component tokens, including when the OS prefers dark mode."""
    theme = gr.themes.Base(
        font=["Inter", "Segoe UI", "system-ui", "sans-serif"],
        font_mono=["ui-monospace", "monospace"],
    ).set(
        body_background_fill="#faf9f5",
        body_text_color="#141413",
        body_text_color_subdued="#6c6a64",
        background_fill_primary="#faf9f5",
        background_fill_secondary="#f5f0e8",
        border_color_primary="#e6dfd8",
        border_color_accent="#a9583e",
        border_color_accent_subdued="#e6dfd8",
        color_accent="#a9583e",
        color_accent_soft="#efe9de",
        link_text_color="#a9583e",
        link_text_color_hover="#a9583e",
        link_text_color_active="#a9583e",
        link_text_color_visited="#a9583e",
        block_background_fill="#faf9f5",
        block_border_color="#c8b9a7",
        block_border_width="0px",
        block_label_background_fill="#faf9f5",
        block_label_text_color="#3d3d3a",
        block_info_text_color="#6c6a64",
        block_title_text_color="#141413",
        block_shadow="none",
        block_radius="8px",
        panel_background_fill="#faf9f5",
        panel_border_color="#e6dfd8",
        panel_border_width="0px",
        input_background_fill="#fffdf9",
        input_background_fill_focus="#fffdf9",
        input_background_fill_hover="#fffdf9",
        input_border_color="#b9a895",
        input_border_width="1px",
        input_border_color_focus="#a9583e",
        input_border_color_hover="#b9a895",
        input_placeholder_color="#6c6a64",
        input_radius="8px",
        input_shadow="none",
        input_shadow_focus="0 0 0 3px rgb(204 120 92 / 15%)",
        button_primary_background_fill="#cc785c",
        button_primary_background_fill_hover="#a9583e",
        button_primary_border_color="#cc785c",
        button_primary_border_color_hover="#a9583e",
        button_primary_text_color="#141413",
        button_primary_text_color_hover="#ffffff",
        button_primary_shadow="none",
        button_primary_shadow_hover="none",
        button_secondary_background_fill="#faf9f5",
        button_secondary_background_fill_hover="#efe9de",
        button_secondary_text_color="#3d3d3a",
        button_secondary_text_color_hover="#141413",
        button_secondary_border_color="#e6dfd8",
        button_secondary_border_color_hover="#d4ccc1",
        button_large_radius="8px",
        button_small_radius="8px",
        button_medium_radius="8px",
        button_transform_hover="none",
        button_transform_active="none",
        loader_color="#a9583e",
        slider_color="#a9583e",
    )
    # Gradio applies .dark independently of CSS color-scheme. Mirror every
    # native token rather than painting over individual component internals.
    light_tokens = {
        name: getattr(theme, name.removesuffix("_dark"))
        for name in vars(theme)
        if name.endswith("_dark")
    }
    # Base.set() resets these two fills unless they are passed explicitly.
    return theme.set(
        **light_tokens,
        background_fill_primary=theme.background_fill_primary,
        background_fill_secondary=theme.background_fill_secondary,
    )


LAB_CSS = """
html, body, gradio-app { background: #faf9f5 !important; color-scheme: light; }
.gradio-container {
    width: min(100%, 1060px) !important;
    max-width: 1060px !important;
    margin-inline: auto !important;
    padding: 24px clamp(16px, 3vw, 32px) 40px !important;
    box-sizing: border-box !important;
}
.gradio-container .main { padding: 0 !important; }
.lab-header { text-align: center; padding: 20px 0 32px; }
.lab-header h1 {
    font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 400;
    line-height: 1.08;
    letter-spacing: -.035em;
    margin: 8px 0 12px;
    color: #141413;
}
.lab-header p { margin: 0 auto; max-width: 540px; color: #6c6a64; line-height: 1.55; }
.lab-header .lab-eyebrow { font-size: .75rem; letter-spacing: .12em; text-transform: uppercase; }
#lab-tabs .tab-container { justify-content: center; gap: 8px; border-bottom: 0 !important; }
#lab-tabs .tab-container button {
    padding: 10px 18px !important; border: 0 !important; border-radius: 8px !important;
    color: #6c6a64; background: transparent; min-height: 44px !important;
}
#lab-tabs button[aria-selected="true"] { background: #e8e0d2; color: #141413; }
#lab-tabs > .tabitem { padding: 24px 0 0; border: 0; }
.lab-panel { padding: 16px 8px !important; border: 0 !important; border-radius: 0 !important; gap: 20px !important; }
.lab-config {
    background: #f5f0e8 !important; border: 0 !important;
    border-radius: 12px !important; padding: 20px !important; gap: 12px !important;
}
.lab-config-title h3 {
    margin: 0; font-family: inherit; font-size: .95rem;
    font-weight: 600; color: #3d3d3a;
}
.lab-result { background: #efe9de !important; border: 0 !important; border-radius: 12px !important; padding: 20px !important; }
.lab-result [aria-label="Empty value"].empty.small {
    border: 1px solid #c8b9a7;
    border-radius: 8px;
    padding: 10px;
    box-sizing: border-box;
}
.lab-panel button.upload-container[aria-label="Drop an audio file here to upload"] {
    background: #fffdf9;
    border: 1px solid #c8b9a7;
    border-radius: 8px;
    padding: 10px;
}
.lab-panel > * { flex-grow: 0 !important; }
.lab-panel .block { border: 0 !important; background: transparent !important; padding: 0 !important; }
.lab-panel .form { background: transparent !important; }
.lab-config .lab-settings { gap: 12px; }
.lab-config .lab-settings > .form { width: 100%; min-width: 0 !important; }
.lab-config .wrap { min-width: 0; }
.lab-section h2 {
    font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
    font-size: 1.6rem; font-weight: 400; letter-spacing: -.02em;
    color: #141413; margin: 0;
}
.lab-note, .lab-note p { font-size: .875rem; color: #6c6a64; line-height: 1.5; }
.lab-result .lab-note { margin-top: 4px; }
.lab-action { min-height: 44px !important; }
.lab-action:disabled { opacity: .55; }
.lab-footer { text-align: center; padding-top: 20px; font-size: .8rem; color: #6c6a64; }
.toast-body.error .toast-messages {
    max-block-size: min(32vh, 16rem);
    overflow: auto;
    overflow-wrap: anywhere;
    overscroll-behavior: contain;
}
.toast-message-text.error { white-space: pre-wrap; overflow-wrap: anywhere; }
.lab-copy-error {
    display: block;
    min-height: 40px;
    margin: 8px 0 0 auto;
    padding: 7px 12px;
    color: #141413;
    background: #fffdf9;
    border: 1px solid #a9583e;
    border-radius: 6px;
    font: inherit;
    font-size: .8rem;
    font-weight: 500;
    cursor: pointer;
}
.lab-copy-error:hover { background: #efe9de; }
.lab-copy-error:focus-visible { outline: 2px solid #a9583e; outline-offset: 2px; }
.lab-copy-transcript {
    display: block;
    min-height: 32px;
    margin: 8px 0 0 auto;
    padding: 4px 10px;
    color: #3d3d3a;
    background: #faf9f5;
    border: 1px solid #c8b9a7;
    border-radius: 6px;
    font: inherit;
    font-size: .78rem;
    cursor: pointer;
}
.lab-copy-transcript:hover { background: #efe9de; }
.lab-copy-transcript:focus-visible { outline: 2px solid #a9583e; outline-offset: 2px; }
.gradio-container button:focus-visible { outline: 2px solid #a9583e; outline-offset: 3px; }
@media (max-width: 767px) {
    #lab-tabs .tab-container button { padding-inline: 12px !important; }
    .lab-header { padding: 12px 0 24px; }
    .lab-panel { padding: 8px 0 !important; }
    .lab-result { padding: 18px !important; }
    .lab-config { padding: 16px !important; }
    .lab-workspace { flex-direction: column; }
    .lab-workspace > .lab-panel { min-width: 0 !important; width: 100%; }
}
"""

ERROR_COPY_JS = """
const root = element.getRootNode();
if (!root.__speechLabErrorCopyObserver) {
    const addCopyButtons = () => {
        for (const toast of root.querySelectorAll('.toast-body.error[role="status"]')) {
            if (toast.querySelector('.lab-copy-error')) continue;
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'lab-copy-error';
            button.textContent = 'Copy error';
            button.setAttribute('aria-label', 'Copy all error details');
            button.setAttribute('aria-live', 'polite');
            button.addEventListener('click', async () => {
                const title = toast.querySelector('.toast-title')?.innerText.trim() || 'Error';
                const details = Array.from(
                    toast.querySelectorAll('[data-testid="toast-text"]'),
                    (message) => message.innerText.trim()
                ).filter(Boolean).join('\\n\\n');
                const content = [title, details].filter(Boolean).join('\\n\\n');
                try {
                    await navigator.clipboard.writeText(content);
                } catch {
                    const clipboardField = document.createElement('textarea');
                    clipboardField.value = content;
                    clipboardField.style.position = 'fixed';
                    clipboardField.style.opacity = '0';
                    document.body.appendChild(clipboardField);
                    clipboardField.select();
                    const copied = document.execCommand('copy');
                    clipboardField.remove();
                    if (!copied) {
                        button.textContent = 'Copy failed';
                        button.setAttribute('aria-label', 'Copying error details failed');
                        return;
                    }
                }
                button.textContent = 'Copied';
                button.setAttribute('aria-label', 'Error details copied');
                window.setTimeout(() => {
                    if (button.isConnected) {
                        button.textContent = 'Copy error';
                        button.setAttribute('aria-label', 'Copy all error details');
                    }
                }, 1500);
            });
            const timer = toast.querySelector('.timer');
            toast.insertBefore(button, timer);
        }
    };
    addCopyButtons();
    root.__speechLabErrorCopyObserver = new MutationObserver(addCopyButtons);
    root.__speechLabErrorCopyObserver.observe(root, { childList: true, subtree: true });
}
"""

TRANSCRIPT_COPY_JS = """
const root = element.getRootNode();
if (!root.__speechLabTranscriptCopyHandler) {
    root.addEventListener('click', async (event) => {
        const button = event.target.closest('.lab-copy-transcript');
        if (!button) return;
        const transcript = button.closest('.lab-result')?.querySelector('textarea')?.value;
        if (!transcript?.trim()) return;
        try {
            await navigator.clipboard.writeText(transcript);
        } catch {
            const field = document.createElement('textarea');
            field.value = transcript;
            field.style.position = 'fixed';
            field.style.opacity = '0';
            document.body.appendChild(field);
            field.select();
            const copied = document.execCommand('copy');
            field.remove();
            if (!copied) return;
        }
        const original = button.textContent;
        button.textContent = 'Copied';
        window.setTimeout(() => { if (button.isConnected) button.textContent = original; }, 1500);
    });
    root.__speechLabTranscriptCopyHandler = true;
}
"""
