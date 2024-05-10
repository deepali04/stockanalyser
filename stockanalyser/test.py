from stocks_analyzer import get_stock_data, plot_compare_stocks
import datetime

def main():
    
    tickers = [ticker.strip() for ticker in input("Enter stock ticker symbols separated by comma (e.g., AAPL, MSFT, GOOGL) : ").split(',')]
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
        tickers = [ticker.upper() for ticker in tickers]
        stock_data = get_stock_data(tickers, start, end)
        plot_compare_stocks(stock_data)

    except ValueError as e:
        print(f"Validation error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# import unittest
# from stocks_analyzer import get_stock_data, plot_compare_stocks
# from utils import validate_tickers

# class TestStockAnalysisPackage(unittest.TestCase):
    
#     def test_validate_tickers(self):
#         """Test the validate_tickers function with both valid and invalid tickers."""
#         input_tickers = ['AAPL', 'GOOGL', 'XXXXX']
#         expected_output = ['XXXXX']  # Assuming 'XXXXX' is an invalid ticker
#         result = validate_tickers(input_tickers)
#         self.assertEqual(result, expected_output)

#     def test_get_stock_data(self):
#         """Test the get_stock_data function to ensure it returns data correctly."""
#         tickers = ['AAPL', 'MSFT']
#         start = '2022-01-01'
#         end = '2022-12-31'
#         data = get_stock_data(tickers, start, end)
#         # Check if data for each ticker is not empty
#         for ticker, df in data.items():
#             self.assertFalse(df.empty, f"Data for {ticker} is empty")

#     # Add more tests for other functions like analyze, plot functions, etc.
    
# if __name__ == '__main__':
#     unittest.main()

