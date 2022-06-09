import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = "6KPNON1CEDUUZNPO"
news_api_key = "9738bfb7f9b648b197ca544a5d4da261"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]['4. close']

day_before_yesterday_data = data_list[1]['4. close']
difference = abs(float(yesterday_data) - float(day_before_yesterday_data))
diff_percent = (difference / float(yesterday_data)) * 100
if diff_percent > 0:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

three_articles = articles[:3]
print(three_articles)
