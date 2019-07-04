import pandas as pd

url1 = 'http://www.bankofcanada.ca/'
url2 = 'valet/observations/group/FX_RATES_DAILY/csv?start_date='
start_date = '2017-01-03'  # Earliest start date is 2017-01-03
url = url1 + url2 + start_date  # Complete url to download csv file
# Read in rates for different currencies for a range of dates
rates = pd.read_csv(url, skiprows=39, index_col='date')
rates.index = pd.to_datetime(rates.index)  # assures data type
# Get number of days & number of currences from shape of rates
days, currencies = rates.shape
# Read in the currency codes & strip off extraneous part
codes = pd.read_csv(url, skiprows=10, usecols=[0, 2],
                    nrows=currencies)
for i in range(currencies):
    codes.iloc[i, 1] = codes.iloc[i, 1].split(' to Canadian')[0]
# Report exchange rates for the most most recent date available
date = rates.index[-1]  # most recent date available
print('\nCurrency values on {0}'.format(date))
for (code, rate) in zip(codes.iloc[:, 1], rates.loc[date]):
    print("{0:20s}  Can$ {1:8.6g}".format(code, rate))
