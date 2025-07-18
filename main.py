import yfinance as yf

ticker = yf.Ticker("ITC.BO")  # Replace with the desired ticker symbol
todays_data = ticker.history(period="1d", interval="1m") # Get data for the past day, 1-minute interval
current_price = todays_data["Close"].iloc[-1]
print(current_price)
