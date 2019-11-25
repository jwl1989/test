import pandas as pd

def stock_data():
    ali = pd.read_csv('data.csv')
    stocks = pd.DataFrame({'Date':ali['Date'],
                           'Close':ali['Close']})
    return stocks


if __name__ == '__main__':
    f = stock_data()
    print(f)