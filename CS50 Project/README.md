# Value At Risk Plotter
### Video Demo: https://youtu.be/RBK1IpUsIjc
### Description

Given a user supplied stock ticker, this program plots an estimation of the value at risk of that stock. The value at risk estimation uses a 250 day window and a 95% significance level. If the user inputs an incorrect ticker then the program will prompt them again.

## project.py

The program consists of 4 functions as a well as a class. The class creates a Stock object and initialises it with an attribute called returns that contains the last 3 years of returns for that stock. To create a Stock object you need to specify a stock ticker such as GOOG (google), MSFT (microsoft) or TSLA (tesla). The stock information is then fetched from Yahoo Finance by the pandas_datareader module.

The four functions are get_stock, var, var_series and plot_series.

### get_stock
Get stock prompts the user for a stock ticker and then returns the Stock object with that name.

### var
This is a helper function. It calculates the var for one particular day. It was used to make the definition of var_series a little more conceptually easier. It takes a window of 250 days before a given n and then find the 5th percentile of returns. The 5th percentile is why this programs outputs a VAR at a 95% (100%-5%) confidence level.

Figuring out the correct use of indices in stock.returns[-250 - n: -n] caused me to do a lot of debugging. It's necessary to split off the n=0 case because stock.returns[-250 : 0] will throw an error. The -n on either side of the : chooses a movable window of 250 returns from stock.returns.

### var_series
Given the function defined above we can use an in range loop to create a series of var values. It's then quite simple to append them together into one list. Note that this will be in reverse chronological order because we are starting from the most recent returns. We therefore reverse the list before returning it.

### plot_series
This function makes use of the matplotlib.pyplot library to plot the given series. It's a very basic function that only requires the x coordinates.

## test_project.py

Testing the functions I made was not straightforward. Because I am fetching real stock data from the internet it is not straightforward to know what the data will be ahead of time. In order to test I then created from fake stock data and a fake testing_Stock class that my functions made use of instead.

I also made use of the isinstance() function to check that the results fetched by pandas_datareader were at least of the correct type. Because I had created the stock returns numerically using list(range(-100000,100000,500)) I was able to calculate their VAR values mathematically. This allowed me to check my functions were calculating the right values.

Testing the plotting function was also difficult. The plt.show() function of matplotlib.pyplot causes pytest to hang. This is because it waits for user input to close. Since pytest gives no input it hangs forever and never finishes testing. In order to test it was creating a plot without raising an error it was necessary to deactivate this part of the plot_series function.

This can be achieved using the monkeypatch functionality of pytest. By passing in a parameter monkeypatch into the test_plot_series function, we can then use monkeypatch.setattr(plt, 'show', lambda: None) to "patch" the show() function so that it does nothing. By adding this line of code before calling the plot_series() function we can stop pytest from hanging.

## Design Choices

The sample window of 250 days was chosen because it is roughly equal to 1 trading year. It is also a standard window used in the industry. The 5% confidence window is also standard within the industry.

One design choice I made early on was to simpify the definition of the Stock object. Originally all of the functions were going to be within the class definition itself, so that stock.var() would return a series of Value at Risk calculated for a given stock. Ultimately though this just seemed needlessly complicated without much benefit and so as a proof of concept I reverted to just storing the returns in stock.return.
