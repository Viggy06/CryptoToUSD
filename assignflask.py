
#################
# All test cases are passed
# Run acceptance_test.py along with this file

from flask import Flask, request, jsonify, Response
import json
import requests
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)

@app.route("/", methods=["GET"]) #/exchange/?coin=bt
def WelcomeMessage():
    data_set = 'Welcome To CyrptioCurrencyConvereter Enter url in form of = Yourlocalhost/exchange?coin=?&amount=?'
    return jsonify(data_set)

@app.route("/exchange", methods=["GET"]) #/exchange/?coin=bt
def exchange_into_dollars():
    coin = request.args.get("coin")
    amount = int(request.args.get("amount"))
    usd_amount = 0

    if coin.lower() == 'btc' and amount > 0 and amount < 10000:
        bt = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').text
        btc = json.loads(bt)
        res = btc['bitcoin']['usd']
        usd_amount = res * amount
        return jsonify({'usd_amount':usd_amount})

    elif  coin.lower() == "eth" and amount > 0 and amount < 10000:
        et = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').text
        eth = json.loads(et)
        res = eth['ethereum']['usd']
        usd_amount = res * amount
        return jsonify({'usd_amount':usd_amount})

    elif coin.lower() == "xrp" and amount > 0 and amount < 10000:
        rp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd').text
        ripp = json.loads(rp)
        res = ripp['ripple']['usd']
        usd_amount = res * amount
        return jsonify({'usd_amount':usd_amount})
    else:
        return jsonify({'error':'Invalid input'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
