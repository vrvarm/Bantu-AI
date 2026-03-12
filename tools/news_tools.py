import os
from dotenv import load_dotenv
from tool_registry import function_tool
import requests


load_dotenv(".env.local")

NEWS_API_KEY = os.getenv("NEWS_API_DATA")

if not NEWS_API_KEY:
    raise ValueError("Missing NEWS_API_KEY in environment variables.")

@function_tool(
    description="Displays the number of News article titles based on the region and the number of articles given by the user.",
    parameters={
        "type": "object",
        "properties":{
            "region":{"type":"string"},
            "num_articles":{"type":"string"}
        },
        "required":["region","num_articles"]
    }
)
def news(region, num_articles):
    country = _region_check(region)
    num_articles = _num_articles_check(num_articles)

    news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=" + NEWS_API_KEY

    news = requests.get(news_url).json()
    articles = news['articles']

    news_articles = []
    for article in articles:
        news_articles.append(article['title'])

    for i in range(num_articles):
        print(news_articles[i])

def _region_check(text):
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

def _num_articles_check(text):

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