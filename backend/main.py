import datetime as dt
import os
import googlesearch
import tkinter as tk
import webbrowser

from text2speech import speak
from speech2text import commands
from coreAI import (
    wishings, browserSearch, videosearch,
    browserOpen, reply
)

wishings()      #First it wishes 

while True:
    # query can be used as an audio from user
    query = commands().lower()

    if query =="none":
        continue
    
    #jarvis tells the time
    if "what's the time" in query:
        strtime = dt.datetime.now().strftime('%H:%M:%S')
        speak(f"Boss, the time is {strtime}")       #responds to the user 
    
    #jarvis tells the date
    elif "what's the date today" in query:
        strdate = dt.datetime.now().strftime('%Y-%m-%d')
        speak(f"Boss, today's date is {strdate}")       #responds to the user

    #jarvis replying to a simple greeting
    elif "how are you" in query:
        speak("I'm doing great Boss. How can I help you?")

    # jarvis open's a browser
    elif "open a browser" in query:

        #if any mistakes happen
        if "sorry" in query:
            speak("that is fine, sir")
            continue
        
        #either search or open browser
        if "search" or "search for" in query:
            browserSearch(query.replace("open a browser", "").replace("search" or "search for", ""))
        else:
            webbrowser.open("https://www.google.com")

    #elif "in youtube" or "in youtube search for" in query:
    #    speak("Opening YouTube to search what you requested boss")
    #    print("Bantu: Opening Google to search what you requested boss")
    #    videosearch(query.replace("in youtube" or "in youtube search for", ""))
    
    #elif "what is the weather today" in query:
    #    pass

    #elif "what's the news" in query:
    #    speak("Fetching latest news from newsapi.org")
    #    newsapi = NewsApiClient(api_key='YOUR_API_KEY')
    #    top_headlines = newsapi.get_top_headlines(country='us')
    #    for article in top_headlines['articles']:
    #        print(article['title'])
    
    #elif "open a video" in query:
    #    pass
    
    #elif "open a file" in query:
    #    pass
    
    #elif "play music" in query:
    #    pass
    
    #elif "open calculator" in query:
    #    pass

    #elif "open a word document" in query:
    #    pass
    
    #elif "open a powerpoint presentation" in query:
    #    pass
    
    #elif "open a picture" in query:
    #    pass
    
    #elif "open a program" in query:
    #    pass
    
    #elif "open a link" in query:
    #    pass
    
    #elif "open paint" in query:
    #    pass
    
    #elif "open notepad" in query:
    #    pass
    
    #elif "open powerpoint" in query:
    #    pass
    
    #elif "open excel" in query:
    #    pass
    
    #elif "open word" in query:
    #    pass
    
    #elif "open a document" or "open a file" in query:
    #    pass
    
    #elif "open a folder" in query:
    #    pass

    #elif 'I have a question' or 'I would like to ask you a question' in query:
    #    speak("Ask me any questions")
    #    question = commands().lower()
    #    reply(question)
    #    print("Program exited\n")

    if "thank you jarvis for helping" in query:
        speak("My pleasure, Sir")
        exit()
