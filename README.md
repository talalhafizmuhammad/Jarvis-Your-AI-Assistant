# 🤖 Jarvis Voice Assistant

A lightweight, offline-capable Python voice assistant that listens to your commands, speaks back answers, and intelligently searches Wikipedia or Google when needed.

---

## ✨ Features

- 🎙️ **Voice Input:** Uses your microphone to understand spoken commands.
- 📚 **Wikipedia Search:** Retrieves concise summaries from Wikipedia.
- 🔎 **Fallback to Google:** Opens browser search results when Wikipedia fails.
- 🗣️ **Text-to-Speech:** Replies to you with a human-like voice.
- ⏰ **Time-Aware Greetings:** Greets you based on the time of day.
- 🔁 **Continuous Listening:** Listens in a loop until you say "exit", "quit", or "bye".

---

## 📦 Requirements

Install the required Python modules:

```bash
pip install speechrecognition
pip install pyttsx3
pip install wikipedia
pip install pipwin && pipwin install pyaudio         # Windows
sudo apt install portaudio19-dev python3-pyaudio     # Linux
