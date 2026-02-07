# dex-stremio

Control Stremio on Nebula projector via ADB.

## Setup

Nebula needs ADB debugging enabled:
1. Settings > About > tap Build 7 times
2. Developer Options > enable USB/Network Debugging
3. Authorize Mac when prompted

## Usage

```bash
# Search for movies/shows
dex-stremio search "Inception"
dex-stremio search "Breaking Bad"

# Play by IMDB ID (from search results)
dex-stremio play tt1375666           # Inception
dex-stremio play tt0903747 S01E01    # Breaking Bad S1E1

# Open Stremio app
dex-stremio open

# Playback controls
dex-stremio pause
dex-stremio resume
dex-stremio stop

# Navigation
dex-stremio back
dex-stremio home
dex-stremio up/down/left/right
dex-stremio select
```

## How it works

1. Search uses OMDB API (free, no key needed)
2. Play sends Stremio deep link via ADB
3. Auto-presses select to start playback
4. Controls use Android keycodes

## Configuration

- `NEBULA_IP` - Projector IP (default: 192.168.0.248)
- `TMDB_API_KEY` - Optional, for better search results
