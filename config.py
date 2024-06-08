# config.py

# MetaTrader 5 credentials
MT5_CREDENTIALS = {
    "LOGIN": "your_mt5_login",
    "PASSWORD": "your_mt5_password",
    "SERVER": "your_mt5_server",
    "PATH": "path_to_your_mt5_terminal"
}

# Other configuration variables
SYMBOL = "EURUSD"
RSI_SETTINGS = {
    "PERIOD": 14,
    "OVERSOLD": 30
}

# Define timeframes
import MetaTrader5 as mt5  # noqa: E402
TIMEFRAMES = {
    "1M": mt5.TIMEFRAME_M1,
    "5M": mt5.TIMEFRAME_M5,
    "15M": mt5.TIMEFRAME_M15,
    "1H": mt5.TIMEFRAME_H1,
    "4H": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,
    "W1": mt5.TIMEFRAME_W1,
    "MN1": mt5.TIMEFRAME_MN1
}