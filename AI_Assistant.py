import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-US")
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't understand that.")
        return ""

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. Ask me anything.")

def handle_query(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Here’s what I found on Google.")
    return True

def main():
    greet()
    while True:
        q = get_audio()
        if any(x in q for x in ["exit", "bye", "quit"]):
            speak("Goodbye.")
            break
        if q:
            handle_query(q)

if __name__ == "__main__":
    main()
