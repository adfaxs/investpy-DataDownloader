import investpy
import datetime
import pandas as pd


stocks=["HIAE","INFY","HDFC"]

start=datetime.date.today()-datetime.timedelta(10000)
enddate=datetime.date.today()
startString = start.strftime("%d/%m/%Y")
endString = enddate.strftime("%d/%m/%Y")
df = investpy.get_stock_historical_data(stock='INFY',country='india', from_date=startString, to_date=endString)
print(df.head())                                    
df.to_csv (r'C:\Users\suraj\Desktop\IFY.csv', index = True, header=True)                        