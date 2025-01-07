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
def reply_groqai(query):
    client = Groq(api_key = API_DATA_GROQAI)
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


def news(region, num_articles):
    
    news_url = f"https://newsapi.org/v2/top-headlines?country={region}&apiKey=" + NEWS_API_DATA

    news = requests.get(news_url).json()
    articles = news['articles']

    news_articles = []
    for article in articles:
        news_articles.append(article['title'])
    
    if 'all' in num_articles:
        for i in range(len(articles)):
            print(news_articles[i])
    
    elif num_articles > 12:
        print("I'm sorry sir, but I can only display 12 articles at a time.")
        return
    
    elif num_articles < 1:
        print("I'm sorry sir, but you need to specify a number of articles.")
        return None
    
    else:
        for i in range(num_articles):
            print(news_articles[i])

def region_check(text):
    specific_word = {
        "us":"us",
        "germany":"de",
        "uk":"gb",
        "india":"in",
        "china":"cn",
        "australia":"au",
        "canada":"ca",
        "japan":"jp",
        "mexico":"mx",
        "russia":"ru",
        "default":"us"
    }

    for key in specific_word:
        if key in text:
            country = specific_word[key]
            break
    else:
        return None
    
    return country

def num_articles_check(text):

    num_of_articles = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'default': 5
    }

    for num in num_of_articles:
        if num in text:
            num_articles = num_of_articles[num]
            break
    else:
        num_articles = text

    return num_articles