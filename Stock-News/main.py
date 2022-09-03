import requests

STOCK_NAME = "GOOGL"
COMPANY_NAME ="Alphabet Inc Class A"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_API_KEY = "ZL8TMSJFVDC9ZIL4"

#get yesterday's closing stock price

stock_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)