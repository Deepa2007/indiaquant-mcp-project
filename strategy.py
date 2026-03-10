from market_data import get_market_data
from utils import safe_float


def trading_strategy(symbol):

    data = get_market_data(symbol)

    if "error" in data:
        return data

    rsi = data["rsi"]
    price = data["price"]

    if rsi < 35:
        signal = "BUY"
        reason = "RSI indicates oversold market"

    elif rsi > 65:
        signal = "SELL"
        reason = "RSI indicates overbought market"

    else:
        signal = "HOLD"
        reason = "RSI indicates neutral conditions"

    return {
        "symbol": symbol,
        "price": safe_float(price),
        "rsi": safe_float(rsi),
        "signal": signal,
        "strategy": "RSI Strategy",
        "reason": reason
    }
