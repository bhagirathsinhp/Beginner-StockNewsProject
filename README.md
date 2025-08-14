# 📈 Tesla Stock Alert & News WhatsApp Notifier

A Python automation project that **monitors Tesla’s stock price** using the **Alpha Vantage API**.  
If the price changes by **±5%** compared to the previous day, it **fetches the top 3 latest news articles** from **NewsAPI** and sends them to your phone via **WhatsApp** using **Call Me Bot API**.

---

## 🚀 Features

- Monitors **Tesla (TSLA)** daily stock prices.
- Calculates **percentage change** between the last two market days.
- If change ≥ ±5%, retrieves **top 3 relevant news articles** about Tesla.
- Sends formatted news headlines, descriptions, and URLs to WhatsApp.
- Uses **environment variables** for secure API key storage.

---

## 🛠️ Technologies Used

- **Python 3**
- **Alpha Vantage API** — Stock price data
- **NewsAPI** — Latest news articles
- **Call Me Bot API** — WhatsApp messaging
- **Requests** — HTTP API calls
- **dotenv** — Environment variable management

---

## 📂 Project Structure

    stock-alert-news/
    │
    ├── main.py                # Main Python script
    ├── .env                   # Environment variables (API keys, endpoints, phone number)
    └── README.md              # Project documentation

---

## 🔑 Environment Variables

- Create a .env file in the project root:

      ALPHAVANTAGE_API_KEY=your_alpha_vantage_api_key
      AV_ENDPOINT=https://www.alphavantage.co/query
      
      NEWSAPI_KEY=your_news_api_key
      GETNEWS_ENDPOINT=https://newsapi.org/v2/everything
      
      CALL_ME_API=your_call_me_bot_api_key
      CALLME_ENDPOINT=https://api.callmebot.com/whatsapp.php
      MOBILE_NUMBER=your_phone_number_with_country_code

---

## ▶️ How It Works

- Fetch Stock Data — The script uses Alpha Vantage API to get the last two closing prices of TSLA.
- Calculate Percentage Change — If the difference is ≥ 5% or ≤ -5%, it proceeds to fetch news.
- Fetch News Articles — NewsAPI returns the 3 most popular Tesla-related articles from the last two days.
- Send WhatsApp Message — Each article is sent as a separate WhatsApp message via Call Me Bot API.

---

## 📜 Example WhatsApp Message

  **Tesla Inc: 5.23% 📈**
  
  **Headline**: Tesla to launch new model in 2025
  
  **Brief**: Tesla has announced the upcoming launch of its latest EV model.
  
  **URL**: https://example.com/tesla-news

---

## 📌 Notes

- The Call Me Bot API requires prior setup to allow sending messages to your WhatsApp.
- The script is currently configured for Tesla (TSLA) but can be adapted for any stock by changing the STOCK and COMPANY_NAME variables

---

## 👤 Author

[![GitHub: bhagirathsinhp](https://img.shields.io/github/followers/bhagirathsinhp?label=Follow&style=social)](https://github.com/bhagirathsinhp)
[![LinkedIn: Bhagirath Parmar](https://img.shields.io/badge/-Bhagirath%20Parmar-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/bhagirath-parmar-385865269/)](https://www.linkedin.com/in/bhagirath-parmar-385865269/)

