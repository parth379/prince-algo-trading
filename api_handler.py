import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AngelOneAPI:
    """Angel One Broker API Handler"""
    
    def __init__(self):
        self.api_key = os.getenv('ANGEL_ONE_API_KEY')
        self.auth_token = os.getenv('ANGEL_ONE_AUTH_TOKEN')
        self.user_id = os.getenv('ANGEL_ONE_USER_ID')
        self.base_url = "https://apiconnect.angelbroking.com"
    
    def get_historical_data(self, symbol, interval='1'):
        """
        Get historical data from Angel One
        interval: 1 = 1-min, 5 = 5-min, 15 = 15-min, 60 = 1-hour, daily = daily
        """
        try:
            endpoint = f"{self.base_url}/rest/secure/historicaldata"
            
            headers = {
                "Authorization": f"Bearer {self.auth_token}",
                "Content-Type": "application/json"
            }
            
            params = {
                "mode": "LTP",
                "exchangeTokens": f"{symbol}",
                "interval": interval
            }
            
            response = requests.get(endpoint, headers=headers, params=params)
            return response.json()
        except Exception as e:
            print(f"Error fetching data from Angel One: {e}")
            return None
    
    def place_order(self, symbol, qty, price, order_type='BUY', product='MIS'):
        """
        Place an order on Angel One
        order_type: BUY or SELL
        product: MIS (intraday) or CNC (delivery)
        """
        try:
            endpoint = f"{self.base_url}/rest/secure/orderplace"
            
            headers = {
                "Authorization": f"Bearer {self.auth_token}",
                "Content-Type": "application/json"
            }
            
            data = {
                "mode": "LTP",
                "exchangeTokens": symbol,
                "transactionType": order_type,
                "quantity": qty,
                "price": price,
                "product": product,
                "orderType": "MARKET"
            }
            
            response = requests.post(endpoint, headers=headers, json=data)
            return response.json()
        except Exception as e:
            print(f"Error placing order: {e}")
            return None
    
    def get_ltp(self, symbol):
        """Get Last Traded Price"""
        try:
            endpoint = f"{self.base_url}/rest/secure/ltp"
            headers = {
                "Authorization": f"Bearer {self.auth_token}"
            }
            params = {"mode": "LTP", "exchangeTokens": symbol}
            
            response = requests.get(endpoint, headers=headers, params=params)
            return response.json()
        except Exception as e:
            print(f"Error fetching LTP: {e}")
            return None


class DeltaExchangeAPI:
    """Delta Exchange (Crypto) API Handler"""
    
    def __init__(self):
        self.api_key = os.getenv('DELTA_API_KEY')
        self.api_secret = os.getenv('DELTA_API_SECRET')
        self.base_url = "https://api.delta.exchange"
    
    def get_historical_data(self, symbol, interval='1m'):
        """
        Get historical data from Delta Exchange
        interval: 1m, 5m, 15m, 1h, 1d
        """
        try:
            endpoint = f"{self.base_url}/v2/history/candles"
            
            headers = {
                "x-api-key": self.api_key,
                "Content-Type": "application/json"
            }
            
            params = {
                "symbol": symbol,
                "resolution": interval,
                "limit": 100
            }
            
            response = requests.get(endpoint, headers=headers, params=params)
            return response.json()
        except Exception as e:
            print(f"Error fetching data from Delta Exchange: {e}")
            return None
    
    def place_order(self, symbol, qty, price, side='buy'):
        """
        Place an order on Delta Exchange
        side: buy or sell
        """
        try:
            endpoint = f"{self.base_url}/v2/orders"
            
            headers = {
                "x-api-key": self.api_key,
                "Content-Type": "application/json"
            }
            
            data = {
                "product_id": symbol,
                "size": qty,
                "price": price,
                "side": side,
                "order_type": "limit_order"
            }
            
            response = requests.post(endpoint, headers=headers, json=data)
            return response.json()
        except Exception as e:
            print(f"Error placing order: {e}")
            return None
    
    def get_ticker(self, symbol):
        """Get current ticker data"""
        try:
            endpoint = f"{self.base_url}/v2/ticker/24hr"
            
            headers = {
                "x-api-key": self.api_key
            }
            
            params = {"symbol": symbol}
            
            response = requests.get(endpoint, headers=headers, params=params)
            return response.json()
        except Exception as e:
            print(f"Error fetching ticker: {e}")
            return None
