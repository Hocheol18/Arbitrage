import requests
from datetime import datetime

def discord(symbol, price_1, price_2, gap):
    discord = 'https://discord.com/api/webhooks/1082219760122597376/sXOloEvxKm0y7TszvpxOhbuI41X5kwYvXaGT1b7_nJmeS74W5Y2rtzlkLenBg_2QEoo9'

    headers = {
        'Content-Type': 'application/json'
    }
    data = '{"content":" %s    Binance : %s    Bingx : %s    GAP :: %d"}' % (symbol, price_1, price_2, gap)
    return requests.post(discord, headers=headers, data=data)

def bing():
    bingx_symbol = list(requests.get("https://api-swap-rest.bingbon.pro/api/v1/market/getTicker").json()['data']['tickers'])
    BingxData = list(
        map(
        lambda ticker: {
        "symbol": ticker['symbol'][:-5],
        "trade_price": float(ticker['lastPrice'])
        }, bingx_symbol
        )
    )
    return BingxData

def binance():
    BinanceData = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr").json()
    return BinanceData

black_list = ["HNT", "ICP"]
import time, datetime
pre_hour = datetime.datetime.now().hour
while True:
    if datetime.datetime.now().hour != pre_hour:
        break
    BingxData, BinanceData = bing(), binance()

    for bingx in BingxData:
        symbol = bingx['symbol']
        price = bingx['trade_price']

        if symbol in black_list:
            continue

        total_data = list(
            filter(lambda d: d['symbol'][:-4]==symbol, BinanceData)
        )

        try:
            lastPrice = total_data[0]['lastPrice']
            if (float(lastPrice) - float(price)) / float(price) * 100 >= 1 or (float(lastPrice) - float(price)) / float(price) * 100 <= - 1:
                discord(symbol, lastPrice, price, (float(lastPrice) - float(price)) / float(price) * 100)
                
        except:
            pass

    time.sleep(3)