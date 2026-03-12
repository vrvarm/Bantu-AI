from text2speech import speak
from speech2text import commands


from apiKey import (
    GENAI_API_DATA, API_DATA_GROQAI, NEWS_API_DATA
)

import pyautogui
import time
import os
import requests
import pywhatkit as kit
import datetime as dt

from groq import Groq



# function to wish the user based on the time of day
def wishings():
    hour = int(dt.datetime.now().hour)  #takes hours and uses it to tell the time

    # responds to the user with the appropriate greeting message based on the time of day
    if hour >= 0 and hour < 12:     # Morning
        speak('Good Morning Boss, this is jarvis how may I help you today')
    elif hour >= 12 and hour < 15:  # Afternoon
        speak('Good Afternoon Boss, this is jarvis how may I help you today')
    elif hour >= 15 and hour < 21:   # Evening
        speak('Good evening Boss, this is jarvis how may I help you today')
    else:                            # Night
        speak('Good Night Boss, this is jarvis how may I help you today')

def time_today():
    strtime = dt.datetime.now().strftime('%H:%M:%S')
    speak(f'The current time is {strtime}')

def date():
    strdate = dt.datetime.now().strftime('%D')
    speak(f'Today is {strdate}')

# function to handle the user's queries
def groqai_AI_voice(audio):
    client = Groq(api_key = API_DATA_GROQAI)
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "system",   # This is the role of the system (Jarvis AI)
                "content": "You are JARVIS, the artificial intelligence from Iron Man. You are intelligent, sophisticated, and always helpful. Respond in a professional and witty manner, similar to the character from the films."
            },
            {
                "role": "user",     # This is my role in the system 
                "content": audio
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
    
    return answer

def connectionCheck():
   try:
      response = requests.get('https://www.google.com')
      if response.status_code == 200:
            return True
      else:
          return False
   except requests.exceptions.RequestException:
       speak("Unable to connect to the internet, using groq AI sir")
       return False

def searchBrowser(search_term):

    os.system('start cmd')
    pyautogui.typewrite(search_term)

    # Wait for Discord to open
    time.sleep(5)

    # Press the Ctrl+K hotkey to open the search bar
    pyautogui.hotkey('ctrl', 'k')

    # Type the search term and press Enter
    pyautogui.typewrite(search_term)
    pyautogui.press('enter')

def start_command(strtcommand):
    if "unmute" in strtcommand:
        return True
    elif "mute" in strtcommand:
        return False
    else:
        return None


def updates():
    #jarvis will convey today's news and the classes that I have today
    speak("Today's news and classes are as follows:")
    DEFAULT_COUNTRY = 'us'
    news_url = f"https://newsapi.org/v2/top-headlines?country={DEFAULT_COUNTRY}&apiKey=" + NEWS_API_DATA

    # getting the url and storing it in json format
    news = requests.get(news_url).json()
    # printing the title of the articles
    articles = news['articles']

    news_articles = []
    for article in articles:
        news_articles.append(article['title'])
    
    for i in range(5):
        speak(news_articles[i])


