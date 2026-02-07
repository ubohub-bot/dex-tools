# dex-tools

Smart home CLIs and utilities for Dex (AI assistant).

## Tools

| Tool | Description |
|------|-------------|
| [lights/](lights/) | WLED LED strip control |
| [cast/](cast/) | Chromecast / Nebula projector control |
| [adb/](adb/) | Android device control via ADB |
| [voice/](voice/) | TTS announcements (macOS `say`) |
| [cam/](cam/) | DJI Osmo Pocket 3 capture via Windows PC |
| [stremio/](stremio/) | Stremio control on Nebula via ADB |

## Install

```bash
# Clone
git clone https://github.com/ubohub-bot/dex-tools.git
cd dex-tools

# Symlink tools to PATH
ln -s $(pwd)/lights/dex-lights /usr/local/bin/
ln -s $(pwd)/cast/dex-cast /usr/local/bin/
ln -s $(pwd)/adb/dex-adb /usr/local/bin/
ln -s $(pwd)/voice/dex_tts.py /usr/local/bin/dex-tts
# etc.
```

## Usage

```bash
# Lights
dex-lights on
dex-lights warm
dex-lights party

# Cast
dex-cast status
dex-cast play https://example.com/video.mp4

# ADB
dex-adb screenshot
dex-adb shell pm list packages

# Voice
dex-tts "Hello world"
```

## Requirements

- macOS (for voice TTS)
- Python 3.10+ (for voice)
- ADB (for adb, stremio tools)
- Network access to devices
