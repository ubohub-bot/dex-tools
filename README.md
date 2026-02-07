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

## Skills

Reusable AI agent skills in [skills/](skills/):

| Skill | Description |
|-------|-------------|
| [frontend-design](skills/frontend-design/) | Distinctive, production-grade UI design |

## Install

```bash
# Clone
git clone https://github.com/ubohub-bot/dex-tools.git
cd dex-tools

# Symlink tools to PATH
ln -s $(pwd)/lights/dex-lights /usr/local/bin/
ln -s $(pwd)/cast/dex-cast /usr/local/bin/
ln -s $(pwd)/adb/dex-adb /usr/local/bin/
# etc.

# Symlink skills to OpenClaw
ln -s $(pwd)/skills/* ~/.openclaw/skills/
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
python voice/dex_tts.py "Hello world"
```

## Requirements

- macOS (for voice TTS)
- Python 3.10+ (for voice)
- ADB (for adb, stremio tools)
- Network access to devices

## License

Tools are provided as-is. Skills may have individual licenses (see each skill folder).
