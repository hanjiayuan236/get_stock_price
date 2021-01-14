# Discription
This is a test code to download stock data from yahoo.com. The function get_stock_price_today from get_stock_price.py takes a single stock_symbol as input, and returns a DataFrame object with 4 columns: 'High', 'Low', 'Open', and 'Close', which are the corrosponding stock data of that symbol today. If the symbol is not found from yahoo.com, it returns a vacant DataFrame.


# How to test if the code works
Run test.py to test the code. It tests 4 stock symbols: 'ISRG', 'AAPL', 'AAAA', and 'CHAU', and prints out data fetch from yahoo.com. If there is no data fetched from yahoo.com, the code prints error information. The printed information for the 4 symbols should be:

price information for ISRG:

High:  824.00

Low:   786.00

Open:  787.37

Close: 811.45

'--------------------------'


price information for AAPL:

High:  131.45

Low:   128.49

Open:  128.76

Close: 130.89

'--------------------------'


No data fetched for symbol AAAA from Yahoo.com. Please try other symbols.


'--------------------------'


price information for CHAU:

High:  48.82

Low:   48.41

Open:  48.66

Close: 48.63

'--------------------------'

# Version of Python and other packages
See requirements.txt
