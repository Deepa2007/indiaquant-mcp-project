import yfinance as yf
from utils import safe_float


def analyze_option_chain(symbol):

    try:

        ticker = yf.Ticker(symbol)

        expiries = ticker.options

        if len(expiries) == 0:
            return {"symbol": symbol, "error": "No option data"}

        expiry = expiries[0]

        chain = ticker.option_chain(expiry)

        calls = chain.calls
        puts = chain.puts

        call_oi = calls["openInterest"].sum()
        put_oi = puts["openInterest"].sum()

        pcr = put_oi / call_oi if call_oi else 0

        if pcr > 1:
            sentiment = "Bearish"
        elif pcr < 0.8:
            sentiment = "Bullish"
        else:
            sentiment = "Neutral"

        call_data = []

        for _, row in calls.head(10).iterrows():

            call_data.append({

                "strike": safe_float(row["strike"]),
                "price": safe_float(row["lastPrice"]),
                "volume": safe_float(row["volume"]),
                "openInterest": safe_float(row["openInterest"]),
                "impliedVolatility": safe_float(row["impliedVolatility"])

            })

        put_data = []

        for _, row in puts.head(10).iterrows():

            put_data.append({

                "strike": safe_float(row["strike"]),
                "price": safe_float(row["lastPrice"]),
                "volume": safe_float(row["volume"]),
                "openInterest": safe_float(row["openInterest"]),
                "impliedVolatility": safe_float(row["impliedVolatility"])

            })
        call_volume = calls["volume"].sum()
        put_volume = puts["volume"].sum()

        ratio = put_volume / call_volume if call_volume > 0 else None

        return {

            "symbol": symbol,
            "expiry": expiry,
            "put_call_ratio": safe_float(ratio),
            "sentiment": sentiment,
            "calls": call_data,
            "puts": put_data

        }

    except Exception as e:

        return {
            "symbol": symbol,
            "error": str(e)
        }
