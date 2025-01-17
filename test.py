# This code is only used to test what I learned

import datetime as dt
import os
import subprocess as sp
import googlesearch
import tkinter as tk
import requests
import keyboard
import groq
import re


from text2speech import speak
from speech2text import commands
#from coreAI import (
#    reply_groqai
#)
from paths import(
    CHROME
)

import google.generativeai as genai
import webbrowser
import pywhatkit as kit
import requests


from apiKey import (
    GENAI_API_DATA, API_DATA_GROQAI, NEWS_API_DATA, TEXT_TO_SPEECH
)
from speech2text import commands
from text2speech import speak


#os.startfile('chrome.exe')
#os.startfile('https://www.youtube.com/search?q=')



# Create a GenerativeAI client
def reply_groqai(query):
    client = groq(api_key = API_DATA_GROQAI)
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "system",
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

genai.configure(api_key = GENAI_API_DATA)

def reply_genai(query):
    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash-exp",
      generation_config=generation_config,
    )

    chat_session = model.start_chat(
      history=[
      ]
    )

    response = chat_session.send_message(query)

    return response.text

# Testing the function
#if __name__ == '__main__':
#    answer = reply("what is a dragon")
#    speak(answer.replace("*", ""))

def connectionCheck():
   try:
      response = requests.get('https://www.google.com')
      if response.status_code == 200:
          return True
      else:
          return False
   except requests.exceptions.RequestException:
       print("Unable to connect to the internet, using groq AI sir")
       return False
       


#def browserSearch(query):
#    kit.search(query)

#def videoSearch(video):
#    kit.playonyt(video)


import time
import pyautogui

def search(search_term):

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

from elevenlabs import play
from elevenlabs.client import ElevenLabs

def speak_labs(text):

    client = ElevenLabs(
        api_key= "sk_38da82fc241ba48280d3a3756b0bc55083a5459a524a7488",
    )
    
    audio = client.text_to_speech.convert(
    voice_id= "JBFqnCBsd6RMkjVDRZzb",
    model_id= "eleven_turbo_v2_5",
    text = text,
    )

    #audio = client.generate(
    #    voice= "George",
    #    model= "eleven_turbo_v2_5",
    #    text = text
    #)

    play(audio)



# Testing the function
if __name__ == '__main__':
    print("hello, how may I help you sir")


#if __name__ == '__main__':
   #print(start_command('stop'))
   #print(reply_groqai('hello'))
   #updates()
   #latest_news()
   #speak_labs()
      
# Example usage
#text = input("May I know how many articles you would like to know and what region do you want sir? ")

#while True:
#    country = region_check(text)

#    if None in country:
#        print("I don't have the region you specified sir")
#        continue
#
#    num_articles = num_articles_check(text)

#    if None in num_articles:
#        continue
#    
#    if not given_text in text:
#        break

#    news(country, num_articles)

#continue

   
