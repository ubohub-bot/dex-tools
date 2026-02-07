# dex-lights 💡

CLI to control WLED LED strip. Part of Dex's home automation toolkit.

## Install

```bash
# Already symlinked to /usr/local/bin/dex-lights
dex-lights status
```

## Usage

```bash
# Power
dex-lights on
dex-lights off

# Named colors
dex-lights red
dex-lights purple
dex-lights warm      # warm white
dex-lights cool      # cool white

# Hex colors
dex-lights #FF5500
dex-lights ff00ff

# RGB
dex-lights rgb 255 100 50

# Brightness (0-255)
dex-lights bri 128

# Effects
dex-lights party     # colorful fast
dex-lights rainbow   # classic rainbow
dex-lights chill     # slow color fade
dex-lights fire      # fire effect
dex-lights pulse     # breathing

# Custom effect by ID (0-117)
dex-lights fx 42

# Status
dex-lights status
```

## Configuration

Edit the script to change `WLED_IP` if your WLED is at a different address.

Default: `192.168.0.176`

## WLED API

This uses WLED's JSON API:
- `GET /json/state` - current state
- `POST /json/state` - update state
- `GET /json/info` - device info

Docs: https://kno.wled.ge/interfaces/json-api/
