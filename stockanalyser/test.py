from stocks_analyzer import get_stock_data, plot_compare_stocks, analyze_trends, plot_ma
import datetime, time, os

def main():
    
    tickers = [ticker.strip() for ticker in input("Enter stock ticker symbols separated by comma (e.g., AAPL, MSFT, GOOGL) : ").split(',')]
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
         os.makedirs("./output")
    except FileExistsError:
        pass

    try:
        tickers = [ticker.upper() for ticker in tickers]
        stock_data = get_stock_data(tickers, start, end)
        plot_compare_stocks(stock_data)
        for ticker, data in stock_data.items():
            ma_data = analyze_trends(data)
            time.sleep(2)
            plot_ma(ticker, ma_data)
    
    except ValueError as e:
        print(f"Validation error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()





