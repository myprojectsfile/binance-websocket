import requests

def get_usdt_trading_pairs():
    # Binance API endpoint for exchange information
    exchange_info_url = "https://api.binance.com/api/v3/exchangeInfo"

    # Make a GET request to retrieve exchange information
    response = requests.get(exchange_info_url)
    
    if response.status_code == 200:
        exchange_info = response.json()
        
        # Filter out only spot trading pairs against USDT
        usdt_trading_pairs = [
            symbol['symbol'] for symbol in exchange_info['symbols'] 
            if symbol['status'] == 'TRADING' and symbol['quoteAsset'] == 'USDT'
        ]

        return usdt_trading_pairs
    else:
        print(f"Failed to retrieve exchange information. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    usdt_pairs = get_usdt_trading_pairs()

    print("Trading-enabled spot crypto USDT pairs:")
    for pair in usdt_pairs:
        print(pair)
        
    print(f"\nTotal number of trading pairs: {len(usdt_pairs)}")