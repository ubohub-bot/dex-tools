#!/usr/bin/env python3
"""
dex-tts: Simple TTS for Dex announcements

Uses macOS `say` command - no API keys needed.
"""

import argparse
import subprocess
import sys

DEFAULT_VOICE = "Samantha"
DEFAULT_DEVICE = "73"  # Nebula projector speakers


def speak(text: str, voice: str = DEFAULT_VOICE, device: str = DEFAULT_DEVICE) -> bool:
    """Speak text using macOS say command."""
    cmd = ["say", "-v", voice, "-a", device, text]
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] say failed: {e}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("[ERROR] say command not found (macOS only)", file=sys.stderr)
        return False


def list_voices():
    """List available voices."""
    subprocess.run(["say", "-v", "?"])


def list_devices():
    """List audio output devices."""
    # Use system_profiler to list audio devices
    subprocess.run(["system_profiler", "SPAudioDataType"])


def main():
    parser = argparse.ArgumentParser(description="Dex TTS - text to speech announcements")
    parser.add_argument("text", nargs="*", help="Text to speak")
    parser.add_argument("-v", "--voice", default=DEFAULT_VOICE, help=f"Voice (default: {DEFAULT_VOICE})")
    parser.add_argument("-d", "--device", default=DEFAULT_DEVICE, help=f"Audio device ID (default: {DEFAULT_DEVICE})")
    parser.add_argument("--list-voices", action="store_true", help="List available voices")
    parser.add_argument("--list-devices", action="store_true", help="List audio devices")
    
    args = parser.parse_args()
    
    if args.list_voices:
        list_voices()
        return
    
    if args.list_devices:
        list_devices()
        return
    
    if not args.text:
        # Read from stdin if no text provided
        text = sys.stdin.read().strip()
    else:
        text = " ".join(args.text)
    
    if not text:
        print("[ERROR] No text provided", file=sys.stderr)
        sys.exit(1)
    
    success = speak(text, voice=args.voice, device=args.device)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
