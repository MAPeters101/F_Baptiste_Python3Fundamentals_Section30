'''
Question 1
Alongside this notebook is a data file named daily_quotes.csv which contains
EOD OHLC/Volume data for a small number of equities over a 6 month period.

The first step is to load up this data into a dataframe, ensuring that all
data types are correct (datetime objects for dates, floats for OHLC data, and
integers for Volume).

Write a function that receives the file name as an argument and returns a
dataframe that:

has the correct data type for each column (str, float, int)
has a row index based on the symbol column
In addition, we would like our dataframe to contain columns named and ordered
in a specific way:

symbol (str)
date (datetime)
open (float)
high (float)
low (float)
close (float)
volume (int)
(with symbol being used as the row index)

Hint:

You will want to read up the Pandas docs for read_csv to see how you can handle
datetime data directly while loading the data (in particular you should look
at the parse_dates option):

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

Alternatively, you could convert these objects into proper datetime types after
loading by using the Pandas function to_datetime, documented here:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

and then use conatenation to build up a dataframe that replaces the "old" date
column with the "new" (properly typed) column.
'''