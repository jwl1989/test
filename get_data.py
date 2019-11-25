# 参考接口文档https://pypi.org/project/yfinance/
from pandas_datareader import data as pdr
import yfinance as yf
import time

# 获取雅虎财经数据接口
yf.pdr_override()
data = pdr.get_data_yahoo('BABA',start='2017-08-20')
data.to_csv('data.csv')
print(data)