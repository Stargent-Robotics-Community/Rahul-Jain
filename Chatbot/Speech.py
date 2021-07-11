import pyttsx3 
import pyaudio
import speech_recognition as sr
import webbrowser as web
import os

r = sr.Recognizer()
a = pyttsx3.init() 
def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print(":",end=" ")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        if text == "Rahul":
            stop = False   
        else:
            print("Sorry password did not match")    
            stop=True 
    except:
        print("speak again can't understand ") 

def chatBot(text):
            Answers = {"hello":"hi","how are you":"I'm doing fine. How are you?","bye":"Okay bye, Have a good day","open": "Open command started. What you want to open?","Google":"google.com","YouTube":"youtube.com","Gmail":"gmail.com","close":"Closing web browser"}
            a.say(Answers[text])
            a.runAndWait()
            return Answers[text]            
# Commands you can use are:
# hello
# how are you
# bye
# open
# (After open command) -> Google, YouTube, Gmail
# close -> close the web browser(only if internet explorer is default browser)

def main():
    stop = False
    website= False
    application= False
    print("Password", end="")
    start()
    while stop==False:      
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            print("You:" , end=" ")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            Answer = chatBot(text)
            print("Dude:",end=" ")
            print(Answer)
            if website==True:
                web.open(Answer)
                website= False
            if text == "open website":
                website= True
            if text == "open application":
                application= True
            if text == "bye":
                stop = True
            if text == "close":
                browserExe = "iexplore.exe" 
                os.system("taskkill /f /im "+browserExe)
        except:
            print("speak again can't understand ")
            y = input("Press n to stop listening")
            if y=="n":
                stop = True

main()



 