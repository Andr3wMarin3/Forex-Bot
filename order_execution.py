import MetaTrader5 as mt5

def place_order(symbol, order_type, lot, sl_points, tp_points):
    """
    Places an order on the MetaTrader 5 platform.

    Args:
        symbol (str): The symbol to trade.
        order_type (str): The type of order to place, e.g., "buy", "sell".
        lot (float): The order volume.
        sl_points (int): The stop-loss level in points.
        tp_points (int): The take-profit level in points.

    Returns:
        mt5.TradeRequest: The order request object.
    """

    # Check if the MetaTrader 5 terminal is initialized
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    # Get the current price
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol, True):
            print("symbol_select({}) failed, exit".format(symbol))
            mt5.shutdown()
            quit()

    price = mt5.symbol_info_tick(symbol).bid if order_type == "buy" else mt5.symbol_info_tick(symbol).ask

    # Define the order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "type": mt5.ORDER_TYPE_BUY if order_type == "buy" else mt5.ORDER_TYPE_SELL,
        "volume": lot,
        "price": price,
        "sl": price - sl_points * mt5.symbol_info(symbol).point,
        "tp": price + tp_points * mt5.symbol_info(symbol).point,
        "magic": 12345,  # Your custom magic number
        "comment": "Python script order",
        "type_time": mt5.ORDER_TIME_GTC,  # Good till cancelled
        "type_filling": mt5.ORDER_FILLING_FOK,  # Fill or kill
    }

    # Send the order request
    result = mt5.order_send(request)

    # Handle order execution result
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print("Order placed successfully!")
        print(result)
        return result
    else:
        print("Order failed!")
        print(result)
        return result

# Example usage
symbol = "EURUSD"
order_type = "buy"
lot = 0.1
sl_points = 50
tp_points = 100
result = place_order(symbol, order_type, lot, sl_points, tp_points)
