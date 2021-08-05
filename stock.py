import pandas as pd
from finvizfinance.quote import finvizfinance
stock = finvizfinance('amzn')

news_df = stock.TickerNews()

print(news_df)