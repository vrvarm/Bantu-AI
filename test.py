# This code is only used to test what I learned

import os
from groq import Groq
import google.generativeai as genai
#import webbrowser
import pywhatkit as kit
import requests


from apiKey import (
    GENAI_API_DATA, API_DATA_GROQAI
)
from speech2text import commands
from text2speech import speak


#os.startfile('chrome.exe')
#os.startfile('https://www.youtube.com/search?q=')



# Create a GenerativeAI client
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


if __name__ == '__main__':
   #videoSearch('what are dragons?')
    if connectionCheck():
        answer = reply_groqai('what are dragons')
        print(answer.replace("*", ""))
    else:
        print("unable to connect internet sir")
