import requests

def get_futures_trading_pairs():
    exchange_info_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    response = requests.get(exchange_info_url)
    
    if response.status_code == 200:
        exchange_info = response.json()
        
        futures_trading_pairs = [
            symbol['symbol'] for symbol in exchange_info['symbols'] 
            if symbol['status'] == 'TRADING'
        ]

        return futures_trading_pairs
    else:
        print(f"Failed to retrieve exchange information. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    futures_pairs = get_futures_trading_pairs()

    print("Trading-enabled futures pairs:")
    for pair in futures_pairs:
        print(pair)

    print(f"\nTotal number of trading pairs: {len(futures_pairs)}")
