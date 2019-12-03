from read_data import stock_data
from matplotlib import pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']   #设置字体
ali = stock_data()
# print(ali['Date'])
ali['Data'] = ali.Date.apply(lambda x : pd.to_datetime(x))
ali.index = ali['Date']
plt.figure()
ax = plt.subplot()
ax.set_title('BABA')
ali['Close'].plot(ax=ax,secondary_y=['BABA'],grid=True)
plt.show()