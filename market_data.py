import yfinance as yf
import pandas as pd
import numpy as np
import datetime

from volatility import historical_volatility
from utils import safe_float


def calculate_rsi(data, window=14):

    delta = data.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    value = rsi.iloc[-1]

    if np.isnan(value):
        return 50

    return value


def get_market_data(symbol):

    try:

        ticker = yf.Ticker(symbol)

        hist = ticker.history(period="6mo")

        price = hist["Close"].iloc[-1]

        rsi = calculate_rsi(hist["Close"])

        vol = historical_volatility(symbol)

        if rsi < 40:
            trend = "Oversold"
        elif rsi > 60:
            trend = "Overbought"
        else:
            trend = "Sideways"

        return {
            "symbol": symbol,
            "price": safe_float(price),
            "rsi": safe_float(rsi),
            "historical_volatility": safe_float(vol),
            "trend": trend,
            "timestamp": str(datetime.datetime.now())
        }

    except Exception as e:

        return {
            "symbol": symbol,
            "error": str(e)
        }
