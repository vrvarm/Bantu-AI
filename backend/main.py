import datetime as dt
import os
import googlesearch

from text2speech import speak
from speech2text import commands
from coreAI import (
    wishings, browserSearch, videosearch,
    browserOpen
)

wishings()      #First it wishes 

while True:
    # query can be used as an audio from user
    query = commands().lower()

    # Wishing the user
    if "what's the time" in query:
        strtime = dt.datetime.now().strftime('%H:%M:%S')
        print(strtime)
        speak(f"Boss, the time is {strtime}")       #responds to the user
        query = ""  #resets variable to redo audio 
        

    elif "how are you" in query:
        speak("I'm doing great Boss. How can I help you?")
        query = ""

    elif "in google" or "in google search for" in query:
        speak("Opening Google to search what you requested boss")
        browserSearch(query.replace("in google" or "in google search for", ""))
        query = ""

    elif "in youtube" or "in youtube search for" in query:
        speak("Opening YouTube to search what you requested boss")
        print("Bantu: Opening Google to search what you requested boss")
        videosearch(query.replace("in youtube" or "in youtube search for", ""))
        query = ""

    elif "Open browser" in query:
        speak("Opening Default Browser...")
        browserOpen(query)
        query = ""
    
    #elif "what is the weather today" in query:
    #    pass

    elif "bye bantu" in query:
        print("Bantu: Goodbye boss! Have a great day")
        speak("goodbye boss  have a great day")
        query = ""
        exit()
