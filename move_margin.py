import hmac
import time
import hashlib
import requests
from urllib.parse import urlencode

KEY = ""
SECRET = ""
BASE_URL = "https://api.binance.com"

def dispatch_request(http_method):
    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": KEY}
    )
    return {
        "GET": session.get,
        "DELETE": session.delete,
        "PUT": session.put,
        "POST": session.post,
    }.get(http_method, "GET")

def hashing(query_string):
    return hmac.new(
        SECRET.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()

def get_timestamp():
    return int(time.time() * 1000)

def send_signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = "timestamp={}".format(get_timestamp())

    url = (
        BASE_URL + url_path + "?" + query_string + "&signature=" + hashing(query_string)
    )
    print("{} {}".format(http_method, url))
    params = {"url": url, "params": {}}
    response = dispatch_request(http_method)(**params)
    return response.json()

def m(coin, network, amount):
    response = send_signed_request("POST", "/sapi/v1/capital/withdraw/apply", {"coin":f"{coin}", "network":f"{network}", "address":"0x97FDf96F5AC0A37D3A49887E06B6Da73a959e9b5", "amount":f"{amount}"})
    print(response)

def u(coin, network, amount):
    response = send_signed_request("POST", "/sapi/v1/capital/withdraw/apply", {"coin":f"{coin}", "network":f"{network}", "address":"0xbd7fb7673ade8de1fb9ac278d65803b4071eb2c5", "amount":f"{amount}"})
    print(response)

def u_xrp(coin, network, address, memo, amount):
    response = send_signed_request("POST", "/sapi/v1/capital/withdraw/apply", {"coin":f"{coin}","network":f"{network}", "address":f"{address}", "addressTag":f"{memo}", "amount":f"{amount}"})
    print(response)

def b(coin, network, amount):
    response = send_signed_request("POST", "/sapi/v1/capital/withdraw/apply", {"coin":f"{coin}", "network":f"{network}", "address":"0x6f99a1c28c4543d3b424fec5e264c509daf4c776", "amount":f"{amount}"})
    print(response)

def mine(coin, network, address, amount):
    response = send_signed_request("POST", "/sapi/v1/capital/withdraw/apply", {"coin":f"{coin}", "network":f"{network}", "address":f"{address}", "amount":f"{amount}"})
    print(response)

def margin_loan(coin, amount):
    response = send_signed_request("POST", "/sapi/v1/margin/loan", {"asset":f"{coin}", "amount": f"{amount}"})
    print(response)

def margin_transfer(coin, amount, type):
    response = send_signed_request("POST", "/sapi/v1/margin/transfer", {"asset":f"{coin}", "amount":f"{amount}", "type":f"{type}"})
    print(response)

def call_back_func():
    margin_loan("XRP", "100")
    time.sleep(0.05)
    margin_transfer("XRP", "100", "2")
    time.sleep(1)
    u_xrp("XRP", "XRP", "raQwCVAJVqjrVm1Nj5SFRcX8i22BhdC9WA", "842967726", "99")

import time, datetime
pre_hour = datetime.datetime.now().minute










''' /sapi/v1/margin/transfer 

    asset   STRING  YES The asset being transferred, e.g., BTC
    amount  DECIMAL YES The amount to be transferred
    type    INT YES 1: transfer from main account to cross margin account 2: transfer from cross margin account to main account

    /sapi/v1/margin/loan

    asset   STRING  YES
    amount  DECIMAL YES

   /sapi/v1/margin/repay

    asset   STRING  YES
    amount  DECIMAL YES
'''

