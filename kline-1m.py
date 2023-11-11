import asyncio
from binance import AsyncClient, BinanceSocketManager

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)

    # start any sockets here, i.e., a trade socket
    ts = bm.kline_socket('BTCUSDT', AsyncClient.KLINE_INTERVAL_1MINUTE)

    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            if res['e'] == 'kline' and res['k']['x']:
                # Check if it's a kline event and if it's the end of the candle
                print("Candle closed:", res)
                # Add your logic here for what you want to do when a candle closes

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(AsyncClient.close_connection())
        loop.close()
