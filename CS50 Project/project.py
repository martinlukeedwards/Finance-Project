import pandas_datareader.data as web
from pandas_datareader._utils import RemoteDataError
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt


class Stock:
    def __init__(self, ticker):
        data = web.DataReader(
            ticker, "yahoo", date.today() - timedelta(365 * 3), date.today()
        )
        self.returns = np.log(data["Close"] / data["Close"].shift(1))[1:]


def main():
    """Create line graph of value of risk of user input of stock ticker."""
    while True:
        try:
            stock = get_stock()
        except RemoteDataError:
            pass
        else:
            break
    var = var_series(stock)
    plot_series(var)


def get_stock():
    """return stock object"""
    return Stock(input("Stock Ticker: "))


def var(stock, n):
    """return the 5% var of stock calculated from last 250 days of returns, starting n days before today"""
    if n != 0:
        return -np.percentile(stock.returns[-250 - n: -n], 5)
    else:
        return -np.percentile(stock.returns[-250:], 5)


def var_series(stock):
    """return series of var values for stock calculated from last 250 days of returns"""
    var_series = []
    for n in range(0, len(stock.returns) - 250 + 1):
        var_series.append(var(stock, n))
    var_series.reverse()
    return var_series


def plot_series(series):
    """outputs line plot of given series"""
    xaxis = series
    plt.plot(xaxis)
    plt.show()


if __name__ == "__main__":
    main()
