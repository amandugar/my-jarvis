import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email import message


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

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
    speak("I am Jarvis Sir. Please tell me how may I help you...")

def takeCommand():
    #It takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 800
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(email,password,to,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (email, to, subject, content)
    server.sendmail(email,to,message)   


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on questions
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.in")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\indiAN\\Music'
            songs = os.listed(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is {strTime}")
        elif 'open visual studio code' in query:
            codePath = 'C:\\Users\\indiAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(codePath)
        elif 'open atom' in query:
            codePath = 'C:\\Users\\indiAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\Atom.lnk'
            os.startfile(codePath)
        elif 'open sublime' in query:
            codePath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk'
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("Type your Email: ")
                email = input()
                speak("Type your password: ")
                password = input("Type your pasword: ")
                speak("What Should be the subject: please speak it out")
                subject= takeCommand();
                speak("What Should I say")
                content = takeCommand();
                speak("To whom I should send")
                to = input()
                sendEmail(email,password,to,subject,content)

            except Exception as e:
                speak("Sorry my friend I am not able to send email")
            
        elif 'google search' in query:
            speak("What do you want to Search...? Please speak only query")
            query = takeCommand()
            webbrowser.open(f"https://www.google.com.tr/search?q={query}")
    
