from text2speech import speak
from speech2text import commands
import datetime as dt
import os
import googlesearch

# function to wish the user based on the time of day
def wishings():
    hour = int(dt.datetime.now().hour)  #takes hours and uses it to tell the time

    # responds to the user with the appropriate greeting message based on the time of day
    if hour >= 0 and hour < 12:     # Morning
        print('Good Morning Boss, how may I help you today')
        speak('Good Morning Boss, how may I help you today')
    elif hour >= 12 and hour < 17:  # Afternoon
        print('Good Afternoon Boss, how may I help you today')
        speak('Good Afternoon Boss, how may I help you today')
    elif hour >= 17 and hour < 21:   # Evening
        print('Good evening Boss, how may I help you today')
        speak('Good evening Boss, how may I help you today')
    else:                            # Night
        print('Good Night Boss, how may I help you today')
        speak('Good Night Boss, how may I help you today')

# function to search for information on Google
def browserSearch(search):
    results = list(googlesearch.search(search, stop = 1))
    if results:
        os.startfile(results[0])
        speak("According to google, ")
        speak(results)
    else:
        speak("No results found for your query boss")

# functions to open different browsers, videos, and images
def videosearch(video):
    os.startfile("https://www.youtube.com/search?q={video}")
    speak("I have opened a video search for you boss")
    print("I have opened a video search for you boss")

def browserOpen(browser):
        os.startfile('chrome.exe')

#def imagesearch(image):
#    pass

#def weather(location):
#    pass

#def translate(text, language):
#    pass

