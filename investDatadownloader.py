import investpy
import datetime
import pandas as pd

start=datetime.date.today()-datetime.timedelta(10000)
enddate=datetime.date.today()
startString = start.strftime("%d/%m/%Y")
endString = enddate.strftime("%d/%m/%Y")

f=open("stocklist.txt","r")
for ticker in f:
     df = investpy.get_stock_historical_data(stock=ticker.strip(),country='india', from_date=startString, to_date=endString)
     df.to_csv(r'C:\Users\suraj\Desktop\%s.csv'%ticker.strip())
    








