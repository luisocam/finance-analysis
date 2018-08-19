import requests
import json
import pandas as pd
import datetime as dt

def get_data(symbol, date):
    """Request a stock or ETF's 5 year price data from IEX's API and save as a csv file."""

    print('Getting 5 year data for ' + symbol + '...')

    url = 'https://api.iextrading.com/1.0/stock/' + symbol + '/chart/5y'
    data = requests.get(url).json()
    df = pd.DataFrame.from_dict(data)
    df.set_index('date', inplace = True)
    df.index = pd.to_datetime(df.index)
    df.to_csv(symbol + '_' + date + '.csv')

    print('Done')

# Get and transform current datetime to YYYY-MM-DD format
today = dt.datetime.now().strftime('%Y-%m-%d')

# Ask the user for the stock or ETF they want information for
user_symbol = input('Enter symbol: ')

# Get the requested stock or ETf's data
get_data(user_symbol, today)