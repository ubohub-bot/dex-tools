# dex-adb 📱

Android device control via ADB. Part of Dex's home automation toolkit.

## Devices

| Alias | Device | IP |
|-------|--------|-----|
| `phone` | Motorola Edge 50 Neo | 192.168.0.112 |
| `tablet` | Xiaomi Redmi Pad | 192.168.0.239:37203 |

## Setup

Enable **Wireless Debugging** on each device:
1. Settings → Developer Options → Wireless Debugging
2. First time: pair with `adb pair <ip>:<port> <code>`
3. Then connect: `dex-adb connect phone`

## Usage

```bash
# List connected devices
dex-adb devices

# Connect to device
dex-adb connect tablet
dex-adb connect phone

# Device info
dex-adb info tablet

# Screenshot
dex-adb screenshot tablet
dex-adb screenshot phone --show

# Launch apps (aliases: spotify, youtube, chrome, telegram, etc.)
dex-adb launch tablet spotify
dex-adb launch phone youtube

# Open URL
dex-adb open tablet "https://youtube.com/watch?v=dQw4w9WgXcQ"

# Screen control
dex-adb screen tablet on
dex-adb screen tablet off

# Input
dex-adb tap tablet 500 500
dex-adb input tablet "hello world"

# Raw shell
dex-adb shell tablet "dumpsys battery"
```

## App Aliases

- `spotify`, `youtube`, `chrome`, `settings`
- `camera`, `photos`, `telegram`, `whatsapp`

Or use full package name: `com.example.app`
