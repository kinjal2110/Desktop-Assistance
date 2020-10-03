'''
It is desktop assistence named jenny.

'''

import pyttsx3      #need to install
import speech_recognition as sr   #need to install
import datetime
import pyaudio      #need to install for audio recognization
import wikipedia    #need to install
import webbrowser   #inbuilt module
import os
import random       #for play random songs
import smtplib      #for sending email

engine = pyttsx3.init('sapi5')      #for inbuild voice
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)    #for girl voice 1.id , for boy voice 0.id

def speak(audio):       #it will speak
    engine.say(audio)
    engine.runAndWait()

def wishMe():       #it will wish you on time using speak function.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:       #morning time
        speak("Good Morning")

    elif hour>=12 and hour<18:      #afternoon time
        speak("Good Afternoon")

    else:
        speak("Good Evening ")
    speak("I am jenny mam, Please tell me how may i help you?")      #i made assistent name jenny

def takeCommand():
    '''
    It takes microphone input from the user and returns string output.
    :return:
    '''

    r = sr.Recognizer()     #it will help you to recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said:{query}\n')

    except Exception as e:
       # print(e)

        print("Say that again Please")
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('suryavanshikinjal99@outlook.com','your password here')     #who you send email those id
    server.sendmail('suryavanshikinjal99@outlook.com',to ,content)
    server.close()




if __name__ == '__main__':
    #speak("Kinjal is a simple girl")
    wishMe()
    if 1:
        query = takeCommand().lower()  #speech to text work.
        # logic for executing task based on query
        if "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)     #if you ask 1 sentense then 1 sentense speak , if 2,3 as you want.
            speak("According to wikipedia ")
            speak(results)
            print(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.com')

        elif 'play music' in query:
            music_dir = "E:\\music\\New folder (2)"
            songs = os.listdir(music_dir)
            # random.shuffle(music_dir)
            r = random.choice(songs)
            os.startfile(os.path.join(music_dir,r))
            print(songs)
            # os.startfile(os.path.join(music_dir, songs[7]))     # also we can randomely song play

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H %M %S") #hour, minute, second
            speak(f' mam, the time is {strtime}')

        elif 'open Turbo C' in query: #not work
            tpath = "C:\\TURBOC3\\Turbo C++.exe"
            os.startfile(tpath)

        elif 'open code' in query:
            codepath = "C:\\Users\\Kinjal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'suryavanshikinjal99@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent! ")
            except Exception as e:
                print(e)
                speak("Sorry , my friend dear kinjal.. I am not able to send this email.")