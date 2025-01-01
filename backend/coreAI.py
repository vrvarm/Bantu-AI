from text2speech import speak
from speech2text import commands
from apiKey import api_data



import os
import webbrowser
import datetime as dt
import googlesearch
from groq import Groq



# function to wish the user based on the time of day
def wishings():
    hour = int(dt.datetime.now().hour)  #takes hours and uses it to tell the time

    # responds to the user with the appropriate greeting message based on the time of day
    if hour >= 0 and hour < 12:     # Morning
        speak('Good Morning Boss, how may I help you today')
    elif hour >= 12 and hour < 17:  # Afternoon
        speak('Good Afternoon Boss, how may I help you today')
    elif hour >= 17 and hour < 21:   # Evening
        speak('Good evening Boss, how may I help you today')
    else:                            # Night
        speak('Good Night Boss, how may I help you today')


# function to handle the user's queries
def reply(query):
    while True:
        client = Groq(api_key = api_data)
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "user",
                    "content": query
                },
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        answer = ""
        for chunk in completion:
            answer += chunk.choices[0].delta.content or ""
    
        speak(answer)

        query = commands().lower()

        if "exit query" in query:
            speak("Exiting sir...")
            return 'none'



# function to search for information on Google
def browserSearch(search):    
    while True:
        if "google" in search:
            search.replace("google" or "in google", "")

            #exit's browser when commanded
            if "exit browser" in search:
                os.system("taskkill /im chrome.exe /f")
                return "none"
            
            speak(f"here is what I got about {search}")
            search_url = f"https://www.google.com/search?q={search}"
            webbrowser.open(search_url)
        else:
            speak(f"here is what I got about {search}")
            search_url = f"https://www.google.com/search?q={search}"
            webbrowser.open(search_url)
        
        speak("what else do you want to search")
        search.commands().lower()

        #exists the function with this reply
        if "nothing else" in search:
                return "none"
    

# functions to open different browsers, videos, and images
def videosearch(video):
    os.startfile("https://www.youtube.com/search?q={video}")
    speak("I have opened a video search for you, sir")

#def imagesearch(image):
#    pass

#def weather(location):
#    pass

#def translate(text, language):
#    pass


