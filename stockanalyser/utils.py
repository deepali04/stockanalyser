import datetime
import yfinance as yf

def validate(date_input):
    try:
        datetime.datetime.strptime(date_input, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD.")

def validate_date_range(start, end):
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
    if start_date >= end_date:
        raise ValueError("Start date must be earlier than end date.")
    if end_date > datetime.datetime.now():
        raise ValueError("End date cannot be in the future.")

def validate_tickers(tickers):
    invalid_tickers = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            # Fetch stock info; accessing 'info' itself triggers data retrieval
            info = stock.info
            # Check a common and usually available field such as 'previousClose'
            if 'previousClose' not in info or info['previousClose'] is None:
                invalid_tickers.append(ticker)
        except ValueError:
            # If accessing the info causes a ValueError, assume ticker is invalid
            invalid_tickers.append(ticker)
        except KeyError:
            # Missing necessary data can also indicate a problem
            invalid_tickers.append(ticker)


    return invalid_tickers

