import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage API:
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
AV_ENDPOINT=os.getenv("AV_ENDPOINT")
av_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHAVANTAGE_API_KEY,
}

# Get News API:
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GETNEWS_ENDPOINT = os.getenv("GETNEWS_ENDPOINT")

# Call Me Bot API:
CALL_ME_API = os.getenv("CALL_ME_API")
CALLME_ENDPOINT = os.getenv("CALLME_ENDPOINT")
MOBILE_NUMBER = os.getenv("MOBILE_NUMBER")

# Function to get News Articles from Get News API:
def getnews_articles(from_date: str, to_date: str):
    url=GETNEWS_ENDPOINT
    getnews_params = {
        "q": COMPANY_NAME,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "sortBy": "popularity",
        "pageSize": 3,
        "apiKey": NEWSAPI_KEY,
    }

    getnews_response = requests.get(url=url, params=getnews_params)
    getnews_response.raise_for_status()
    getnews_data = getnews_response.json()
    articles = getnews_data["articles"]
    return articles

# Function to send Whatsapp messages through Call Me Bot API:
def send_whatsapp_message(phone_number: str, msg: str):
    url = CALLME_ENDPOINT
    callme_params = {
        "phone": phone_number,
        "text": msg,
        "apikey":CALL_ME_API
    }

    call_me_response = requests.get(url=url, params=callme_params)
    print(call_me_response.text)

def message():
    articles_response = getnews_articles(av_two_dates[0], av_two_dates[1])
    msg_list = []
    for article in articles_response:
        headline = article['title']
        brief = article['description']
        article_url = article['url']
        text_message = f"""
*{company_text}*

*Headline*: {headline},

*Brief*: {brief},

*URL*: {article_url}
        """
        msg_list.append(text_message)

    return msg_list

## STEP 3: Use Call Me Bot
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_news():
    message_list = message()
    for messages in message_list:
        send_whatsapp_message(MOBILE_NUMBER, messages)
        time.sleep(1)

# Fetching Stock Data for the Company through Alpha Vantage API:
av_response = requests.get(url=AV_ENDPOINT, params=av_params)
av_response.raise_for_status()
av_data = av_response.json()
# print(av_data)

av_timeseries = av_data["Time Series (Daily)"]
av_timeseries_dates_list = list(av_timeseries.keys())

av_two_dates = av_timeseries_dates_list[:2]
av_two_day_data = [av_timeseries[dates] for dates in av_two_dates]

yesterday_close = float(av_two_day_data[0]['4. close'])
day_before_yesterday_close = float(av_two_day_data[1]['4. close'])
print(yesterday_close, day_before_yesterday_close)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
difference_percentage = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
difference_percentage = round(difference_percentage, 2)
print(difference_percentage)
# difference_percentage = -5

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if difference_percentage >= 5:
    company_text = f"{COMPANY_NAME}: {difference_percentage}% 📈"
    send_news()

elif difference_percentage <= -5:
    company_text = f"{COMPANY_NAME}: {difference_percentage}% 📉"
    send_news()



