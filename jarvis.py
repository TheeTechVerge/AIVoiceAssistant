import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def greetings():
    speak("Welcome to the Tech Verge!")
    speak("the current time is")
    time()
    speak("The current date is")
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir, Welcome to the Tech Verge")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir, Welcome to the Tech Verge")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir, Welcome to the Tech Verge")

    else:
        speak("Good Night Sir, Welcome to the Tech Verge")
    speak("Jarvis at your service, PLease tell me how can I help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

    return query


takeCommand()
