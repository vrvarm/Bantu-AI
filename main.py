import datetime as dt
import os
import subprocess as sp
import googlesearch
import tkinter as tk
import webbrowser
import keyboard


from text2speech import speak
from speech2text import commands
from coreAI import (
    wishings, browserSearch, videoSearch,
    connectionCheck, reply_groqai
)
from paths import(
    NOTEPAD, CHROME, DISCORD, COPILOT,
    NOTES, 
)

RESPECT = 'sir'

#when a key combination is typed, it starts listening
listening = False

def start_listening():
    global listening    
    listening = True
    print("started listening")

def stop_listening():
    global listening
    listening = False
    print("stopped listening")

keyboard.add_hotkey('ctrl + alt + z', start_listening)
keyboard.add_hotkey('ctrl + alt + shift', stop_listening)       

#First it wishes
wishings()

while True:
    if listening:   #uses functions given above

        # query can be used as an audio from user
        query = commands().lower()
    
        #jarvis tells the time
        if "what's the time" in query:
            strtime = dt.datetime.now().strftime('%H:%M:%S')
            speak(f"Boss, the time is {strtime}")       #responds to the user 
    
        #jarvis tells the date
        elif "what's the date today" in query:
            strdate = dt.datetime.now().strftime('%D')
            speak(f"Boss, today's date is {strdate}")       #responds to the user

        #jarvis replying to a simple greeting
        elif "how are you" in query:
            speak("I'm doing great Boss. How can I help you?")

        elif "who made you" in query:
            speak("Ravi, the prince of the Bhaskara Raju Vathsavai's family made me. I am grateful for being their assistant and will always help when needed")

        elif "open command prompt" in query:
            speak(f"Opening Command Prompt {RESPECT}...")
            os.system('start cmd')
        
        elif "open camera" in query:
            speak(f"Opening Camera, {RESPECT}")
            os.run('start microsoft.windows.camera', shell = True)  #uses shell interpretation to run the camera
                                                                    #with using the start command
        elif "open notepad" in query:
            speak(f"Opening notepad {RESPECT}...")
            os.startfile('NOTEPAD')
        
        elif "open discord" in query:
            speak(f"Opening Discord for you {RESPECT}...")
            os.startfile(DISCORD)
        
        elif "open google" in query:
            speak(f"Opening google for you {RESPECT}...")
            os.startfile(CHROME)

        elif "Go to youtube" or "in Youtube" in query:
            if " and search for" in query:
                search = query.replace("go to youtube", "").replace(" and search for", "")
                videoSearch(search)
            else:
                speak("What would you want me to search sir?")
                search = commands().lower()
                videoSearch(search)
        
        elif "Go to google" or "In google" in query:
            if "and search for" or "search for" in query:
                search = query.replace("search for" or "and search for","").replace("Go to google" or "In google","")
                browserSearch(search)
            else:
                speak("What would you want me to search sir?")
                search = commands().lower()
                videoSearch(search)
        
        elif "search for" in query:
            if connectionCheck():
                answer = reply_groqai('what are dragons')
                print(answer.replace("*", ""))
            else:
                continue
        
