import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
import requests
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

client = genai.Client(
    api_key = gemini_key
)
recognizer = sr.Recognizer()


def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are Jarvis.
Reply in 1-2 short sentences only.
Keep answers concise and easy to speak.

User: {prompt}
"""
        )

        return response.text

    except Exception as e:
        print(e)
        return "Sorry, I couldn't answer."

def speak(text):
    print("Jarvis:", text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 220)
    engine.setProperty("volume", 1)

    engine.say(text)
    engine.runAndWait()

    del engine


def process_command(command):

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command.startswith("play"):

        song = command.replace("play", "").strip()

        if song in musiclib.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclib.music[song])

        else:
            speak("Song not found")
    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}")
        if r.status_code == 200:
            data = r.json()
            articles = data["articles"][:5]
            for i, article in enumerate(articles, 1):
                speak(f"News {i}: {article['title']}")

    elif "exit" in command:
        speak("Goodbye")
        return False

    else:
        response = ask_ai(command)
        speak(response)

    return True


speak("Initializing Jarvis")

while True:

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.energy_threshold = 300
            recognizer.dynamic_energy_threshold = False

            audio = recognizer.listen(source)

        wake = recognizer.recognize_google(audio).lower()

        print("Heard:", wake)

        if "jarvis" in wake:

            speak("Yes")

            with sr.Microphone() as source:

                print("Waiting for command")

                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()

            print(command)

            if not process_command(command):
                break

    except Exception as e:
        print("ERROR:", e)