#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    start_date = '2018-01-12'
    end_date = '2018-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    df1 = pd.DataFrame(index = dates)

    for symbol in ['AMZN', 'GLD', 'HCP', 'TWTR']:
        df_temp = pd.read_csv(  "resources/{}.csv".format(symbol),
                                index_col="Date",
                                parse_dates=True,
                                usecols=['Date', 'Adj Close'],
                                na_values=['NaN']
                            )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp, how='inner')
    print(df1)
    
    df_slice = df1.ix['2018-01-13':'2018-01-18', ['AMZN']]
    print(df_slice)
    plot_data(df1/df1.ix[0,:])

def plot_data(df, title="Stock Prices"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

if __name__ == '__main__':
    test_run()

