import investpy
import datetime
import os
import progressbar
from time import sleep

start=datetime.date.today()-datetime.timedelta(10000)
enddate=datetime.date.today()
startString = start.strftime("%d/%m/%Y")
endString = enddate.strftime("%d/%m/%Y")
path='C:\\Users\\suraj\\Desktop\\EOD DATA'
if not os.path.exists(path):
    os.makedirs(path)

f=open("stocklist.txt","r")
ticker=f.readlines()
num_lines=len(ticker)
# num_lines = sum(1 for line in f if line.rstrip())
#f.seek(0)
bar = progressbar.ProgressBar(maxval=num_lines,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

for x in range(num_lines):
     ticker[x]=ticker[x].split(",")
     #df = investpy.get_index_historical_data(index=ticker.strip(), country='india', from_date=startString, to_date=endString)
     df = investpy.get_stock_historical_data(stock=ticker[x][1],country='india', from_date=startString, to_date=endString)
     df.to_csv(path +'\\%s.csv'%ticker[x][0])
     bar.update(x)
    
f.close()
bar.finish()










