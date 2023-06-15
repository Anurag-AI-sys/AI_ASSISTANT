import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am NRG Sir. How may I help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('my-email ID', 'my-password')
    server.sendmail('my email-ID', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()



        if 'open youtube' in query:
            speak("Opening youtube sir...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google sir...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stack overflow sir...")
            webbrowser.open("stackoverflow.com")


        elif 'open music' in query:
            music_dir = "D:\MOVIES"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email to father' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's-emailID"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend.I am not able to send this email")