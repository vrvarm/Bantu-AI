import os
from dotenv import load_dotenv
from tool_registry import function_tool
import requests


load_dotenv(".env.local")

NEWS_API_KEY = os.getenv("NEWS_API_DATA")

if not NEWS_API_KEY:
    raise ValueError("Missing NEWS_API_KEY in environment variables.")

# NEWS Tool 
@function_tool(
    description="Get top news headlines for a region.",
    parameters={
        "type": "object",
        "properties":{
            "region":{"type":"string"},
            "num_articles":{"type":"integer"}
        },
        "required":["region"]
    }
)

def news(region, num_articles: int):
    country = region_check(region)
    num_articles = num_articles_check(num_articles)
    
    if not country:
        country = "us" # fall back to the default Location

    news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"

    try:
        news = requests.get(news_url).json()
        data = news.json()

        if data.get("status") != "ok":
            return " Sorry, I couldn't fetch the news right now."

        articles = data.get("articles", [])

        if not articles:
            return "No news articles found"

        news_articles = min(num_articles, len(articles))
        
        headlines = [
            f"{i + 1}. {articles[i]["title"]}"
            for i in range(num_articles)
        ]

        return "\n".join(headlines)
        
    except Exception as e:
        return f"Error fetching news: {str(e)}"

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

    text = text.lower()

    for key in specific_word:
        if key in text:
            return specific_word[key]
            
    else:
        return "us"

def num_articles_check(num: int):
    try:
        return num
    except:
        return 5