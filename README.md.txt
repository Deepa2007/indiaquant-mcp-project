# 📈 IndiaQuant MCP Server

A Model Context Protocol (MCP) server for financial market analysis built using FastAPI.
This project exposes APIs that provide stock analytics such as RSI, sentiment analysis, stock price data, and options max pain calculations.

The server is designed to integrate with AI agents or financial dashboards that require real-time market insights.

---

# 🚀 Features

* 📊 Stock Price API – Fetch latest stock price using Yahoo Finance
* 📉 RSI Indicator – Calculate Relative Strength Index for technical analysis
* 📰 Market Sentiment Analysis – Analyze news or text sentiment
* 🧮 Options Max Pain– Determine max pain strike price
* ⚡ FastAPI-based MCP server– Lightweight and high performance

---

# 🏗️ Project Structure

```
indiaquant-mcp
│
├── mcp_server.py        # Main MCP server
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/indiaquant-mcp.git
cd indiaquant-mcp
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the MCP Server

Start the FastAPI server:

```bash
uvicorn mcp_server:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## Home

```
GET /
```

Response:

```json
{
  "message": "IndiaQuant MCP Server Running"
}
```

---

## Get Stock Price

```
GET /stock-price?symbol=AAPL
```

Example response:

```json
{
  "symbol": "AAPL",
  "price": 193.45
}
```

---

## Calculate RSI

```
GET /rsi?symbol=AAPL
```

Example response:

```json
{
  "symbol": "AAPL",
  "rsi": 61.2
}
```

---

## Sentiment Analysis

```
POST /sentiment
```

Request body:

```json
{
  "text": "Stock market looks bullish today"
}
```

Response:

```json
{
  "sentiment": "positive"
}
```

---

## Options Max Pain

```
GET /max-pain?symbol=AAPL
```

Returns estimated max pain strike price.

---

# 🧰 Tech Stack

* Python
* FastAPI
* Pandas
* yfinance
* TextBlob
* Uvicorn

---

# 🧠 What is MCP?

Model Context Protocol (MCP) allows AI systems and agents to interact with external tools and APIs.
This server acts as a financial data provider that AI assistants can query to perform market analysis.

---

# 📌 Future Improvements

* Add MACD indicator
* Add Moving Averages
* Real-time news sentiment
* Portfolio analytics
* Options Greeks calculation

---

# 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

GitHub: https://github.com/Deepa2007
