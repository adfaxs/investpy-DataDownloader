import investpy
import datetime
import pandas as pd


stocks=["HIAE","INFY","HDFC"]

start=datetime.date.today()-datetime.timedelta(10000)
enddate=datetime.date.today()
startString = start.strftime("%d/%m/%Y")
endString = enddate.strftime("%d/%m/%Y")

for ticker in stocks:
    df = investpy.get_stock_historical_data(stock=ticker,country='india', from_date=startString, to_date=endString)
    df.to_csv(r'C:\Users\suraj\Desktop\%s.csv'%ticker)
