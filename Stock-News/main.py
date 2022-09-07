import requests

STOCK_NAME = "GOOGL"
COMPANY_NAME ="Alphabet Inc Class A"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_API_KEY = "ZL8TMSJFVDC9ZIL4"
MY_NEWS_ENDPOINT_API_KEY = "b079f236f23e4a9fb480f19fb4de12d3"
#get yesterday's closing stock price

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
#print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
#print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) 
if difference > 1:
    news_params = {
        "apiKey": MY_NEWS_ENDPOINT_API_KEY,
        "q": COMPANY_NAME
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
    three_articles = articles[:3]
    
    
    #formatted_articles = [f"Headline: {article['title']}. \nBrief: {article["description"]}" for article in three_articles]