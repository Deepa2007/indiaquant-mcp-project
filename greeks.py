import yfinance as yf
import math
from scipy.stats import norm
from utils import safe_float


def calculate_greeks(S, K, T, r, sigma):

    d1 = (math.log(S/K) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1)/(S*sigma*math.sqrt(T))
    theta = -(S*norm.pdf(d1)*sigma)/(2*math.sqrt(T))
    vega = S*norm.pdf(d1)*math.sqrt(T)

    return delta, gamma, theta, vega


def analyze_option(symbol):

    try:

        ticker = yf.Ticker(symbol)

        price = ticker.history(period="1d")["Close"].iloc[-1]

        strike = round(price/5)*5

        sigma = 0.25
        r = 0.05
        T = 30/365

        delta, gamma, theta, vega = calculate_greeks(price, strike, T, r, sigma)

        return {

            "symbol": symbol,
            "spot_price": safe_float(price),
            "atm_strike": safe_float(strike),
            "implied_volatility": safe_float(sigma),

            "greeks": {

                "delta": safe_float(delta),
                "gamma": safe_float(gamma),
                "theta": safe_float(theta),
                "vega": safe_float(vega)

            }

        }

    except Exception as e:

        return {
            "symbol": symbol,
            "error": str(e)
        }
