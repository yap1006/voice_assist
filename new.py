import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5') #The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications. To date, a number of versions of the API have been released, which have shipped either as part of a Speech SDK or as part of the Windows OS itself.
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id) #to set voice pf your choice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("guten morgen or good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am your personal bot YAP sir. please tell me how may i help")    

def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer() # this class will help us in recognising audio
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1   # this will help in taking pause while speaking so that it doesnt complete while we take a pause
        audio = r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")  
    except Exception as e:
        #print(e)
        print("say that again pls....")
        return "None"
    return query
def sendemail(to,content):  #allow less secure apps in your pc for it to work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yash196000@gmail.com','sryp@2017')
    server.sendmail('yash196000@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    #wishMe()
    while True:
    #if 1: 
        query=takeCommand().lower() 
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2) #it will return 2 sentences from wikipedia
            speak("according to wikipedia")
            speak(results)  
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"your time is {strtime}")
        elif 'open code' in query:
            cpath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)
        elif 'send email' in query:
            try:
                speak("say what you want?")
                content=takeCommand()
                to="yash196000@gmail.com"
                sendemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry we are unable to send email at the moment...")
        elif 'quit' in query:
            exit()

            

            


    
    #logic for executinng task based on query
   
    