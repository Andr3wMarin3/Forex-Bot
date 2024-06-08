import MetaTrader5 as mt5

def get_market_data(symbol, timeframe, num_bars):
    # Initialize MT5 if it's not already initialized
    if not mt5.initialize():
        print("Failed to initialize MT5")
        return None

    try:
        # Retrieve the data
        rates, _ = mt5.copy_rates_from(symbol, timeframe, 0, num_bars)
        
        # Check if data is available
        if len(rates) > 0:
            return {
                'time': [rate.time for rate in rates],
                'open': [rate.open for rate in rates],
                'high': [rate.high for rate in rates],
                'low': [rate.low for rate in rates],
                'close': [rate.close for rate in rates],
                'tick_volume': [rate.tick_volume for rate in rates],
                'spread': [rate.spread for rate in rates],
                'real_volume': [rate.real_volume for rate in rates]
            }
        else:
            print(f"No data available for {symbol} on {timeframe} timeframe")
            return None
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None
    finally:
        # Shutdown MT5
        mt5.shutdown()

# Example usage
data = get_market_data('EURUSD', mt5.TIMEFRAME_M1, 100)
if data:
    print(data)
else:
    print("No data retrieved")
