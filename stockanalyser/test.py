from stocks_analyzer import get_stock_data, plot_compare_stocks, analyze
import datetime

def main():
    
    tickers = [ticker.strip() for ticker in input("Enter stock ticker symbols separated by comma (e.g., AAPL, MSFT, GOOGL) : ").split(',')]
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
        tickers = [ticker.upper() for ticker in tickers]
        stock_data = get_stock_data(tickers, start, end)
        plot_compare_stocks(stock_data)
        for ticket in tickers:
            print(ticket.upper())
            stock_data=get_stock_data([ticket],start,end)
            print(analyze(stock_data,ticket))

    except ValueError as e:
        print(f"Validation error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()





