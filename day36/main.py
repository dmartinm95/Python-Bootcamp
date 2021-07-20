# Day 36: Stock Trading News Alert Project
import datetime
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = "1ST9KS7PTQ5INABC"
news_api_key = "61d3edf4fe9142feb0e09744b8b5af84"
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
    "outputsize": "compact",
}

news_url = "https://newsapi.org/v2/everything"
news_params = {
    "q": COMPANY_NAME,
    "from": str(datetime.datetime.now().date()),
    "sortBy": "popularity",
    "apiKey": news_api_key,
}
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

response = requests.get(url=url, params=params)

response.raise_for_status()

stock_data = response.json()
stock_time_series = stock_data["Time Series (Daily)"]

last_business_day = datetime.datetime.today()
shift = datetime.timedelta(max(1, (last_business_day.weekday() + 6) % 7 - 3))
last_business_day = last_business_day - shift
last_business_day = last_business_day.date()

day_before_last_business_day = last_business_day - datetime.timedelta(days=1)

last_business_day = str(last_business_day)
day_before_last_business_day = str(day_before_last_business_day)

market_close_yesterday = float(
    stock_time_series[last_business_day]["4. close"])
market_close_day_before_yesterday = float(
    stock_time_series[day_before_last_business_day]["4. close"])

price_difference = market_close_yesterday - market_close_day_before_yesterday
price_difference_percentage = max(market_close_yesterday, market_close_day_before_yesterday) / \
    min(market_close_yesterday, market_close_day_before_yesterday)

news_response = requests.get(url=news_url, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
news_articles = news_data["articles"]
top_three_articles = news_articles[:3]
top_three_urls = [article["url"] for article in top_three_articles]
top_three_titles = [article["title"] for article in top_three_articles]
top_three_descriptions = [article["description"]
                          for article in top_three_articles]

print("REPORT")
if price_difference > 0:
    print(f"{STOCK}: UP by {format(price_difference_percentage, '.2f')}%")
else:
    print(f"{STOCK}: DOWN by {format(price_difference_percentage, '.2f')}%")


for i in range(len(top_three_articles)):
    print(f"ARTICLE {i+1}")
    print(f"Headline: {top_three_titles[i]}")
    print(f"Brief: {top_three_descriptions[i]}")
    print(f"URL: {top_three_urls[i]}\n")
