# This code is only used to test what I learned

import os
#from groq import Groq
#import google.generativeai as genai
import webbrowser


#from apiKey import api_data
from speech2text import commands
from text2speech import speak


#os.startfile('chrome.exe')
#os.startfile('https://www.youtube.com/search?q=')



# Create a GenerativeAI client
#def reply(query):
#    client = Groq(api_key = api_data)
#    completion = client.chat.completions.create(
#        model="gemma2-9b-it",
#        messages=[
#            {
#                "role": "user",
#                "content": query
#            },
#        ],
#        temperature=1,
#        max_tokens=1024,
#        top_p=1,
#        stream=True,
#        stop=None,
#    )
#
#    answer = ""
#    for chunk in completion:
#        answer += chunk.choices[0].delta.content or ""
#    
#    return answer

#GENAI_API_KEY = api_data

#genai.configure(api_key = GENAI_API_KEY)

#def reply(query):
    # Create the model
#    generation_config = {
#    "temperature": 1,
#    "top_p": 0.95,
#    "top_k": 40,
#    "max_output_tokens": 8192,
#    "response_mime_type": "text/plain",
#    }
#
#    model = genai.GenerativeModel(
#      model_name="gemini-2.0-flash-exp",
#      generation_config=generation_config,
#    )
#
#    chat_session = model.start_chat(
#      history=[
#      ]
#    )
#
#    response = chat_session.send_message(query)
#
#   return response.text

# Testing the function
#if __name__ == '__main__':
#    answer = reply("what is a dragon")
#    speak(answer.replace("*", ""))

#def browserSearch(search):    
#    while True:
#        if "google" in search:
#            search.replace("google" or "in google", "")
#            if "exit browser" in search:
#                return "none"
#            speak(f"here is what I got about {search}")
#           search_url = f"https://www.google.com/search?q={search}"
#           webbrowser.open(search_url)
#       else:
#           speak(f"here is what I got about {search}")
#           search_url = f"https://www.google.com/search?q={search}"
#            webbrowser.open(search_url)
#            
#        search.commands().lower()
#
#        if "exit browser" in search:
#                return "none"


#if __name__ == '__main__':
#    browserSearch('what are dragons in google?')