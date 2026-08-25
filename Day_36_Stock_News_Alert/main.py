import requests
from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

news_api =NewsApiClient(news_api_key)

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()

stock_response_data = response.json()
print(stock_response_data)

yesterday_closing_price = stock_response_data["Time Series (Daily)"]["2026-08-21"]["4. close"]

two_days_ago_closing_price = stock_response_data["Time Series (Daily)"]["2026-08-20"]["4. close"]

price_difference = abs(float(yesterday_closing_price) -float(two_days_ago_closing_price))

percentage_change = (price_difference / float(two_days_ago_closing_price)) * 100


if percentage_change > 5:
    news_parameters = {
        "apikey": news_api_key,
        "q": COMPANY_NAME,
        "language": "en",
        "sortBy": "relevance"
    }

    news_response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()

    news_response_data = news_response.json()

    latest_articles = news_response_data["articles"][:3]

    news_messages = [
        f"Headline: {news_article['title']}\n"
        f"Brief: {news_article['description']}"
        for news_article in latest_articles
    ]

    twilio_client = Client(twilio_account_sid,twilio_auth_token)

    for news_message in news_messages:
        message = twilio_client.messages.create(
            to="+2348085221944",
            from_="+17372508034",
            body=f"TSLA: 🔺{percentage_change:.2f}%\n{news_message}"
        )