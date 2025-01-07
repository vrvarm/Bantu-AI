from text2speech import speak
import speech_recognition as sr
import tkinter as tk
import random
from conv import random_text
import datetime as dt


# function used to change speech to text
def commands():
    r = sr.Recognizer() 

    # capture audio from the microphone and convert it to text. 
    # 1 second pause is used between each capture to allow the microphone 
    # to adjust to the ambient noise level.

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        r. adjust_for_ambient_noise (source, duration = 1)
        audio = r.listen(source)
    
    try: 
        print("Wait for few minutes ...\n")
        query = r.recognize_google(audio, language = 'en-in')   # The recognizer is configured to 
                                                                #understand the English language.
        print(f"Ravi: {query}\n")
        
        if "see you later" in query:
            hour = dt.datetime.now().hour
            if hour >= 20 and hour < 24:
                speak("Good Night, sir")
            else:
                speak("have a great day, sir")

            exit()
    
    except Exception as e:  #Captures errors 
        print(e)
        speak("Sorry, I couldn't hear you boss. Repeat what you said? ")
        query = "none"
    
    return query