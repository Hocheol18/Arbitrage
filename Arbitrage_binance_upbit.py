import threading
import requests
import datetime, time
import os, certifi
from binance.websocket.spot.websocket_client \
    import SpotWebsocketClient as WebsocketClient

os.environ['SSL_CERT_FILE'] = certifi.where()
ws_client = WebsocketClient()

def discord(res):
    discord = 'https://discord.com/api/webhooks/1082221772587417660/B8uFkDJ7ruDrl_vaw3m4BFtUoGl-zYTVT7UBr0mUMa6cclV11X_TjYcsYynBdy92Y_Sy'

    headers = {
        'Content-Type': 'application/json'
    }
    data = '{"content":" %s"}' % (res)
    return requests.post(discord, headers=headers, data=data)

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

def getAllMarket():
    try:
        res = requests.get("https://api.upbit.com/v1/market/all")
        return res.json()
    except:
        return None

def getTickers(markets):
    try:
        res = requests.get(f"https://api.upbit.com/v1/ticker?markets={markets}")
        return res.json()
    except:
        return None

def getKrwRate():
    try:
        res = requests.get(
            "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"
        )
        return res.json()
    except:
        return None

class UpbitThread(threading.Thread):
    def __init__(self):
        super(UpbitThread, self).__init__()
        self.daemon = True

        markets = getAllMarket()
        krwMarkets = list(
            filter(lambda market: market["market"].startswith("KRW-"), markets)
        )
        BTCMarkets = list(
            filter(lambda market: market["market"].startswith("BTC-"), markets)
        )
        self.KRWmarkets = list(map(lambda market: market["market"], krwMarkets))
        self.BTCmarkets = list(map(lambda market: market["market"], BTCMarkets))

        self.KRWsymbols = ",".join(self.KRWmarkets)
        self.BTCsymbols = ",".join(self.BTCmarkets)

        self.KRWupbitData = []
        self.BTCupbitData = []
        self.binanceData = []

    def run(self):
        while True:
            KRWBTC = getTickers("KRW-BTC")[0]['trade_price']
            currentKrwRate = getKrwRate()
            krwRate = currentKrwRate[0]["basePrice"]

            # Getting the upbit market datas
            self.KRWupbitData = getTickers(self.KRWsymbols)

            BTC_KRW_data = getTickers(self.BTCsymbols)

            self.BTCupbitData = list(
                map(
                    lambda ticker: {
                        "market": ticker["market"],
                        "trade_price": float(ticker["trade_price"]) * float(KRWBTC),
                    },
                    BTC_KRW_data
                )
            )
            
            # Getting the binance market datas
            binanceTickers = message_handler(message=ws_client.ticker(id=1, callback=message_handler))

            try:
                self.binanceData = list(
                    map(
                        lambda ticker: {
                            "symbol": ticker["s"][:-4],
                            "price": float(ticker["c"]) * krwRate,
                        },
                        binanceTickers
                    )
                )

            except:
                pass

            time.sleep(10)

upbitThread = UpbitThread()
upbitThread.start()
target_price = 4

remove_box = ['DENT']
pre_hour = datetime.datetime.now().hour

while True:
    if datetime.datetime.now().hour != pre_hour:
        break
    numbers = 0
    double_box = []
    avg_KRW, avg_BTC = 0, 0
    for binance in upbitThread.binanceData:
        symbol = binance["symbol"]
        price = binance["price"]
        
        UpbitdataKRW = list(
            filter(lambda d: d["market"][4:] == symbol, upbitThread.KRWupbitData)
        )
        
        res = ""
        # 원화 갭 차이
        try:
            if symbol not in remove_box:
                UpbitdataPriceKRW = UpbitdataKRW[0]["trade_price"]
                if (float(UpbitdataPriceKRW) - float(price)) / float(price) * 100 >= target_price or (float(UpbitdataPriceKRW) - float(price)) / float(price) * 100 <= -target_price:
                    avg_KRW += round((float(UpbitdataPriceKRW) - float(price)) / float(price) * 100, 5)
                    res += (f"KRW ALERT :: {symbol}   Binance :: {round(float(price),3)}  Upbit :: {round(float(UpbitdataPriceKRW),3)}  GAP :: {round((float(UpbitdataPriceKRW) - float(price)) / float(price) * 100, 5)}%")
                    discord(res=res)
                    double_box.append(symbol)
                else:
                    avg_KRW += round((float(UpbitdataPriceKRW) - float(price)) / float(price) * 100, 5)
                numbers += 1
        except:
            pass

    if numbers != 0:
        discord(res=f"KRW KIMP :: {round(avg_KRW/numbers, 3)}%")

    numbers = 0
    for binance in upbitThread.binanceData:
        symbol = binance["symbol"]
        price = binance["price"]

        UpbitdataBTC = list(
            filter(lambda d: d["market"][4:] == symbol, upbitThread.BTCupbitData)
        )

        res = ''

        # BTC 갭 차이
        try:
            if symbol not in double_box and symbol not in remove_box:
                UpbitdataPrice = UpbitdataBTC[0]["trade_price"]
                if (float(UpbitdataPrice) - float(price)) / float(price) * 100 >= target_price or (float(UpbitdataPrice) - float(price)) / float(price) * 100 <= -target_price:
                    avg_BTC += round((float(UpbitdataPrice) - float(price)) / float(price) * 100, 5)
                    res += (f"BTC ALERT :: {symbol}   Binance :: {round(float(price),3)}  Upbit :: {round(float(UpbitdataPrice),3)}  GAP :: {round((float(UpbitdataPrice) - float(price)) / float(price) * 100, 5)}%")
                    discord(res=res)
                else:
                    avg_BTC += round((float(UpbitdataPrice) - float(price)) / float(price) * 100, 5)
                numbers += 1
        except:
            pass

    if numbers != 0:
        discord(res=f"BTC KIMP :: {round(avg_BTC/numbers, 3)}%")
    
    time.sleep(10)