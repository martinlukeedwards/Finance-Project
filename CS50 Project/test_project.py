from project import Stock, var, var_series, plot_series
import numpy as np
import matplotlib.pyplot as plt

def test_Stock():
    stock=Stock('GOOG')
    assert isinstance(stock.returns[1], np.float64)

#Redefining Stock for the purpose of testing.
class testing_Stock:
    def __init__(self, ticker):
        self.returns=list(range(-100000,100000,500))


def test_var():
    stock=testing_Stock('GOOG')
    assert (var(stock,0)) == 18775.0
    assert (var(stock,100)) == 68775.0


def test_var_series():
    stock=testing_Stock('GOOG')
    assert isinstance(var_series(stock), list)
    assert (var_series(stock))[-1] == 18775.0


def test_plot_series(monkeypatch):
    xaxis=[0,1,2]
    #The following code deactivates the plt.show() function so that pytest does not hang.
    monkeypatch.setattr(plt, 'show', lambda: None)
    plot_series(xaxis)
    assert True
