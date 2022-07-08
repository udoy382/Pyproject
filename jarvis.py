import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
## print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
    else:
        print("Good Evening")

    speak("I am Jarvis sir. Please tell me how how may I help you")

def takeCommand():
    # it takes microphone input from the user and returns starting output

    # r = sr.Recognizer()
    r = sr.Recognizer()
    with sr.Microphone() as source:
       audio = r.listen(source)

    try:
        print("Recognizing...")
        quary = r.recognize_google(audio, language='en-in')
        print(f"User said: {quary}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return quary

if __name__ == '__main__':
    wishMe()
    while True:
        quary = takeCommand().lower()

    # logic for executing tasks bases on query
    if 'wikipedia' is quary:
        speak('Searching Wikipedia...')
        quary = quary.replace("wikipedia", "")
        results = wikipedia.summary(quary, sentences=2)
        speak("According to wikipesia")
        print(results)
        speak(results)

    elif 'open youtube' in quary:
        webbrowser.open("youtube.com")

    elif 'open google' in quary:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in quary:
        webbrowser.open("stackoverflow.com")
    