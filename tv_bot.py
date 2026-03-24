from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8330193239:AAFRc1VOGxzUwWLsoZVzR_-0TuM5BITdHyU"
CHAT_ID = "970135168"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    symbol = data.get("symbol", "Unknown")
    signal = data.get("signal", "No Signal")

    message = f"""
🚀 TRADINGVIEW SIGNAL

📊 Pair: {symbol}
📈 Signal: {signal}
"""

    send_telegram(message)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
