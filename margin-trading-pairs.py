import requests

def get_margin_trading_pairs():
    exchange_info_url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(exchange_info_url)
    
    if response.status_code == 200:
        exchange_info = response.json()
        
        margin_trading_pairs = [
            symbol['symbol'] for symbol in exchange_info['symbols'] 
            if symbol['status'] == 'TRADING' and symbol['isMarginTradingAllowed']
        ]

        return margin_trading_pairs
    else:
        print(f"Failed to retrieve exchange information. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    margin_pairs = get_margin_trading_pairs()

    print("Trading-enabled margin pairs:")
    for pair in margin_pairs:
        print(pair)

    print(f"\nTotal number of trading pairs: {len(margin_pairs)}")
