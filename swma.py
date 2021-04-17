import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from pandas_datareader import data as pdr 
import yfinance as yf
from scipy import stats

def get_data_from_csv(fn_asset, fn_market):
    asset_data = pd.read_csv(fn_asset)
    market_data = pd.read_csv(fn_market)
    return_asset = asset_data['Adj Close'].pct_change()[1:]
    return_market = market_data['Adj Close'].pct_change()[1:]

    return return_asset, return_market


def get_data(asset, market, start_date, end_date):
    yf.pdr_override()
    asset_data = pdr.get_data_yahoo(asset, start=start_date, end=end_date)
    market_data = pdr.get_data_yahoo(market, start=start_date, end=end_date)

    return_asset = asset_data['Adj Close'].pct_change()[1:]
    return_market = market_data['Adj Close'].pct_change()[1:]
    
    return return_asset, return_market

def visualize_return(return_asset, return_market):
    plt.figure(figsize=(20,10))
    return_asset.plot(label='SWMA.ST')
    return_market.plot(label='^OMX')
    plt.legend()
    plt.show()


def compute_beta(X,Y):
    min_length= min(len(X), len(Y))
    beta, alpha = stats.linregress(X[:min_length].values, Y[:min_length].values)[0:2]
    print("The portfolio beta is", round(beta, 4))

#swma, omx = get_data('SWMA.ST', '^OMX', '2016-04-10', '2021-04-10')
swma, omx = get_data_from_csv('./^OMX.csv', './SWMA.ST.csv')

compute_beta(swma, omx)

visualize_return(swma, omx)