import investpy


df = investpy.get_stock_historical_data(stock='HIAE',country='india', from_date='01/01/2000', to_date='01/01/2021')
print(df.head())                                    
                        