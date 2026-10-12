#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/web-app/.venv"
PRUNE_UV_CACHE=false
REMOVE_MODELS=false

usage() {
    printf 'Usage: %s [--prune-uv-cache] [--models]\n' "${0##*/}"
    printf 'Remove this lab\x27s virtual environment.\n'
    printf '  --prune-uv-cache  Also prune unused uv package-cache files.\n'
    printf '  --models          Offer to remove Kokoro and Whistle model caches.\n'
}

for argument in "$@"; do
    case "$argument" in
        --prune-uv-cache)
            PRUNE_UV_CACHE=true
            ;;
        --models)
            REMOVE_MODELS=true
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            usage >&2
            exit 2
            ;;
    esac
done

if [[ -d "$VENV_DIR" ]]; then
    printf 'Removing project environment: %s\n' "$VENV_DIR"
    rm -rf -- "$VENV_DIR"
else
    printf 'No project environment found; nothing to remove.\n'
fi

if [[ "$PRUNE_UV_CACHE" == true ]]; then
    if command -v mise >/dev/null 2>&1; then
        mise exec -- uv cache prune
    elif command -v uv >/dev/null 2>&1; then
        uv cache prune
    else
        printf 'Warning: uv is unavailable; skipped uv cache pruning.\n' >&2
    fi
fi

if [[ "$REMOVE_MODELS" == true ]]; then
    if [[ -n "${HF_HUB_CACHE:-}" ]]; then
        HF_CACHE="$HF_HUB_CACHE"
    elif [[ -n "${HF_HOME:-}" ]]; then
        HF_CACHE="$HF_HOME/hub"
    elif [[ -n "${XDG_CACHE_HOME:-}" ]]; then
        HF_CACHE="$XDG_CACHE_HOME/huggingface/hub"
    else
        HF_CACHE="$HOME/.cache/huggingface/hub"
    fi

    MODEL_DIRS=(
        "$HF_CACHE/models--hexgrad--Kokoro-82M"
        "$HF_CACHE/models--Cactus-Compute--whistle"
        "$HF_CACHE/models--Cactus-Compute--needle3"
        "$HOME/.cache/cactus-needle/whistle"
        "$HOME/.cache/cactus-needle/v3"
    )
    EXISTING_MODEL_DIRS=()
    for model_dir in "${MODEL_DIRS[@]}"; do
        if [[ -d "$model_dir" ]]; then
            EXISTING_MODEL_DIRS+=("$model_dir")
        fi
    done

    if ((${#EXISTING_MODEL_DIRS[@]} == 0)); then
        printf 'No Kokoro or Whistle model-cache directories found.\n'
    else
        printf '\nThe following shared model-cache directories will be removed:\n'
        printf '  %s\n' "${EXISTING_MODEL_DIRS[@]}"
        printf 'Other projects may need to download these models again.\n'
        if [[ -n "${NEEDLE_WHISTLE_WEIGHTS:-}" ]]; then
            printf 'NEEDLE_WHISTLE_WEIGHTS is set; its custom file will not be removed.\n'
        fi
        read -r -p 'Delete these model caches? [y/N] ' answer || answer=''
        case "$answer" in
            y|Y|yes|YES|Yes)
                for model_dir in "${EXISTING_MODEL_DIRS[@]}"; do
                    rm -rf -- "$model_dir"
                    printf 'Removed %s\n' "$model_dir"
                done
                ;;
            *)
                printf 'Kept model caches.\n'
                ;;
        esac
    fi
else
    printf 'Model caches were left untouched. Use --models to review and remove them.\n'
fi

printf 'Done.\n'
