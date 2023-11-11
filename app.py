import binance.client 
from binance import ThreadedWebsocketManager

client = binance.client.Client()

bm = ThreadedWebsocketManager(client)

def process_message(msg):
    print(msg)

conn_key = bm.start_kline_socket('BTCUSDT', process_message, '1m')

bm.start()
