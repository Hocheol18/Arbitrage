import threading
import requests
import time, datetime
import os, certifi
from binance.websocket.spot.websocket_client \
    import SpotWebsocketClient as WebsocketClient

os.environ['SSL_CERT_FILE'] = certifi.where()
ws_client = WebsocketClient()

tickers = []

def message_handler(message):
    global tickers
    try:
        tickers = list(
            filter(lambda Tickers: Tickers['s'].endswith("USDT"), message)
        )
    except:
        pass

    return tickers

ws_client.start()

ws_client.ticker(id=1, callback=message_handler)

def getKrwRate():
    try:
        res = requests.get(
            "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"
        )
        return res.json()
    except:
        return None

def getAllKRW():
    res = requests.get("https://api.bithumb.com/public/ticker/ALL_KRW").json()['data']
    KRWbox = []
    for key, value in res.items():
        if key == "date":
            continue
        KRWbox.append(key)
    return KRWbox
    
def getAllTickers(symbols):
    res = requests.get("https://api.bithumb.com/public/orderbook/ALL_KRW")
    Tickers = []
    for i in symbols:
        Tickers.append(res.json()['data'][f"{i}"]['order_currency'] + str(res.json()['data'][f"{i}"]['bids'][0]) + str(res.json()['data'][f"{i}"]['asks'][0]))
    return Tickers

class BithumbThread(threading.Thread):
    def __init__(self):
        super(BithumbThread, self).__init__()
        self.daemon = True

        self.KRWsymbols = getAllKRW()
        self.KRWTickers = []
        self.binanceData = []

    def run(self):
        while True:
            self.KRWTickers = getAllTickers(self.KRWsymbols)
            krwRate = getKrwRate()[0]["basePrice"]
            binanceTicker = message_handler(message=ws_client.ticker(id=1, callback=message_handler))

            try:
                self.binanceData = list(
                    map(
                        lambda ticker : {
                            "symbol": ticker["s"][:-4],
                            "price": float(ticker["c"]) * krwRate
                        },
                        binanceTicker
                    )
                )

            except:
                pass

            time.sleep(10)

bithumbthread = BithumbThread()
bithumbthread.start()
target = 2

remove_box = ["XNO"]
pre_hour = datetime.datetime.now().hour
while True:
    if datetime.datetime.now().hour != pre_hour:
        break
    try:
        numbers = 0
        avg_KRW = 0
        for tickers in bithumbthread.KRWTickers:
            ticker = tickers.replace("}", "").split("{")
            symbol = ticker[0]
            KrwPrice = ((float(ticker[1].split("'")[3]) + float(ticker[2].split("'")[3])) / 2)
            
            BinanceTicker = list(
                filter(lambda d: d['symbol'] == symbol, bithumbthread.binanceData)
            )
            
            try:
                if symbol not in remove_box:
                    BinancePrice = BinanceTicker[0]['price']
                    if (float(KrwPrice) - float(BinancePrice)) / float(BinancePrice) * 100 >= target or (float(KrwPrice) - float(BinancePrice)) / float(BinancePrice) * 100 <= -target:
                        print(f"ALERT :: {symbol}\nBithumb :: {round(float(KrwPrice))} Binance :: {round(float(BinancePrice),3)}\nGAP :: {round((float(KrwPrice) - float(BinancePrice)) / float(BinancePrice) * 100,3)}%\n")
                        avg_KRW += round((float(KrwPrice) - float(BinancePrice)) / float(BinancePrice) * 100,3)
                    else:
                        avg_KRW += round((float(KrwPrice) - float(BinancePrice)) / float(BinancePrice) * 100,3)
                    numbers += 1
            except:
                pass

        if numbers != 0:
            print(f"연우홀릭은 신이야 :: {round(avg_KRW/numbers, 3)}")

        time.sleep(10)
    except:
        pass