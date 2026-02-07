# dex-voice

Simple TTS for Dex announcements using macOS `say` command.

No API keys needed.

## Usage

```bash
# Speak text
./dex_tts.py "Lights turned on"

# Different voice
./dex_tts.py -v Alex "Hello there"

# List available voices
./dex_tts.py --list-voices

# Pipe text
echo "Motion detected" | ./dex_tts.py
```

## Install

```bash
chmod +x dex_tts.py

# Optional: symlink to PATH
ln -s $(pwd)/dex_tts.py /usr/local/bin/dex-tts
```

## Config

- **Default voice:** Samantha
- **Default device:** 73 (Nebula projector speakers)

Change defaults in script or pass `-v` / `-d` flags.

## Use Cases

- Announce smart home changes (lights, projector, etc.)
- Speak on demand via Telegram
- Alert notifications

## Requirements

- macOS (uses `say` command)
- Python 3.10+
