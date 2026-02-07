# dex-cast 📺

Cast media to Nebula projector (Chromecast). Part of Dex's home automation toolkit.

## Install

Requires `catt` (Cast All The Things):
```bash
pip install catt
```

## Usage

```bash
# Cast YouTube video
dex-cast "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Cast any media URL
dex-cast "https://example.com/video.mp4"

# Playback control
dex-cast stop
dex-cast pause
dex-cast play

# Volume (0-100)
dex-cast volume 50

# Status and info
dex-cast status
dex-cast info
dex-cast status --json
```

## Configuration

Edit the script to change:
- `NEBULA_IP` - Projector IP (default: 192.168.0.248)
- `NEBULA_NAME` - Device name (default: D2426)

## Device

- **Nebula Capsule** - Portable Chromecast-compatible projector
- Also has good speakers - great for music!
