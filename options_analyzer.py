import yfinance as yf


def get_option_chain(symbol):

    try:

        ticker = yf.Ticker(symbol)

        expirations = ticker.options

        if not expirations:
            return None

        expiry = expirations[0]

        chain = ticker.option_chain(expiry)

        calls = chain.calls
        puts = chain.puts

        return {
            "expiry": expiry,
            "calls_count": len(calls),
            "puts_count": len(puts),
        }

    except Exception as e:

        print("Option chain error:", e)

        return None
