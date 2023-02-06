import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os

print("Jerry talk...")
MASTER = "irfan"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
#kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
#jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        talk("Hello Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        talk("Hello Good Afternoon" + MASTER)
    else:
        talk("Hello Good Evening" + MASTER)

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "jerry" in command:
                print(command)
                command = command.replace("jerry", "")
                talk(command)
                
    except:
        pass

    return command


def run_jerry():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("playing"+ song)
        print("playing"+ song)
        pywhatkit.playonyt(song)
    elif "who are you" in command:
        print("I am jerry, your virtual assistant "+ MASTER)
        talk("I am jerry, your virtual assistant "+ MASTER)
    elif "open calculator" in command:
        talk("Ok, calculator is being on")
        os.system("calc")
    elif "close calculator" in command:
        talk("Ok, calculator will be closed")
        os.system("taskkill /F /IM CalculatorApp.exe")
    elif "open file" in command:
        talk("Ok, file explorer is being on")
        os.system("explorer")
    elif "open cmd" in command:
        talk("Ok, cmd is being on")
        os.system("cmd")
    elif "close cmd" in command:
        talk("Ok, cmd is being close")
        os.system("taskkill /F /IM cmd.exe")
    elif "open notepad now" in command:
        talk("Ok, notepad is being on")
        os.system("notepad")
    elif "close notepad" in command:
        talk("Ok, notepad is being close")
        os.system("taskkill /F /IM notepad.exe")
    elif "thank you" in command:
        print("you're welcome")
        talk("you're welcome")
    elif "close program" in command:
        print("Ok, good bay " + MASTER)
        talk("Ok, good bay " + MASTER)
        os.system("cmd")
    elif "clean up" in command:
        talk("Ok")
        os.system("cls")
        print("the command has been removed")
        talk("the command has been removed")
    elif "what the time now" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("time now is "+ time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("searching wikipedia")
        print(info)
        talk(info)
    else:
        talk("not any intruction")
        print(command)
wishMe()

while True:   
    MASTER = "irfan"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    #kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    #jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    talk("I am jerry what do you want")
    run_jerry()