import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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

    speak("I am friday Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        if(query=='Input' or query =='input' or query==None):
            query = input('Eenter Query: ')
        print(f"User said: {query}\n")

    except:
        # print(e)
        print("Say that again please...")  
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('user1@gmail.com', 'message')
    server.sendmail('user2@gmail.com', to, content)
    server.close()
user2_email='user2@gmail.com'
user3_email='user3@gmail.com'
#enter your own email...as per requirement.

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()'
        if query.endswith('wikipedia'):
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif query=='open youtube':
            webbrowser.open("youtube.com")

        elif query=='open google':
            webbrowser.open("google.com")

        elif query=='open stackoverflow':
            webbrowser.open("stackoverflow.com")   

        elif query=='play music':
            music_dir = 'path to music//music'#make a file in your drive and paste it here 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif query=='the time':
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif query=='open code' or query=='open vscode':
            codePath = 'path to file//vscode' #make a file in your drive and paste it here 
            os.startfile(codePath)

        elif query.startswith('email to '):
            if(query.endswith('user1') or query.endswith('user1') or query.endswith('user1')):
                receiver=user1_email
            else:
                receiver=user2_email
            try:
                speak("What should I say?")
                content = takeCommand()
                sendEmail(receiver, content)
                speak("Email has been sent to "+receiver)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif query.startswith('search') and (query.endswith('in google') or query.endswith('on google')):
            url="www.google.com/search?q="
            query=query[7:len(query)-10]
            for i in query:
                if(i!=" "):
                    url+=i
                else:
                    url+="+"
            print(url)
            webbrowser.open(url)
        elif query.startswith('search google for'):
            url="www.google.com/search?q="
            query=query[18:len(query)]
            for i in query:
                if(i!=" "):
                    url+=i
                else:
                    url+="+"
            print(url)
            webbrowser.open(url)

        elif query=='stop' or query=='exit' or query =='quit' or query=='chup':
            speak('See you soon!')
            print("See you soon!")
            exit()

        elif query.startswith('repeat after me '):
            repetation=query[15:len(query)]
            speak(repetation)

        elif query=='wait' or query=='delay' or query=='one moment':
            time.sleep(15)