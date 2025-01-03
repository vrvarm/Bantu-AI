from text2speech import speak
from speech2text import commands


from apiKey import (
    GENAI_API_DATA, API_DATA_GROQAI
)

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

def browserSearch(query):
    kit.search(query)

def videoSearch(video):
    kit.playonyt(video)


#def imagesearch(image):
#    pass

#def weather(location):
#    pass

#def translate(text, language):
#    pass


