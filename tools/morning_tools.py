import os
import requests
import datetime as dt
from dotenv import load_dotenv
from tool_registry import function_tool

load_dotenv(".env.local")

NEWS_API_KEY = os.getenv("NEWS_API_DATA")
WEATHER_API_KEY = os.getenv("WEATHER_API_DATA")


@function_tool(
    description="Provides a full morning briefing including news, weather, music, calendar events, and assignments.",
    parameters={
        "type": "object",
        "properties": {
            "city": {"type": "string"}
        },
        "required": []
    }
)
def morning_briefing(city: str = "Dallas"):

    output = []

    # ── GREETING ─────────────────────────────
    hour = dt.datetime.now().hour
    if hour < 12:
        output.append("Good morning, sir.")
    elif hour < 18:
        output.append("Good afternoon.")
    else:
        output.append("Good evening.")

    output.append("Here are your updates for today.")

    # ── NEWS ────────────────────────────────
    output.append("Here are today's top headlines:")

    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    news = requests.get(news_url).json()
    articles = news.get("articles", [])

    for i in range(min(5, len(articles))):
        output.append(articles[i]['title'])

    # ── WEATHER ─────────────────────────────
    output.append("Here is today's weather:")

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    weather_data = requests.get(weather_url).json()

    if weather_data.get("cod") == 200:
        temp = weather_data["main"]["temp"]
        desc = weather_data["weather"][0]["description"]
        output.append(f"The temperature is {temp}°C with {desc}.")
    else:
        output.append("I could not retrieve the weather.")

    # ── CALENDAR (placeholder) ──────────────
    output.append("Here are your events for today:")

    events = [
        "Machine Learning class at 10 AM",
        "Team meeting at 2 PM"
    ]

    if events:
        output.extend(events)
    else:
        output.append("No events scheduled.")

    # ── ASSIGNMENTS (placeholder) ───────────
    output.append("Upcoming deadlines:")

    tasks = [
        "CS 3345 Homework due tomorrow",
        "AI project due in 3 days"
    ]

    if tasks:
        output.extend(tasks)
    else:
        output.append("No deadlines found.")

    output.append("That concludes your morning briefing.")

    return "\n".join(output)