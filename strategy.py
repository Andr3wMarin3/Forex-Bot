import numpy as np

def calculate_rsi(closes, period=14):
    deltas = np.diff(closes)
    up, down = np.zeros_like(deltas), np.zeros_like(deltas)
    up[deltas > 0] = deltas[deltas > 0]
    down[deltas < 0] = -deltas[deltas < 0]
    roll_up1 = np.mean(up[:period])
    roll_down1 = np.mean(down[:period])
    rs = roll_up1 / roll_down1
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

def identify_lower_high_low(rates, is_bullish):
    highs = rates['high']
    lows = rates['low']
    if is_bullish:
        for i in range(2, len(highs)):
            if highs[i] < highs[i-1] and highs[i-1] > highs[i-2]:
                for j in range(2, len(lows)):
                    if lows[j] > lows[j-1] and lows[j-1] < lows[j-2]:
                        return i-1, j-1  # Return the index of the lower high and higher low
        return None, None  # Return None if no lower high and higher low are found
    else:
        for i in range(2, len(highs)):
            if highs[i] > highs[i-1] and highs[i-1] < highs[i-2]:
                for j in range(2, i):  # Ensure the higher low is within the range of the higher high
                    if lows[j] > lows[j-1] and lows[j-1] < lows[j-2]:
                        return i-1, j-1  # Return the index of the higher high and higher low
        return None, None  # Return None if no higher high and higher low are found

def check_strategy(symbol, timeframes):
    priority_order = ["Monthly", "Weekly", "Daily", "4H", "1H", "15M", "5M", "1M"]
    main_timeframe = None
    main_lower_high_idx = None
    main_lower_low_idx = None
    main_is_bullish = None

    for tf_name in priority_order:
        tf_value = timeframes[tf_name]
        rates = get_market_data(symbol, tf_value, 100)  # Replace with your actual market data retrieval function
        if rates is None:
            continue
        closes = rates['close']
        rsi = calculate_rsi(closes)
        if main_timeframe is None:
            main_timeframe = tf_name
        if rsi < 30 and main_is_bullish is None:  # Oversold, bullish sentiment
            main_is_bullish = True
            main_lower_high_idx, main_lower_low_idx = identify_lower_high_low(rates, main_is_bullish)

        elif rsi > 70 and main_is_bullish is None:  # Overbought, bearish sentiment
            main_is_bullish = False
            main_lower_high_idx, main_lower_low_idx = identify_lower_high_low(rates, main_is_bullish)

        if main_is_bullish is not None:
            break

    if main_is_bullish is None:
        return "HOLD"

    return "HOLD"

def get_market_data(symbol, timeframe, limit):
    # Implement your market data retrieval logic here
    # Return a dictionary with keys 'high', 'low', 'close'
    pass

# Example Usage
symbol = "EURUSD"
timeframes = {"Monthly": "1mo", "Weekly": "1w", "Daily": "1d", "4H": "4h", "1H": "1h", "15M": "15m", "5M": "5m", "1M": "1m"}
signal = check_strategy(symbol, timeframes)
print(signal)
