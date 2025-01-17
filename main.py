import datetime as dt
import os
#import subprocess as sp
#import googlesearch
#import tkinter as tk
#import webbrowser
#import keyboard
import random

from conv import random_text
from text2speech import speak
from speech2text import commands
from coreAI import (
    wishings, time_today, date, updates, searchBrowser, start_command,
    region_check, num_articles_check, news
)
from paths import(
    YOUTUBE, CHROME, NOTEPAD, CMD, GMAIL
)

RESPECT = 'sir'

given_text = {
    "how are you",
    "i'm fine",
    "good",
    "good morning",
    "good evening",
    "what's the weather today",
    "what's the news",
    "what's the top news",
    "how's the internet",
    "open notepad",
    "open chrome",
    "open youtube",
    "open gmail",
    "open command prompt",
    "what's the time",
    "what's the date today",
    "what's the weather",
    "what's the news",
    "what's the top news",
    "what's the weather",
    "what's the news",
    "what's the top news",
    "what's the weather",
    "what's the news",
}

intro_text = [
    "hello",
    "hi",
    "hey",
    "howdy",
    "hey jarvis",
    "good morning jarvis",
    "good evening jarvis",
    "good afternoon jarvis"
]

agreeable_text = [
    "fine",
    "okay",
    "alright"
]

exit_text = [
    "bye",
    "goodbye",
    "see you later",
    "have a great day",
    "have a nice day",
    "have a good night",
    "mute jarvis"
]

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

#First it wishes
wishings()
time_today()
date()
updates()


#keyboard.add_hotkey('ctrl + alt + z', start_listening)
#keyboard.add_hotkey('ctrl + alt + shift', stop_listening)

while True:
    if listening:   #uses functions given above

        # query can be used as an audio from user
        query = commands().lower()
        start_command(query)
    
        #jarvis tells the time
        if "time" in query:
            strtime = dt.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is {strtime} {RESPECT}")       #responds to the user 
    
        #jarvis tells the date
        elif "date" in query:
            strdate = dt.datetime.now().strftime('%D')
            speak(f"today's date is {strdate} {RESPECT}")       #responds to the user

        #jarvis replying to a simple greeting
        elif "how are you" in query:
            speak("I'm doing great sir. what can I do for sir?")

        elif "who made you" in query:
            speak("Ravi, the prince of the Bhaskara Raju Vathsavai's family made me. I am grateful for being their assistant and will always help when needed")



        elif "go to the" or "open" or "in" in query:
            
            if "command prompt" in query:
                speak(random.choice(random_text))
                speak(f"Opening Command Prompt {RESPECT}...")
                os.system(CMD)
                speak("file opened")

                if "type" in query:
                    speak(f"Sorry {RESPECT}, I am not built for this function yet")
                    continue
                
        
            #elif "camera" in query:
            #    speak(f"Opening Camera, {RESPECT}")
            #    os.run('start microsoft.windows.camera', shell = True)  #uses shell interpretation to run the camera
                                                                        #with using the start command
            elif "notepad" in query:
                speak(random.choice(random_text))
                speak(f"Opening notepad {RESPECT}...")
                os.startfile(NOTEPAD)

                speak(f"Would you want me to type for you, {RESPECT}? ")
                search = commands().lower()
                if "no" in search:
                    continue
                elif "type" in search:
                    search = query.replace("type","").replace("Go to google" or "open google","")
                    searchBrowser(search)   
        
            elif "chrome" in query:
                speak(random.choice(random_text))
                speak(f"Opening google for you {RESPECT}...")
                os.startfile(CHROME)
                speak("file opened")
                
                speak(f"Would you like to search for anything, {RESPECT}? ")
                search = commands().lower()
                if "no" in search:
                    continue
                elif "search for" in search:
                    search = query.replace("search","").replace("Go to google" or "open google","")
                    searchBrowser(search)


            elif " Youtube" in query:
                speak(random.choice(random_text))
                speak(f"Opening google for you {RESPECT}...")
                os.startfile(YOUTUBE)
                speak("file opened")

                speak(f"What would you want me to search {RESPECT}?")
                search = commands().lower()

                if "search for" in search:
                    search = search.replace("go to youtube", "").replace(" and search for", "")
                    searchBrowser(search)
                elif "no" in search:
                    continue
            
            elif "gmail" in query:
                speak(f"Opening gmail for you {RESPECT}...")
                os.startfile(GMAIL)
                speak("file opened")
                
                speak(f"Would you like to search for anything, {RESPECT}? ")
                search = commands().lower()
                if "no" in search:
                    continue
                elif "search for" in search:
                    search = search.replace("go to gmail", "").replace(" and search for", "")
                    searchBrowser(search)
                
            elif "news" in query:
                speak(random.choice(random_text))
                while True:
                    country = region_check(query)

                    if None in country:
                        print("I don't have the region you specified sir")
                        continue

                    num_articles = num_articles_check(query)

                    if None in num_articles:
                        continue
    
                    if not given_text in query:
                        break

                    news(country, num_articles)

                continue
            
            
