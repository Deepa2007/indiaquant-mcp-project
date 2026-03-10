import numpy as np
import yfinance as yf

def historical_volatility(symbol):

    try:
        data = yf.download(symbol, period="6mo", progress=False)

        if data.empty:
            return 0.25

        returns = np.log(data["Close"] / data["Close"].shift(1))
        vol = returns.std() * np.sqrt(252)

        if np.isnan(vol):
            return 0.25

        return round(float(vol), 4)

    except Exception:
        return 0.25
