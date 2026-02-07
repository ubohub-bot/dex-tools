# dex-cam 📸

Capture images from DJI Osmo Pocket 3 via Windows PC. Part of Dex's home automation toolkit.

## How it works

Osmo Pocket 3 webcam mode only works on Windows. This CLI:
1. SSH to Windows PC
2. Captures frame via ffmpeg DirectShow
3. SCPs image back to Mac

## Install

```bash
# Already symlinked to /usr/local/bin/dex-cam
dex-cam status
```

## Requirements

- Windows PC with Osmo connected in webcam mode
- SSH access to Windows PC (via Tailscale)
- ffmpeg installed on Windows

## Usage

```bash
# Quick capture (1080p)
dex-cam

# 4K capture
dex-cam --4k

# 720p (faster)
dex-cam --720p

# Save to specific path
dex-cam -o ~/Desktop/snapshot.jpg

# Open after capture (macOS)
dex-cam --show

# JSON output for scripting
dex-cam --json

# Check if camera is connected
dex-cam status
dex-cam status --json
```

## Configuration

Edit the script to change:
- `WINDOWS_HOST` - Windows PC IP (default: 100.96.244.31)
- `WINDOWS_USER` - SSH user (default: Zeu)
- `CAMERA_NAME` - DirectShow device name (default: OsmoPocket3)

## Bonus: Other cameras detected

The Windows PC also has:
- Meta Quest 3, 3S, 2, Pro (virtual cameras)
- NVIDIA Broadcast (virtual camera)
- Immersed Webcam
