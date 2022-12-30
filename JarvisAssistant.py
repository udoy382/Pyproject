import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import pyjokes
from bs4 import BeautifulSoup
import speech_recognition as sr
from pynput.keyboard import Key, Controller
from pywikihow import search_wikihow
from time import sleep
import datetime
import requests
import random
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('Hi! I am Jarvis. Please tell me how may I help you.')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('🤖 Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('🤖 Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please.')
        return "None"
    
    return query


def searchGoogle(query):
    if "search" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("search on google", "")
        query = query.replace("search in google", "")
        query = query.replace("google search", "")
        query = query.replace("search google", "")

        speak("This is what I found on google!")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("No speakable output available.")


def searchYoutube(query):
    if "play" in query:
        speak("This is what I found on youtube!")
        query = query.replace("jarvis", "")
        query = query.replace("play", "")
        query = query.replace("youtube", "")
        query = query.replace("play on youtube", "")
        query = query.replace("play in youtube", "")
        query = query.replace("play youtube", "")
        query = query.replace("youtube play", "")

        web = f"https://www.youtube.com/results?search_query={query}"

        speak('playing' + query)
        webbrowser.open(web)
        pywhatkit.playonyt(query)


keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


propose_ = [
    "The best place for me is in your Heart I know there is no better place for me so can you be the love of my life? In you I have found the one I was looking for my heart now longs to propose you my love. This proposal Day, I want to say will you be mine?",
    "I can win the world with my hand, only if you promise me to hold my other hand, for a lifetime!!",
    "I want to walk with you, I want to talk with you.",
    "Truth is if I could be with anyone, I would still choose you. Please be mine till eternity!",
    "They filled my days with your laughter, and I filled my heart with your thoughts. Promise me we will be together forever because I love you!"
]

replay_propose_ = [
    "Your love is truly a wonderful gift for me. I can never think of anyone else who could love me so deeply!",
    "I promise I will be with you in every condition and I will support in difficulties of your life.",
    "You are like the sunshine so warm. Also, you are like sugar, so sweet. You are like you and thats the reason I love you definitely.",
    "You are just so beautiful, both inside and outside. I must be so lucky that I could find you in this big world and make you mine.",
    "You are the bright sunshine in my overcast life. Can you stay with me forever?"
]

do_you_love_me_ = [
    "I love you very much, probably more than anybody could love another person.",
    "I'll love you until time runs out.",
    "I love you so much, sometimes too much.",
    "I love you from here to the end of the universe.",
    "I love you like the earth loves the sun."
]

how_much_do_you_love_me_ = [
    "My love for you is as big as the universe.",
    "A little more every day.",
    "You'll never believe how much.",
    "More than you love me!",
    "More than you can imagine."
]


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching from Wikipedia.')
            query = query.replace('jarvis', "")
            query = query.replace('wikipedia', "")
            query = query.replace('search in wikipedia', "")
            query = query.replace('search wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'hi' in query:
            speak('Hi! How can I help you today?')
        
        elif 'hello' in query:
            speak('Hello! How can I help you today?')

        elif 'assistant' in query:
            speak("Yes, I am the Assistant. How can I help you today?")

        elif "i am fine" in query  or "i am good" in query or "i am great" in query or "i am awesome" in query  or "i am cool" in query or "i am perfect" in query:
            speak("That's great!")
        
        elif 'how are you' in query:
            speak("As an artificial intelligence, I don't have feelings or emotions in the same way that humans do. However, I am programmed to assist and support users to the best of my abilities. Is there something specific you would like to know or discuss?")

        elif 'bye' in query or 'goodbye' in query:
            speak("Goodbye! If you have any further questions or need any additional assistance, please don't hesitate to reach out. I'm here to help.")

        elif 'exit' in query:
            speak("Sure, sir.")
            break

        elif 'i am back' in query or 'i am come back' in query or 'i am come back again' in query:
            speak("I'm glad you're back! Is there something specific you would like to ask or discuss? I'm here to help answer any questions you might have or provide information on a wide range of topics. Please let me know how I can assist you.")

        elif "your name" in query or "what's your name" in query:
            speak("I am an artificial intelligence assistant. I don't have a personal name like a human, but you can call me Jarvis.")

        elif 'help me' in query:
            speak("Of course, I'd be happy to help! Please let me know what you need.")

        elif 'where am i' in query or 'where am i located' in query or 'what is my location' in query:
            speak("I'm sorry, but I don't have access to information about your physical location. AS an artificial intelligence, I don't have the ability to see or interact with the physical world in the same way that humans do.")
        
        elif 'thank you' in query:
            speak("You're welcome!")

        elif 'prime minister of bangladesh' in query:
            speak('The current prime minister, Sheikh Hasina, was appointed on 6 January 2009 by the President of Bangladesh, and she is also the longest serving prime minister in the country and still is.')
        
        elif 'president of bangladesh' in query:
            speak('Mohammad Abdul Hamid (born 1 January 1944) is a Bangladeshi politician who is currently serving as the president of Bangladesh. He was elected to his first term in April 2013,[1] and re-elected to his current second term in 2018.')

        elif 'made you' in query or 'build you' in query or 'create you' in query:
            speak("I was created by a team of researchers and programmers at J K and H K Science Club")

        elif 'which programming language is used for AI' in query:
            speak('Python, Java, R. This programming language is used for AI.')
        
        elif 'our team member' in query or 'what is our team member' in query:
            speak('Udoy, Yusuf, Soykot. They are the member of our team.')

        elif 'our club name' in query:
            speak('J K and H K science club') 

        # --------------

        elif 'sweetest language in the world' in query:
            speak('according to a UNESCO, bengali has been classified as the sweetest language in the world.')

        elif 'capital of bangladesh' in query:
                    speak('dhaka, also spelled dacca, city and capital of bangladesh')

        elif 'where are we now' in query:
                    speak('In Habiganj')

        elif 'say hello' in query:
                    speak('assalamu alaikum... how are you?')

        elif 'tell me about your self' in query:
                    speak('now me to introduce myself, i am jarvis.. the virtual artificial intelligence.. and i am here  to assist you with a variety of tasks as best i can 24 hours a day seven days a week importing all preferences from home interface systems are now fully operational you...')

        elif 'location of habiganj?' in query:
                    speak('habiganj is a district in northeastern  bangladesh.. it is part of the sylhet division.')

        elif 'what is habiganj khown for?' in query:
                    speak('habiganj district is located in the sylhet division. it is a historic place where freedom fighters started the first guerrilla movement against the pakistan army during the bangladesh liberation war.')

        elif 'district commissionar of habiganj' in query:
                    speak('israt jahan is the district commissioner of habiganj!')

        elif 'who made you' in query:
                    speak('Saifur Rahman Udoy made me.')


        # ---------------
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'school name' in query:
            speak('School name is, J K and H K High School and College')

        elif 'science teacher' in query:
            speak('our teacher name is, motior sir, kamal sir, kamrul sir, sumsuddin sir.')

        elif 'headmaster' in query:
            speak(' Our headmaster name is, Abul Hasan sir.')

        elif 'who are you' in query or 'about yourself' in query or 'who you are' in query:
            speak("now me to introduce myself, I am Jarvis. The virtual artificial intelligence, and I am here to assist you with a variety of tasks as best I can. 24 hours a day, seven days a week, importing all preferences from home interface. Systems are now fully operational!")

        elif 'propose' in query:
            x = random.choice(propose_)
            speak(x)
        
        elif 'i love you' in query or 'love you' in query:
            y = random.choice(replay_propose_)
            speak(y)

        elif 'do you love me' in query or 'love me' in query:
            doYouLoveMe = random.choice(do_you_love_me_)
            speak(doYouLoveMe)

        elif 'how much do you love me' in query or 'how much you love me' in query:
            howMuchDoYouLoveMe = random.choice(how_much_do_you_love_me_)
            speak(howMuchDoYouLoveMe)

        elif 'father of nation' in query or 'who is father of nation' in query:
            speak('In 2011, the 15th constitutional amendment in Bangladesh referred to Sheikh Mujib as the Father of the Nation who declared independence; these references were enshrined in the fifth, sixth, and seventh schedules of the constitution.')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
    
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open education board bangladesh' in query:
            webbrowser.open('http://www.educationboard.gov.bd/')

        elif 'activate how to do mod' in query:
            speak('How to do mode is activated.')
            while True:
                speak('Please tell me what you want to know.')
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay, how to do mode is closed.")
                        break
                    else:
                        max_results = 1
                        how = takeCommand()
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry, I am not able to find this.")
    
        elif 'search' in query:
            searchGoogle(query)
        
        elif 'play' in query:
            searchYoutube(query)
        
        elif 'pause' in query:
            pyautogui.press("k")
            speak('video paused')
    
        elif 'unpause' in query:
            pyautogui.press("k")
            speak('video played')

        elif 'mute' in query:
            pyautogui.press("m")
            speak('video muted')

        elif 'volume up' in query:
            speak('Turning volume up')
            volumeup()

        elif 'volume down' in query:
            speak('Turning volume down')
            volumedown()

        elif 'temperature' in query:
            search = "temperature in Habiganj"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'weather' in query:
            search = "weather in Habiganj"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {strTime}")

        elif 'date' in query:
            date = datetime.date.today()
            speak(f"The current date is {date}")
    
        elif 'code' in query:
            path = "C:\\Users\\singe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
    
        elif 'chrome' in query:
            path = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        else:
            print("I'm sorry, but I'm not able to understand your message. Could you please provide more context or clarify your question?")
            speak("I'm sorry, but I'm not able to understand your message. Could you please provide more context or clarify your question?")