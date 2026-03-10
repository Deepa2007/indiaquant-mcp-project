from fastapi import FastAPI

from market_data import get_market_data
from strategy import trading_strategy
from option_chain import analyze_option_chain
from greeks import analyze_option


app = FastAPI(title="Quant Trading MCP Server")


@app.get("/market-data")
def market_data(symbol: str):
    return get_market_data(symbol)


@app.get("/strategy")
def strategy(symbol: str):
    return trading_strategy(symbol)


@app.get("/option-chain")
def option_chain(symbol: str):
    return analyze_option_chain(symbol)


@app.get("/analyze")
def analyze(symbol: str):
    return analyze_option(symbol)
