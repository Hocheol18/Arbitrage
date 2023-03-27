import ccxt
import requests
import time
from datetime import datetime

def discord(res):
    discord = 'https://discord.com/api/webhooks/1079663426126749727/O__d9cO0aqlt-RM3mQK0_bLya6cRXc0XNWWkaVvnIBWTgexlspigN4JL3BpgQvin30f3'

    headers = {
        'Content-Type': 'application/json'
    }
    data = '{"content":" %s"}' % (res)
    return requests.post(discord, headers=headers, data=data)

phemex = ccxt.phemex()

bingx_data = ['BTC-USDT','ETH-USDT','LINK-USDT','BCH-USDT','EOS-USDT','ADA-USDT','XRP-USDT','LTC-USDT','XTZ-USDT','DOT-USDT','AVAX-USDT','THETA-USDT','ALGO-USDT','AXS-USDT','DYDX-USDT','OMG-USDT','CELR-USDT',
'MATIC-USDT','SHIB-USDT','ICP-USDT','SAND-USDT','KSM-USDT','VET-USDT','SUSHI-USDT','SOL-USDT','NEAR-USDT','ATOM-USDT','UNI-USDT','FIL-USDT','AAVE-USDT','DOGE-USDT','ENJ-USDT','MANA-USDT','CHZ-USDT',
'TRX-USDT','SKL-USDT','ZRX-USDT','BAL-USDT','BAND-USDT','SNX-USDT','FTM-USDT','CRV-USDT','LRC-USDT','YFI-USDT','MKR-USDT','1INCH-USDT','COMP-USDT','GRT-USDT','MASK-USDT','AR-USDT','ANT-USDT','ENS-USDT',
'BAT-USDT','STORJ-USDT','IOTX-USDT','IMX-USDT','XLM-USDT','ZEC-USDT','DASH-USDT','XMR-USDT','WAVES-USDT','ONT-USDT','ONE-USDT','EGLD-USDT','HBAR-USDT','CELO-USDT','KAVA-USDT','BNB-USDT','GALA-USDT',
'C98-USDT','ALICE-USDT','APE-USDT','KNC-USDT','ZIL-USDT','FLOW-USDT','KLAY-USDT','GMT-USDT','RUNE-USDT','RVN-USDT','IOST-USDT','ETC-USDT','ROSE-USDT','API3-USDT','PEOPLE-USDT','GAL-USDT','ANKR-USDT',
'OGN-USDT','LUNC-USDT','LUNA-USDT','OP-USDT','FLM-USDT','LDO-USDT','STG-USDT','INJ-USDT','BTCDOM-USDT','APT-USDT','QNT-USDT','BLUEBIRD-USDT','ARPA-USDT','SFP-USDT','BONK-USDT']

Bitget_data = ['BTCUSDT_UMCBL','ETHUSDT_UMCBL','XRPUSDT_UMCBL','EOSUSDT_UMCBL','BCHUSDT_UMCBL','LTCUSDT_UMCBL','ADAUSDT_UMCBL','ETCUSDT_UMCBL','LINKUSDT_UMCBL','TRXUSDT_UMCBL','DOTUSDT_UMCBL','DOGEUSDT_UMCBL',
'SOLUSDT_UMCBL','MATICUSDT_UMCBL','BNBUSDT_UMCBL','UNIUSDT_UMCBL','ICPUSDT_UMCBL','AAVEUSDT_UMCBL','FILUSDT_UMCBL','XLMUSDT_UMCBL','ATOMUSDT_UMCBL','XTZUSDT_UMCBL','SUSHIUSDT_UMCBL','AXSUSDT_UMCBL',
'THETAUSDT_UMCBL','FTMUSDT_UMCBL','AVAXUSDT_UMCBL','DASHUSDT_UMCBL','SHIBUSDT_UMCBL','MANAUSDT_UMCBL','GALAUSDT_UMCBL','SANDUSDT_UMCBL','DYDXUSDT_UMCBL','CRVUSDT_UMCBL','NEARUSDT_UMCBL','EGLDUSDT_UMCBL',
'KSMUSDT_UMCBL','ARUSDT_UMCBL','RENUSDT_UMCBL','PEOPLEUSDT_UMCBL','LRCUSDT_UMCBL','NEOUSDT_UMCBL','ALICEUSDT_UMCBL','WAVESUSDT_UMCBL','ALGOUSDT_UMCBL','IOTAUSDT_UMCBL','YFIUSDT_UMCBL','ENJUSDT_UMCBL',
'GMTUSDT_UMCBL','ZILUSDT_UMCBL','IOSTUSDT_UMCBL','APEUSDT_UMCBL','RUNEUSDT_UMCBL','KNCUSDT_UMCBL','APTUSDT_UMCBL','CHZUSDT_UMCBL','XMRUSDT_UMCBL','ROSEUSDT_UMCBL','ZRXUSDT_UMCBL','KAVAUSDT_UMCBL','ENSUSDT_UMCBL',
'GALUSDT_UMCBL','MTLUSDT_UMCBL','AUDIOUSDT_UMCBL','SXPUSDT_UMCBL','C98USDT_UMCBL','OPUSDT_UMCBL','RSRUSDT_UMCBL','SNXUSDT_UMCBL','STORJUSDT_UMCBL','1INCHUSDT_UMCBL','COMPUSDT_UMCBL','IMXUSDT_UMCBL','LUNA2USDT_UMCBL',
'FLOWUSDT_UMCBL','REEFUSDT_UMCBL','TRBUSDT_UMCBL','QTUMUSDT_UMCBL','API3USDT_UMCBL','MASKUSDT_UMCBL','WOOUSDT_UMCBL','GRTUSDT_UMCBL','BANDUSDT_UMCBL','STGUSDT_UMCBL','LUNCUSDT_UMCBL','ONEUSDT_UMCBL','JASMYUSDT_UMCBL',
'MKRUSDT_UMCBL','BATUSDT_UMCBL', 'HNTUSDT_UMCBL']

Mexc_data = ['BTC_USDT','ETH_USDT','SOL_USDT','ALPHA_USDT','LDO_USDT','DOGE_USDT','SRM_USDT','ETC_USDT','XRP_USDT','KAVA_USDT','LUNC_USDT','MATIC_USDT','LTC_USDT','NEAR_USDT','JASMY_USDT','APE_USDT','BNB_USDT',
'ATOM_USDT','ADA_USDT','CHZ_USDT','OP_USDT','BTC_USD','AVAX_USDT','ETH_USD','XRP_USD','DYDX_USDT','SHIB_USDT','MASK_USDT','FTM_USDT','LINK_USDT','WAVES_USDT','SAND_USDT','ANC_USDT','ATOM_USD','ETC_USD',
'CHZ_USD','BIT_USDT','FLOW_USDT','GMT_USDT','APT_USDT','REN_USDT','FILECOIN_USDT','OCEAN_USDT','ICP_USDT','DOT_USDT','ALGO_USDT','RLC_USDT','BONE_USDT','AXS_USDT','ETHW_USDT','BAND_USDT','COMP_USDT',
'RAY_USDT','AAVE_USDT','MANA_USDT','GALA_USDT','DC_USDT','EGLD_USDT','TRX_USDT','KSM_USDT','CTK_USDT','CRV_USDT','KAS_USDT','1INCH_USDT','VINU_USDT','HNT_USDT','XMR_USDT','FITFI_USDT','ANT_USDT',
'RVN_USDT','GMX_USDT','SUSHI_USDT','UNI_USDT','KLAY_USDT','ZEC_USDT','TWT_USDT','ENS_USDT','RUNE_USDT','DENT_USDT','SNX_USDT','DASH_USDT','BCH_USDT','USTC_USDT','MTL_USDT','GRT_USDT','HBAR_USDT','C98_USDT',
'MX_USDT','PEOPLE_USDT','TONCOIN_USDT','SFP_USDT','LUNANEW_USDT','GAL_USDT','CEEK_USDT','MKR_USDT','ALICE_USDT','WOO_USDT','EOS_USDT','VET_USDT','CELO_USDT','THETA_USDT','CEL_USDT','YFI_USDT','STORJ_USDT',
'IOTA_USDT','LRC_USDT','RSR_USDT','ENJ_USDT','COTI_USDT','DAR_USDT','OGN_USDT','NEO_USDT','ZIL_USDT','GLMR_USDT','TRB_USDT','XTZ_USDT','MAGIC_USDT','BAT_USDT','UNFI_USDT','REEF_USDT','AR_USDT','SNFT_USDT',
'ONT_USDT','ONE_USDT','IOTX_USDT','BAL_USDT','BLZ_USDT','KNC_USDT','HT_USDT','AUDIO_USDT','ROSE_USDT','XLM_USDT','YFII_USDT','BFT_USDT','BAKE_USDT','CRO_USDT','ANKR_USDT','HOT_USDT','IMX_USDT','PSG_USDT',
'INJ_USDT','API3_USDT','SANTOS_USDT','OSMO_USDT','LIT_USDT','LOOKS_USDT','OMG_USDT','ZRX_USDT','GTC_USDT','YGG_USDT','CVX_USDT','QTUM_USDT','CHR_USDT','SWEAT_USDT','IOST_USDT','SXP_USDT','LINA_USDT',
'FOOTBALL_USDT','ATA_USDT','RNDR_USDT','NKN_USDT','ARPA_USDT','FLM_USDT','DUSK_USDT','CVC_USDT','DGB_USDT','STG_USDT','STMX_USDT','CSPR_USDT','CELR_USDT','BSV_USDT','BEL_USDT','ACH_USDT','CTSI_USDT',
'MDX_USDT','CREAM_USDT','PERP_USDT','JST_USDT','UMA_USDT','DEGO_USDT', 'BONK_USDT', 'FLR_USDT']

Huobi_data = ['MANA-USDT','SHIB-USDT','CHZ-USDT','DOT-USDT','SOL-USDT','YFI-USDT','CTSI-USDT','EOS-USDT','UNI-USDT','LUNA-USDT','FIL-USDT','GRT-USDT','C98-USDT','JST-USDT','AAVE-USDT','OP-USDT','REN-USDT',
'LUNC-USDT','1INCH-USDT','ETHW-USDT','KSM-USDT','MATIC-USDT','DOGE-USDT','ICP-USDT','ETH-USDT','QNT-USDT','THETA-USDT','NEAR-USDT','GMT-USDT','BTC-USDT','XRP-USDT','AXS-USDT','ENS-USDT',
'BNB-USDT','GAL-USDT','ETC-USDT','PEOPLE-USDT','ONE-USDT','SUSHI-USDT','FTM-USDT','BCH-USDT','APE-USDT','LTC-USDT','CRV-USDT','IMX-USDT','KAVA-USDT','AVAX-USDT','SNX-USDT','LINK-USDT',
'ALGO-USDT','WAVES-USDT','JASMY-USDT','APT-USDT','TRX-USDT','LRC-USDT','WIN-USDT','HT-USDT','DYDX-USDT','SAND-USDT','ATOM-USDT','ADA-USDT']

CoinEX_data = ['ONTUSDT','KAVAUSDT','ATOMUSDT','GRTUSDT','OMGUSDT','LUNAUSDT','BATUSDT','ONEUSDT','DASHUSDT','MKRUSDT','KSMUSDT','ZENUSDT','LINKUSDT','XTZUSDT','HOTUSDT','IOTXUSDT','LTCUSDT',
'DOTUSDT','BTCUSD','XRPUSDT','NFTUSDT','1INCHUSDT','HBARUSDT','LRCUSDT','ALGOUSDT','LPTUSDT','IOTAUSDT','SOLUSDT','ZECUSDT','RNDRUSDT','AAVEUSDT','NEOUSDT','FTMUSDT','SNXUSDT','IOSTUSDT','CHZUSDT',
'WOOUSDT','YFIUSDT','AUDIOUSDT','NEARUSDT','DOGEUSDT','ARUSDT','RENUSDT','ADAUSDT','RUNEUSDT','MASKUSDT','BTCUSDT','RSRUSDT','KDAUSDT','ETHUSDT',
'ELONUSDT','MATICUSDT','CAKEUSDT','ICPUSDT','FLOWUSDT','THETAUSDT','TRXUSDT','MINAUSDT','ETHUSD','QTUMUSDT','ANKRUSDT','FILUSDT','WAVESUSDT','WAXPUSDT',
'ICXUSDT','CELOUSDT','ZRXUSDT','BTTUSDT','SXPUSDT','ENSUSDT','ROSEUSDT','AXSUSDT','BNBUSDT','IMXUSDT','BCHUSDT','GMTUSDT','AVAXUSDT','COMPUSDT','ENJUSDT','ZILUSDT','ETCUSDT',
'GALAUSDT','STORJUSDT','VETUSDT','CRVUSDT','SANDUSDT','XECUSDT','SKLUSDT','SUSHIUSDT','EOSUSDT','MANAUSDT','HNTUSDT','EGLDUSDT',
'DYDXUSDT','APEUSDT','UNIUSDT','XLMUSDT','SCRTUSDT','APTUSDT','LUNCUSDT','XMRUSDT','SHIBUSDT']

Bybit_data = ['10000NFTUSDT','1000BONKUSDT','1000BTTUSDT','1000LUNCUSDT','1000XECUSDT','1INCHUSDT','AAVEUSDT','ACHUSDT','ADAUSD','ADAUSDT','AGLDUSDT','AKROUSDT','ALGOUSDT','ALICEUSDT','ALPHAUSDT',
'ANCUSDT','ANKRUSDT','ANTUSDT','APEUSDT','API3USDT','APTUSDT','ARPAUSDT','ARUSDT','ASTRUSDT','ATOMUSDT','AUDIOUSDT','AVAXUSDT','AXSUSDT','BAKEUSDT','BALUSDT','BANDUSDT','BATUSDT','BCHUSDT','BELUSDT',
'BICOUSDT','BITUSD','BITUSDT','BLZUSDT','BNBUSDT','BNXUSDT','BOBAUSDT','BSVUSDT','BSWUSDT','BTCUSD','BTCUSDH22','BTCUSDH23','BTCUSDM22','BTCUSDM23','BTCUSDT','BTCUSDU21','BTCUSDU22','BTCUSDZ21',
'BTCUSDZ22','BTTUSDT','C98USDT','CEEKUSDT','CELOUSDT','CELRUSDT','CHRUSDT','CHZUSDT','CKBUSDT','COMPUSDT','COTIUSDT','CREAMUSDT','CROUSDT','CRVUSDT','CTCUSDT','CTKUSDT','CTSIUSDT','CVCUSDT','CVXUSDT',
'DARUSDT','DASHUSDT','DENTUSDT','DGBUSDT','DODOUSDT','DOGEUSDT','DOTUSD','DOTUSDT','DUSKUSDT','DYDXUSDT','EGLDUSDT','ENJUSDT','ENSUSDT','EOSUSD','EOSUSDT','ETCUSDT','ETHUSD','ETHUSDH22','ETHUSDH23',
'ETHUSDM22','ETHUSDM23','ETHUSDT','ETHUSDU21','ETHUSDU22','ETHUSDZ21','ETHUSDZ22','ETHWUSDT','FILUSDT','FITFIUSDT','FLMUSDT','FLOWUSDT','FTMUSDT','FTTUSDT','FXSUSDT','GALAUSDT','GALUSDT','GLMRUSDT',
'GMTUSDT','GMXUSDT','GRTUSDT','GSTUSDT','GTCUSDT','HBARUSDT','HNTUSDT','HOTUSDT','ICPUSDT','ICXUSDT','ILVUSDT','IMXUSDT','INJUSDT','IOSTUSDT','IOTAUSDT','IOTXUSDT','JASMYUSDT','JSTUSDT','KAVAUSDT',
'KDAUSDT','KEEPUSDT','KLAYUSDT','KNCUSDT','KSMUSDT','LDOUSDT','LINAUSDT','LINKUSDT','LITUSDT','LOOKSUSDT','LPTUSDT','LRCUSDT','LTCUSD','LTCUSDT','LUNA2USDT','LUNAUSD','LUNAUSDT','MAGICUSDT','MANAUSD',
'MANAUSDT','MASKUSDT','MATICUSDT','MINAUSDT','MKRUSDT','MTLUSDT','NEARUSDT','NEOUSDT','OCEANUSDT','OGNUSDT','OMGUSDT','ONEUSDT','ONTUSDT','OPUSDT','PAXGUSDT','PEOPLEUSDT','QTUMUSDT','RAYUSDT','REEFUSDT',
'RENUSDT','REQUSDT','RNDRUSDT','ROSEUSDT','RSRUSDT','RSS3USDT','RUNEUSDT','RVNUSDT','SANDUSDT','SCRTUSDT','SCUSDT','SFPUSDT','SHIB1000USDT','SKLUSDT','SLPUSDT','SNXUSDT','SOLUSD','SOLUSDT','SPELLUSDT',
'SRMUSDT','STGUSDT','STMXUSDT','STORJUSDT','STXUSDT','SUNUSDT','SUSHIUSDT','SWEATUSDT','SXPUSDT','THETAUSDT','TLMUSDT','TOMOUSDT','TRBUSDT','TRXUSDT','TWTUSDT','UNFIUSDT','UNIUSDT','USDCUSDT','USTUSDT',
'VETUSDT','WAVESUSDT','WOOUSDT','XCNUSDT','XEMUSDT','XLMUSDT','XMRUSDT','XNOUSDT','XRPUSD','XRPUSDT','XTZUSDT','YFIUSDT','YGGUSDT','ZECUSDT','ZENUSDT','ZILUSDT','ZRXUSDT']

Okx_data = ['ETC-USDT-SWAP','CRV-USDT-SWAP','SUSHI-USDT-SWAP','XLM-USDT-SWAP','DASH-USDT-SWAP','MATIC-USDT-SWAP','THETA-USDT-SWAP','CRO-USDT-SWAP','LTC-USDT-SWAP','UNI-USDT-SWAP','WAVES-USDT-SWAP',
'APE-USDT-SWAP','STORJ-USDT-SWAP','USTC-USDT-SWAP','XMR-USD-SWAP','ENJ-USDT-SWAP','IOST-USDT-SWAP','BTC-USDT-SWAP','BNB-USDT-SWAP','APT-USDT-SWAP','SNX-USDT-SWAP','NEO-USDT-SWAP','AVAX-USDT-SWAP',
'LPT-USDT-SWAP','SAND-USD-SWAP','RSR-USDT-SWAP','ZEC-USD-SWAP','KNC-USDT-SWAP','XLM-USD-SWAP','LINK-USDT-SWAP','DOGE-USDT-SWAP','DORA-USDT-SWAP','NFT-USDT-SWAP','COMP-USDT-SWAP','PERP-USDT-SWAP',
'YFI-USD-SWAP','UNI-USD-SWAP','MKR-USDT-SWAP','BADGER-USDT-SWAP','SOL-USD-SWAP','THETA-USD-SWAP','GRT-USDT-SWAP','DOME-USDT-SWAP','AVAX-USD-SWAP','DOT-USD-SWAP','FIL-USDT-SWAP','FIL-USD-SWAP',
'ETH-USDT-SWAP','SHIB-USDT-SWAP','FLM-USDT-SWAP','MINA-USDT-SWAP','LUNC-USDT-SWAP','ENS-USDT-SWAP','IMX-USDT-SWAP','XTZ-USDT-SWAP','BSV-USDT-SWAP','EOS-USDT-SWAP','CVC-USDT-SWAP','CRV-USD-SWAP',
'LRC-USDT-SWAP','DYDX-USDT-SWAP','OP-USDT-SWAP','KISHU-USDT-SWAP','SLP-USDT-SWAP','CHZ-USDT-SWAP','SUSHI-USD-SWAP','JST-USDT-SWAP','GODS-USDT-SWAP','LTC-USD-SWAP','BCH-USDT-SWAP','TON-USDT-SWAP',
'ATOM-USDT-SWAP','ETHW-USDT-SWAP','YGG-USDT-SWAP','AAVE-USDT-SWAP','EGLD-USDT-SWAP','AGLD-USDT-SWAP','ONT-USDT-SWAP','TRX-USD-SWAP','ALGO-USDT-SWAP','ADA-USDT-SWAP','BTC-USDC-SWAP','GALA-USDT-SWAP',
'LUNA-USDT-SWAP','XRP-USD-SWAP','ADA-USD-SWAP','ETC-USD-SWAP','MANA-USD-SWAP','SAND-USDT-SWAP','CELO-USDT-SWAP','TRX-USDT-SWAP','BTC-USD-SWAP','KLAY-USDT-SWAP','OMG-USDT-SWAP','LOOKS-USDT-SWAP',
'EOS-USD-SWAP','1INCH-USD-SWAP','MANA-USDT-SWAP','GRT-USD-SWAP','DASH-USD-SWAP','SWEAT-USDT-SWAP','BICO-USDT-SWAP','ICP-USDT-SWAP','BAND-USDT-SWAP','ZEC-USDT-SWAP','ZRX-USDT-SWAP','QTUM-USDT-SWAP',
'CSPR-USDT-SWAP','YFI-USDT-SWAP','CEL-USDT-SWAP','1INCH-USDT-SWAP','SOL-USDT-SWAP','ETH-USD-SWAP','ETH-USDC-SWAP','ATOM-USD-SWAP','STARL-USDT-SWAP','DOT-USDT-SWAP','API3-USDT-SWAP','NEO-USD-SWAP',
'ALPHA-USDT-SWAP','DOGE-USD-SWAP','BAT-USDT-SWAP','REN-USDT-SWAP','LINK-USD-SWAP','PEOPLE-USDT-SWAP','IOTA-USDT-SWAP','TRB-USDT-SWAP','RVN-USDT-SWAP','XCH-USDT-SWAP','ALGO-USD-SWAP','GMT-USDT-SWAP',
'KSM-USD-SWAP','KSM-USDT-SWAP','ZIL-USDT-SWAP','YFII-USDT-SWAP','CFX-USDT-SWAP','MASK-USDT-SWAP','BCH-USD-SWAP','UMA-USDT-SWAP','ZEN-USDT-SWAP','NEAR-USDT-SWAP','FTM-USDT-SWAP','FITFI-USDT-SWAP',
'XRP-USDT-SWAP','BNT-USDT-SWAP','BAL-USDT-SWAP','BSV-USD-SWAP','ANT-USDT-SWAP','AXS-USDT-SWAP','XMR-USDT-SWAP']

DeepCoin_data = ['1INCH-USDT','AAVE-USDT','ADA-USDT','ALGO-USDT','ALICE-USDT','ANC-USDT','ANV-USDT','APE-USDT','APT-USDT','AR-USDT',
'ARG-USDT','ATM-USDT','ATOM-USDT','AVAX-USDT','AXS-USDT','BABYDOGE-USDT','BAND-USDT','BAR-USDT','BAT-USDT','BCH-USDT','BEAM-USDT',
'BLZ-USDT','BNB-USDT','BNX-USDT','BSV-USDT','BTC-USDT','BTK-USDT','BTTC-USDT','BUSD-USDT','C98-USDT','CAKE-USDT','CELO-USDT','CHZ-USDT',
'CITY-USDT','COMP-USDT','COTI-USDT','CPET-USDT','CRO-USDT','CRV-USDT','CTSI-USDT','DAI-USDT','DAR-USDT','DASH-USDT','DC-USDT',
'DENT-USDT','DF-USDT','DFI-USDT','DG-USDT','DODO-USDT','DOGE-USDT','DORA-USDT','DOT-USDT','DYDX-USDT','EGLD-USDT','ENJ-USDT',
'ENS-USDT','EOS-USDT','ETC-USDT','ETH-USDT','ETHW-USDT','EVMOS-USDT','FIL-USDT','FIO-USDT','FIRO-USDT','FLOKI-USDT','FLOW-USDT',
'FTM-USDT','FTT-USDT','FWC-USDT','GAL-USDT','GALA-USDT','GMT-USDT','GMX-USDT','HFT-USDT','HNT-USDT','HOOK-USDT','HOT-USDT','HT-USDT',
'ICP-USDT','ICX-USDT','IMX-USDT','INJ-USDT','IOST-USDT','IOTA-USDT','IOTX-USDT','JASMY-USDT','JST-USDT','KAVA-USDT','KDA-USDT',
'KEY-USDT','KLAY-USDT','KLV-USDT','KNC-USDT','KSM-USDT','KUBE-USDT','LAZIO-USDT','LDO-USDT','LEVER-USDT','LINA-USDT','LINK-USDT',
'LRC-USDT','LTC-USDT','LUNA-USDT','LUNC-USDT','MANA-USDT','MASK-USDT','MATIC-USDT','MENGO-USDT','MEV-USDT','MINA-USDT','MKR-USDT',
'MOB-USDT','NEAR-USDT','NEO-USDT','NEXO-USDT','NUM-USDT','OMG-USDT','ONE-USDT','OP-USDT','ORC-USDT','OSMO-USDT','PAX-USDT','PAXG-USDT',
'PEOPLE-USDT','PERP-USDT','PHA-USDT','PI-USDT','PIT-USDT','POR-USDT','PORTO-USDT','PROM-USDT','PSG-USDT','QI-USDT','QNT-USDT',
'QUICK-USDT','RAD-USDT','REEF-USDT','REN-USDT','ROSE-USDT','RUNE-USDT','RXBX-USDT','SAITAMA-USDT','SAMO-USDT','SAND-USDT','SANTOS-USDT',
'SFP-USDT','SHIB-USDT','SKL-USDT','SLP-USDT','SNX-USDT','SOL-USDT','SOLO-USDT','SPS-USDT','SRLTY-USDT','SRM-USDT','STG-USDT',
'STORJ-USDT','STX-USDT','SUSHI-USDT','TAMA-USDT','THETA-USDT','TORN-USDT','TRB-USDT','TRX-USDT','TWT-USDT','UMA-USDT','UNI-USDT',
'USDC-USDT','USDP-USDT','UST-USDT','VELO-USDT','VET-USDT','VINU-USDT','VOLT-USDT','WAXP-USDT','WOO-USDT','XCH-USDT','XEC-USDT',
'XEN-USDT','XETA-USDT','XLM-USDT','XMR-USDT','XRP-USDT','XTZ-USDT','YFI-USDT','YFII-USDT','YGG-USDT','ZEC-USDT','ZEN-USDT','ZIL-USDT',
'ZRX-USDT']

target_price = 0.2
res = ''
res += ("Binance  :::  ")

for i in requests.get("https://fapi.binance.com/fapi/v1/premiumIndex").json():
    if float(i['lastFundingRate'])*100 >= target_price or float(i['lastFundingRate'])*100 <= -target_price:
        res += (i['symbol'] + " " + str(round(float(i['lastFundingRate'])*100, 4)) + "%" + " // ")
discord(res=res)

res = ''
res += ("Phemex  :::  ")

b = requests.get("https://api.phemex.com/public/products").json()['data']['products']
b = list(map(lambda x:x['symbol'], b))

for i in b:
    if i[0] == 's' or i[0] == 'u':
        i = i[1::]
    try:
        funding = phemex.fetch_funding_rate(i)
        if float(funding['info']['fundingRateRr']) * 100 >= target_price or float(funding['info']['fundingRateRr']) * 100 <= -target_price or float(funding['info']['predFundingRateRr']) *100 >= target_price or float(funding['info']['predFundingRateRr']) *100 <= -target_price:
            res += (i + ' ' + 'Cur' + ' ' + str(round(float(funding['info']['fundingRateRr'])*100, 3)) + "%" + ' ' + 'Nex' + ' ' + str(round(float(funding['info']['predFundingRateRr'])*100, 3)) + "%" + ' ' + 'Vol' +  ' ' + funding['info']['volumeRq'] + " // ")
    except:
        continue
discord(res=res)

res = ''
res += ("Bitget  :::  ")

for i in Bitget_data:
    try:
        b = 'https://api.bitget.com/api/mix/v1/market/current-fundRate?symbol=' + i
        data = requests.get(b)
        if float(data.json()['data']['fundingRate'])*100 >= target_price or float(data.json()['data']['fundingRate'])*100 <= -target_price:
            res += (i[:-6] + " " + ":" + " " + str(round(float(data.json()['data']['fundingRate'])*100, 3)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''
res += ("MEXC  :::  ")

b = requests.get("https://contract.mexc.com/api/v1/contract/funding_rate/").json()['data']
for q in b:
    c = round(float(q['fundingRate'])*100,4)
    if c >= target_price or c <= -target_price:
        res += (q['symbol'] + ":" + " " + str(c) + "%" + " // ")
discord(res=res)

res = ''
res += ("Kucoin  :::  ")

b = "https://api-futures.kucoin.com/api/v1/contracts/active"
for i in requests.get(b).json()['data']:
    try:
        if float(i['fundingFeeRate'])*100 >= target_price or float(i['fundingFeeRate'])*100 <= -target_price or float(i['predictedFundingFeeRate'])*100 >= target_price or float(i['predictedFundingFeeRate'])*100 <= -target_price:
            res += (i['symbol'] + " Cur : " + str(round(float(i['fundingFeeRate'])*100, 5)) + "%  " + "Nex : " + str(round(float(i['predictedFundingFeeRate'])*100, 5)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''

# print("--------------------------------------")
# print("Woox")
# print("--------------------------------------")

# c = "https://api.woo.org/v1/public/funding_rates"
# data = requests.get(c)
# for i in data.json()['rows']:
#     if float(i['est_funding_rate'])*100*8 >= target_price or float(i['est_funding_rate'])*100*8 <= -target_price:
#         print(i['symbol'][5::] + " :" + " 8hr " + str(round(float(i['est_funding_rate'])*100*8, 5)) + "%" + "  " + "1hr" + " "+ str(round(float(i['est_funding_rate'])*100, 5)) + "%")

res += ("Huobi  :::  ")


for i in Huobi_data:
    try:
        b = "https://api.hbdm.com/linear-swap-api/v1/swap_funding_rate?contract_code=" + i
        if float(requests.get(b).json()['data']['funding_rate'])*100 >= target_price or float(requests.get(b).json()['data']['funding_rate'])*100 <= -target_price:
            res += (i + " " + str(round(float(requests.get(b).json()['data']['funding_rate'])*100,5)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''

# print("--------------------------------------")
# print("BTCEX")
# print("--------------------------------------")

# a = requests.get("https://www.btcex.com/api/v1/public/coin_gecko_contracts").json()
# for i in a['result']:
#     if float(i['funding_rate'])*100 >= target_price or float(i['funding_rate'])*100 <= -target_price:
#         res += (i['ticker_id'] + " " + str(round(float(i['funding_rate'])*100,5))+"%")
res += ("CoinEx  :::  ")

for i in CoinEX_data:
    try:
        if float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]["funding_rate_predict"])*100 >= target_price or float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]["funding_rate_predict"])*100 <= -target_price or float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]['funding_rate_next'])*100 >= target_price or float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]['funding_rate_next'])*100 <= -target_price:
            res += (i + " " + "Cur : " + str(round(float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]['funding_rate_next'])*100, 5)) + "%" + "   Nex : " + " " + str(round(float(requests.get("https://api.coinex.com/perpetual/v1/market/ticker/all").json()['data']['ticker'][i]["funding_rate_predict"])*100, 5)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''
res += ("Gate.io  :::  ")

for i in requests.get("https://api.gateio.ws/api/v4/futures/usdt/tickers").json():
    try:
        if float(i['funding_rate']) * 100 >= target_price or float(i['funding_rate']) * 100 <= -target_price:
            res += (i['contract'] + " " + str(round(float(i['funding_rate'])*100, 5)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''
res += ("Okx  :::  ")

for i in Okx_data:
    try:
        a = 'https://www.okx.com/api/v5/public/funding-rate?instId=' + i
        if float(requests.get(a).json()['data'][0]['fundingRate'])*100 >= target_price or float(requests.get(a).json()['data'][0]['fundingRate'])*100 <= -target_price or float(requests.get(a).json()['data'][0]['nextFundingRate'])*100 >= target_price or float(requests.get(a).json()['data'][0]['nextFundingRate'])*100 <= -target_price:
            res += (i + " " + "Cur : " + str(round(float(requests.get(a).json()['data'][0]['fundingRate'])*100,5)) + "%" + " " + "   Nex : " + str(round(float(requests.get(a).json()['data'][0]['nextFundingRate'])*100,5)) + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''
res += ("Bingx  :::  ")

for i in bingx_data:
    try:
        a = "https://api-swap-rest.bingbon.pro/api/v1/market/getLatestFunding?symbol=" + i
        if float(requests.get(a).json()['data']['fundingRate']) >= target_price or float(requests.get(a).json()['data']['fundingRate']) <= -target_price:
            res += (i + " " + requests.get(a).json()['data']['fundingRate'] + "%" + " // ")
    except:
        continue
discord(res=res)

res = ''
# print("--------------------------------------")
# print("XT_com")
# print("--------------------------------------")

# for i in XT_com_data:
#     a = "https://fapi.xt.com/future/market/v1/public/q/funding-rate?symbol=" + i
#     if float(requests.get(a).json()['result']['fundingRate'])*100 >= 0.1 or float(requests.get(a).json()['result']['fundingRate'])*100 <= -0.1:
#         print(requests.get(a).json()['result']['symbol'] + " " + str(round(float(requests.get(a).json()['result']['fundingRate'])*100, 5)) + "%")

res += ("Bybit  :::  ")
for i in Bybit_data:
    try:
        a = "https://api.bybit.com/derivatives/v3/public/tickers?symbol=" + i
        if float(requests.get(a).json()['result']['list'][0]['fundingRate'])*100 >= target_price or float(requests.get(a).json()['result']['list'][0]['fundingRate'])*100 <= -target_price:
            res += (requests.get(a).json()['result']['list'][0]['symbol'] + " " + str(round(float(requests.get(a).json()['result']['list'][0]['fundingRate'])*100, 5))+"%" + " // ")
    except:
        continue
discord(res=res)

# print("--------------------------------------")
# print("Kraken")
# print("--------------------------------------")

# for i in requests.get("https://futures.kraken.com/derivatives/api/v3/tickers").json()['tickers']:
#     try:
#         if round(i['fundingRate']*8, 5) >= target_price or round(i['fundingRate']*8, 5) <= -target_price or round(i['fundingRatePrediction']*8, 5) >= target_price or round(i['fundingRatePrediction']*8, 5) <= -target_price:
#             if i['pair'][:3] == "YFI" or i['pair'][:3] == 'XBT':
#                 continue
#             else:
#                 res += (i['pair'] + " Cur :: " + str(round(i['fundingRate'], 5)) + " Nex ::  " + str(round(i['fundingRatePrediction'], 5)))
#     except:
#         continue

print("DONE")