import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('yes, I am single, for you')
    elif 'do you love me' in command:
        talk('yes, I love you')
    elif 'who am i' in command:
        talk('you are Saifur Rahman Udoy')
    elif 'propose me' in command:
        talk('I love you')
    elif 'do you merry me' in command:
        talk('sure I will merry you')
    elif 'who are you' in command:
        talk('im you assistant alexa')
    elif 'who are you' in command:
        talk('Hi! I am Alexa')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        exit()
    else:
        talk('Please say the command again.')
while True:
    run_alexa()