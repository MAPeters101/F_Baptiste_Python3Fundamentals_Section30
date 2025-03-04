'''
Question 1
Alongside this notebook is a data file named daily_quotes.csv which contains EOD OHLC/Volume data for a small number of equities over a 6 month period.

The first step is to load up this data into a dataframe, ensuring that all data types are correct (datetime objects for dates, floats for OHLC data, and integers for Volume).

Write a function that receives the file name as an argument and returns a dataframe that:

has the correct data type for each column (str, float, int)
has a row index based on the symbol column
In addition, we would like our dataframe to contain columns named and ordered in a specific way:

symbol (str)
date (datetime)
open (float)
high (float)
low (float)
close (float)
volume (int)
(with symbol being used as the row index)

Hint:

You will want to read up the Pandas docs for read_csv to see how you can handle datetime data directly while loading the data (in particular you should look at the parse_dates option):

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

Alternatively, you could convert these objects into proper datetime types after loading by using the Pandas function to_datetime, documented here:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

and then use conatenation to build up a dataframe that replaces the "old" date column with the "new" (properly typed) column.

Solution
We'll use the Pandas read_csv function to load the dataframe with the column names and index we want to use:

import pandas as pd
Let's see what our data file looks like before we load it up:

with open('daily_quotes.csv') as f:
    for _ in range(5):
        print(next(f).strip())
﻿Symbol,Date, Close/Last, Volume, Open, High, Low
AAPL,2/12/21,135.37,60145130,134.35,135.53,133.6921
AMZN,2/12/21,3277.71,2335339,3250,3280.25,3233.31
GOOG,2/12/21,2104.11,855865,2090.25,2108.82,2083.13
MSFT,2/12/21,244.99,16561080,243.933,245.3,242.73
We can see that our columns are ordered as: Symbol, Date, Close/Last, Volume, Open, High, Low - we'll use that fact to rename our columns as we import the data.

df = pd.read_csv(
    'daily_quotes.csv',
    header=0,
    names=['symbol', 'date', 'close', 'volume', 'open', 'high', 'low'],
    index_col = 0,
)
df
date	close	volume	open	high	low
symbol
AAPL	2/12/21	135.37	60145130	134.350	135.5300	133.6921
AMZN	2/12/21	3277.71	2335339	3250.000	3280.2500	3233.3100
GOOG	2/12/21	2104.11	855865	2090.250	2108.8200	2083.1300
MSFT	2/12/21	244.99	16561080	243.933	245.3000	242.7300
AAPL	2/11/21	135.13	64280030	135.900	136.3900	133.7700
...	...	...	...	...	...	...
MSFT	8/14/20	208.90	17958940	208.760	209.5900	207.5100
AAPL	8/13/20	115.01	210082080	114.430	116.0425	113.9275
AMZN	8/13/20	3161.02	3149043	3182.990	3217.5211	3155.0000
GOOG	8/13/20	1518.45	1455208	1510.340	1537.2500	1508.0050
MSFT	8/13/20	208.70	22588870	209.440	211.3500	208.1500
508 rows × 6 columns

We want to generate a dataframe where the columns are ordered slightly differently, so we can use fancy indexing for that:

df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
df
date	open	high	low	close	volume
symbol
AAPL	2/12/21	134.350	135.5300	133.6921	135.37	60145130
AMZN	2/12/21	3250.000	3280.2500	3233.3100	3277.71	2335339
GOOG	2/12/21	2090.250	2108.8200	2083.1300	2104.11	855865
MSFT	2/12/21	243.933	245.3000	242.7300	244.99	16561080
AAPL	2/11/21	135.900	136.3900	133.7700	135.13	64280030
...	...	...	...	...	...	...
MSFT	8/14/20	208.760	209.5900	207.5100	208.90	17958940
AAPL	8/13/20	114.430	116.0425	113.9275	115.01	210082080
AMZN	8/13/20	3182.990	3217.5211	3155.0000	3161.02	3149043
GOOG	8/13/20	1510.340	1537.2500	1508.0050	1518.45	1455208
MSFT	8/13/20	209.440	211.3500	208.1500	208.70	22588870
508 rows × 6 columns

We also need to check the data type of each column:

df.info()
<class 'pandas.core.frame.DataFrame'>
Index: 508 entries, AAPL to MSFT
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    508 non-null    object
 1   open    508 non-null    float64
 2   high    508 non-null    float64
 3   low     508 non-null    float64
 4   close   508 non-null    float64
 5   volume  508 non-null    int64
dtypes: float64(4), int64(1), object(1)
memory usage: 27.8+ KB
So, all the columns except the date column have the correct data type.

We could use Pandas' to_datetime function to cast that column to the proper type:

pd.to_datetime(df['date'])
symbol
AAPL   2021-02-12
AMZN   2021-02-12
GOOG   2021-02-12
MSFT   2021-02-12
AAPL   2021-02-11
          ...
MSFT   2020-08-14
AAPL   2020-08-13
AMZN   2020-08-13
GOOG   2020-08-13
MSFT   2020-08-13
Name: date, Length: 508, dtype: datetime64[ns]
If we approach it this way, we'll need to concatenate this column with the other columns from our original dataframe to form the new dataframe.

Instead, it is quite easy to actually specify that this column should be parsed as a datetime right in the rads_csv function's arguments:

df = pd.read_csv(
    'daily_quotes.csv',
    header=0,
    names=['symbol', 'date', 'close', 'volume', 'open', 'high', 'low'],
    parse_dates=['date'],
    index_col = 0,
)
df
date	close	volume	open	high	low
symbol
AAPL	2021-02-12	135.37	60145130	134.350	135.5300	133.6921
AMZN	2021-02-12	3277.71	2335339	3250.000	3280.2500	3233.3100
GOOG	2021-02-12	2104.11	855865	2090.250	2108.8200	2083.1300
MSFT	2021-02-12	244.99	16561080	243.933	245.3000	242.7300
AAPL	2021-02-11	135.13	64280030	135.900	136.3900	133.7700
...	...	...	...	...	...	...
MSFT	2020-08-14	208.90	17958940	208.760	209.5900	207.5100
AAPL	2020-08-13	115.01	210082080	114.430	116.0425	113.9275
AMZN	2020-08-13	3161.02	3149043	3182.990	3217.5211	3155.0000
GOOG	2020-08-13	1518.45	1455208	1510.340	1537.2500	1508.0050
MSFT	2020-08-13	208.70	22588870	209.440	211.3500	208.1500
508 rows × 6 columns

And if we now look at our dataframes columns, we'll see that the date column is actually a datetime object:

df.info()
<class 'pandas.core.frame.DataFrame'>
Index: 508 entries, AAPL to MSFT
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    508 non-null    datetime64[ns]
 1   close   508 non-null    float64
 2   volume  508 non-null    int64
 3   open    508 non-null    float64
 4   high    508 non-null    float64
 5   low     508 non-null    float64
dtypes: datetime64[ns](1), float64(4), int64(1)
memory usage: 27.8+ KB
So let's put all this in a function that will return the dataframe that we want based on the data in that file:

def load_df(file_name):
    df = pd.read_csv(
        'daily_quotes.csv',
        header=0,
        names=['symbol', 'date', 'close', 'volume', 'open', 'high', 'low'],
        index_col = 0,
        parse_dates=['date'],
    )
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
    return df
df = load_df('daily_quotes.csv')
df.info()
<class 'pandas.core.frame.DataFrame'>
Index: 508 entries, AAPL to MSFT
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    508 non-null    datetime64[ns]
 1   open    508 non-null    float64
 2   high    508 non-null    float64
 3   low     508 non-null    float64
 4   close   508 non-null    float64
 5   volume  508 non-null    int64
dtypes: datetime64[ns](1), float64(4), int64(1)
memory usage: 27.8+ KB
Question 2
Write a function that, given a dataframe sructured as the one we created in Question 1 and a symbol name as a string (e.g. AAPL, MSFT, etc), will:

return a similarly structured dataframe consisting of the row (or rows) containing the records with the highest volume for the given symbol
raises a ValueError if the symbol is not in the dataframe
Solution
We'll use the dataframe from Question 1.

We'll want to focus on a single symbol at a time, so we can do this by leveraging the symbol index we have on the dataframe.

For example, to extract just the rows for GOOG, we could do this:

df = load_df('daily_quotes.csv')
df.loc['GOOG', :]
date	open	high	low	close	volume
symbol
GOOG	2021-02-12	2090.25	2108.8200	2083.130	2104.11	855865
GOOG	2021-02-11	2099.51	2102.0300	2077.320	2095.89	945650
GOOG	2021-02-10	2094.21	2108.3700	2063.090	2095.38	1135464
GOOG	2021-02-09	2078.54	2105.1300	2078.540	2083.51	889850
GOOG	2021-02-08	2105.91	2123.5469	2072.000	2092.91	1242411
...	...	...	...	...	...	...
GOOG	2020-08-19	1553.31	1573.6800	1543.950	1547.53	1660611
GOOG	2020-08-18	1526.18	1562.4700	1523.710	1558.60	2027086
GOOG	2020-08-17	1514.67	1525.6100	1507.970	1517.98	1378600
GOOG	2020-08-14	1515.66	1521.9000	1502.880	1507.73	1355200
GOOG	2020-08-13	1510.34	1537.2500	1508.005	1518.45	1455208
127 rows × 6 columns

Note that if the symbol does not exist, we get a KeyError exception (which we'll later want to raise as a ValueError instead - although leaving it as a KeyError is probably just fine, it's a good exercise reminding us how to trap and raise exceptions).

try:
    df.loc['ABC', :]
except KeyError:
    print('Could not find symbol ABC')
Could not find symbol ABC
Next, we'll want to identify the max of the Volume column for this particular subset:

subset = df.loc['GOOG', :]
subset['volume']
symbol
GOOG     855865
GOOG     945650
GOOG    1135464
GOOG     889850
GOOG    1242411
         ...
GOOG    1660611
GOOG    2027086
GOOG    1378600
GOOG    1355200
GOOG    1455208
Name: volume, Length: 127, dtype: int64
And the max of that column can be calculated using the max function:

max(subset['volume'])
4330862
Or we could use the max method instead:

subset['volume'].max()
4330862
Once we have that number, we can use boolean masking to pick up the specific row (or rows if that same max occurs multiple times) from the dataframe:

subset[subset['volume'] == subset['volume'].max()]
date	open	high	low	close	volume
symbol
GOOG	2020-10-30	1672.11	1687.0	1604.46	1621.01	4330862
In this case only a single row matched that maximal value.

So now let's write a function to encapsulate all this.

def max_volume(df, symbol):
    try:
        subset = df.loc[symbol, :]
    except KeyError:
        raise ValueError(f'Symbol {symbol} has no data.')

    return subset[subset['volume'] == subset['volume'].max()]
max_volume(df, 'GOOG')
date	open	high	low	close	volume
symbol
GOOG	2020-10-30	1672.11	1687.0	1604.46	1621.01	4330862
max_volume(df, 'MSFT')
date	open	high	low	close	volume
symbol
MSFT	2021-01-27	238.0	240.44	230.14	232.9	69870640
max_volume(df, 'AAPL')
date	open	high	low	close	volume
symbol
AAPL	2020-08-24	128.6975	128.785	123.9363	125.8575	345937760
max_volume(df, 'AMZN')
date	open	high	low	close	volume
symbol
AMZN	2020-09-18	3031.74	3037.8	2905.54	2954.91	8892580
And we should get a ValueError if we speciy a symbol that is not in the data:

try:
    max_volume(df, 'XYZ')
except ValueError as ex:
    print(ex)
Symbol XYZ has no data.
Question 3
Using the same dataframe as in the preceding questions, our goal now is to write a function that will return, for a specific symbol, the row that had the largest high-low spread.

Write a function to do that - it should just return a dataframe with the row (or rows) with the largest high-low spread.

Solution
We'll basically follow the same approach as the last question, but we'll need to calculate the high-low spread - we'll use a Pandas series to first calculate all the high-low deltas:

df = load_df('daily_quotes.csv')
subset = df.loc['AAPL', :]
subset
date	open	high	low	close	volume
symbol
AAPL	2021-02-12	134.3500	135.5300	133.6921	135.3700	60145130
AAPL	2021-02-11	135.9000	136.3900	133.7700	135.1300	64280030
AAPL	2021-02-10	136.4800	136.9900	134.4000	135.3900	73046560
AAPL	2021-02-09	136.6200	137.8770	135.8500	136.0100	76774210
AAPL	2021-02-08	136.0300	136.9600	134.9200	136.9100	71297210
...	...	...	...	...	...	...
AAPL	2020-08-19	115.9833	117.1625	115.6100	115.7075	145538000
AAPL	2020-08-18	114.3525	116.0000	114.0075	115.5625	105633560
AAPL	2020-08-17	116.0625	116.0875	113.9625	114.6075	119561440
AAPL	2020-08-14	114.8288	115.0000	113.0450	114.9075	165565200
AAPL	2020-08-13	114.4300	116.0425	113.9275	115.0100	210082080
127 rows × 6 columns

Next, we can calculate the delta between low and high - since high > low we don't actually need to use an absolute value, but I'll do that here anyways, just to be absolutely sure:

deltas = abs(subset['high'] - subset['low'])
deltas
symbol
AAPL    1.8379
AAPL    2.6200
AAPL    2.5900
AAPL    2.0270
AAPL    2.0400
         ...
AAPL    1.5525
AAPL    1.9925
AAPL    2.1250
AAPL    1.9550
AAPL    2.1150
Length: 127, dtype: float64
The max spread is then given by:

deltas.max()
12.810000000000002
We can then use boolean masking, just like before:

subset[deltas == deltas.max()]
date	open	high	low	close	volume
symbol
AAPL	2020-09-04	120.07	123.7	110.89	120.96	332607200
Let's put all this into a function:

def max_spread(df, symbol):
    try:
        subset = df.loc[symbol, :]
    except KeyError:
        raise ValueError(f'{symbol} not in data')

    deltas = abs(subset['high'] - subset['low'])
    max_delta = deltas.max()
    return subset[deltas == max_delta]
max_spread(df, 'AAPL')
date	open	high	low	close	volume
symbol
AAPL	2020-09-04	120.07	123.7	110.89	120.96	332607200
max_spread(df, 'MSFT')
date	open	high	low	close	volume
symbol
MSFT	2020-09-03	229.27	229.31	214.9602	217.3	58400290
Question 4
Using the same dataframe as the preceding questions, write a function that returns a single dataframe containing the record(s) with maximum high-low spread for each symbol in the dataframe. (Do not hardcode symbol names in this function - instead you should recover the possible symbol names from the data itself).

The returned dataframe should have the same structure as the original dataframe, but just contain the rows of maximum high-low spread for each symbol.

Solution
To find all the symbol values, we can simply look at the index on the dataframe:

df = load_df('daily_quotes.csv')
df.index
Index(['AAPL', 'AMZN', 'GOOG', 'MSFT', 'AAPL', 'AMZN', 'GOOG', 'MSFT', 'AAPL',
       'AMZN',
       ...
       'GOOG', 'MSFT', 'AAPL', 'AMZN', 'GOOG', 'MSFT', 'AAPL', 'AMZN', 'GOOG',
       'MSFT'],
      dtype='object', name='symbol', length=508)
From that index we can recover the unique values by using a Python set:

set(df.index)
{'AAPL', 'AMZN', 'GOOG', 'MSFT'}
Now that we have the symbol names, we can use the max_spread function we wrote in the last question to generate the dataframe for each symbol:

for symbol in set(df.index):
    subset = df.loc[symbol, :]
    rows = max_spread(subset, symbol)
    print(rows)
             date    open    high      low    close   volume
symbol
AMZN   2020-09-04  3318.0  3381.5  3111.13  3294.62  8781754
             date    open    high       low  close    volume
symbol
MSFT   2020-09-03  229.27  229.31  214.9602  217.3  58400290
             date    open   high     low   close     volume
symbol
AAPL   2020-09-04  120.07  123.7  110.89  120.96  332607200
             date    open    high      low    close   volume
symbol
GOOG   2021-02-03  2073.0  2116.5  2018.38  2070.07  4118170
We can then concatenate all these dataframes along the vertical axis.

What we'll do is use a list comprehension to generate a list of these dataframes, and then use the concat function in Pandas:

max_frames = [
    max_spread(df.loc[symbol, :], symbol)
    for symbol in set(df.index)
]
max_frames
[             date    open    high      low    close   volume
 symbol
 AMZN   2020-09-04  3318.0  3381.5  3111.13  3294.62  8781754,
              date    open    high       low  close    volume
 symbol
 MSFT   2020-09-03  229.27  229.31  214.9602  217.3  58400290,
              date    open   high     low   close     volume
 symbol
 AAPL   2020-09-04  120.07  123.7  110.89  120.96  332607200,
              date    open    high      low    close   volume
 symbol
 GOOG   2021-02-03  2073.0  2116.5  2018.38  2070.07  4118170]
And then we can concatenate them:

pd.concat(max_frames, axis=0)
date	open	high	low	close	volume
symbol
AMZN	2020-09-04	3318.00	3381.50	3111.1300	3294.62	8781754
MSFT	2020-09-03	229.27	229.31	214.9602	217.30	58400290
AAPL	2020-09-04	120.07	123.70	110.8900	120.96	332607200
GOOG	2021-02-03	2073.00	2116.50	2018.3800	2070.07	4118170
Let's put this together in a function:

def max_spreads(df):
    max_frames = [
        max_spread(df.loc[symbol, :], symbol)
        for symbol in set(df.index)
    ]
    return pd.concat(max_frames, axis=0)
max_spreads(df)
date	open	high	low	close	volume
symbol
AMZN	2020-09-04	3318.00	3381.50	3111.1300	3294.62	8781754
MSFT	2020-09-03	229.27	229.31	214.9602	217.30	58400290
AAPL	2020-09-04	120.07	123.70	110.8900	120.96	332607200
GOOG	2021-02-03	2073.00	2116.50	2018.3800	2070.07	4118170
Click to add a cell.
'''