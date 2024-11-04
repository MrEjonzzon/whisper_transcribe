# Setup and Use Whisper for Audio Transcription

Uses https://github.com/openai/whisper

## Prerequisites
Ensure Python (version 3.8 to 3.12) is installed on your system.

## Installation Steps
1. Open Command Prompt: Open your command prompt or terminal.
2. Navigate to Your Project Directory: `cd path\to\your\project\directory`
3. Create the Virtual Environment: `python -m venv whisper_env`
4. Activate the Virtual Environment: `whisper_env\Scripts\activate`
5. Install the Whisper Package: `pip install -U openai-whisper`
6. Install FFmpeg (required for handling audio files):
   - Ubuntu or Debian: `sudo apt update && sudo apt install ffmpeg`
   - Arch Linux: `sudo pacman -S ffmpeg`
   - MacOS (using Homebrew): `brew install ffmpeg`
   - Windows (using Chocolatey): `choco install ffmpeg`
   - Windows (using Scoop): `scoop install ffmpeg`

## Usage
- To transcribe all MP3 files in the directory, run `python batch_transcribe.py`.
- To transcribe a single audio file, use: `python -m whisper transcribe "filename.mp3" --model large`

## Troubleshooting
Please refer to Whisper's documentation

This guide has been also used: https://wandb.ai/wandb_fc/gentle-intros/reports/OpenAI-Whisper-How-to-Transcribe-Your-Audio-to-Text-for-Free-with-SRTs-VTTs---VmlldzozNDczNTI0
