#!/usr/bin/env python3.6

import pandas as pd
import matplotlib.pyplot as plt

def test_run() :
    #df = pd.read_csv("resources/HCP.csv")
    #print(df.head())
    #print(df[2:5])
    print(get_max_close("HCP"))

def plot_graph():
    df = pd.read_csv("resources/HCP.csv")
    #print(df['Adj Close'])
    #df['Adj Close'].plot()
    df[['Open', 'Close']].plot()
    plt.show()

def get_max_close(symbol):
    df = pd.read_csv("resources/{}.csv".format(symbol))
    return df['Volume'].mean()

if __name__ == "__main__":
    test_run() 
    plot_graph()