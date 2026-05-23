# MegaJarvis

MegaJarvis is a simple voice-controlled assistant built in Python. It listens for the wake word `jarvis`, accepts spoken commands, and can open websites, play songs from a predefined music library, fetch news headlines, and answer general questions via Gemini AI.

## Features

- Voice recognition using `SpeechRecognition`
- Text-to-speech replies using `pyttsx3`
- Website launching for Google and YouTube
- Music playback via YouTube links from `musiclib.py`
- News headlines using NewsAPI
- AI question answering via Google Gemini generative AI

## Files

- `main.py` - Main application entrypoint and command processing logic.
- `musiclib.py` - Simple music library mapping song names to YouTube URLs.
- `requirements.txt` - Python dependencies required to run MegaJarvis.

## Setup

1. Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   NEWS_API_KEY=your_newsapi_api_key
   ```

## Usage

Run the assistant from the project root:
```powershell
python main.py
```

Speak clearly and say `jarvis` first to wake the assistant. After the wake word, give commands such as:

- `open youtube`
- `open google`
- `play shape of you`
- `news`
- `exit`

## Customizing Music

Add or update songs in `musiclib.py` using the `music` dictionary. Keys are song names, and values are YouTube URLs.

## Notes

- Make sure your microphone is enabled and accessible.
- The assistant uses Google Speech Recognition via the default recognizer.
- The current AI support is configured for Google Gemini and requires a valid API key.
