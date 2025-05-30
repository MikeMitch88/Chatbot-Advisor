"""
CryptoBuddy Pro - API Utilities
Handles CoinGecko API integration for real-time cryptocurrency data
"""

import requests
import time
from datetime import datetime
from colorama import Fore, Style

class CoinGeckoAPI:
    """CoinGecko API wrapper for cryptocurrency data"""
    
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.last_refresh = None
        self.cache = {}
        self.cache_duration = 300  # 5 minutes cache
        
    def _make_request(self, endpoint, params=None):
        """Make a request to the CoinGecko API with error handling"""
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}❌ API Error: {e}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}❌ Unexpected error: {e}{Style.RESET_ALL}")
            return None
    
    def get_coin_price(self, coin_id, vs_currency="usd"):
        """Get current price for a specific coin"""
        cache_key = f"price_{coin_id}_{vs_currency}"
        
        # Check cache first
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        endpoint = "simple/price"
        params = {
            "ids": coin_id,
            "vs_currencies": vs_currency,
            "include_24hr_change": "true",
            "include_market_cap": "true",
            "include_24hr_vol": "true"
        }
        
        data = self._make_request(endpoint, params)
        if data and coin_id in data:
            result = data[coin_id]
            self.cache[cache_key] = result
            self.cache[f"{cache_key}_timestamp"] = time.time()
            self.last_refresh = datetime.now()
            return result
        return None
    
    def get_trending_coins(self):
        """Get trending cryptocurrencies"""
        cache_key = "trending"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        endpoint = "search/trending"
        data = self._make_request(endpoint)
        
        if data and "coins" in data:
            trending = data["coins"]
            self.cache[cache_key] = trending
            self.cache[f"{cache_key}_timestamp"] = time.time()
            self.last_refresh = datetime.now()
            return trending
        return None
    
    def get_top_coins(self, limit=10, vs_currency="usd"):
        """Get top cryptocurrencies by market cap"""
        cache_key = f"top_coins_{limit}_{vs_currency}"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        endpoint = "coins/markets"
        params = {
            "vs_currency": vs_currency,
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": "false"
        }
        
        data = self._make_request(endpoint, params)
        if data:
            self.cache[cache_key] = data
            self.cache[f"{cache_key}_timestamp"] = time.time()
            self.last_refresh = datetime.now()
            return data
        return None
    
    def get_coin_details(self, coin_id):
        """Get detailed information about a specific coin"""
        cache_key = f"details_{coin_id}"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        endpoint = f"coins/{coin_id}"
        params = {
            "localization": "false",
            "tickers": "false",
            "market_data": "true",
            "community_data": "false",
            "developer_data": "false",
            "sparkline": "false"
        }
        
        data = self._make_request(endpoint, params)
        if data:
            self.cache[cache_key] = data
            self.cache[f"{cache_key}_timestamp"] = time.time()
            self.last_refresh = datetime.now()
            return data
        return None
    
    def _is_cache_valid(self, cache_key):
        """Check if cached data is still valid"""
        timestamp_key = f"{cache_key}_timestamp"
        if cache_key in self.cache and timestamp_key in self.cache:
            return time.time() - self.cache[timestamp_key] < self.cache_duration
        return False
    
    def format_price(self, price):
        """Format price with appropriate decimal places"""
        if price is None:
            return "N/A"
        
        if price >= 1:
            return f"${price:,.2f}"
        elif price >= 0.01:
            return f"${price:.4f}"
        else:
            return f"${price:.8f}"
    
    def format_market_cap(self, market_cap):
        """Format market cap in readable format"""
        if market_cap is None:
            return "N/A"
        
        if market_cap >= 1e12:
            return f"${market_cap/1e12:.2f}T"
        elif market_cap >= 1e9:
            return f"${market_cap/1e9:.2f}B"
        elif market_cap >= 1e6:
            return f"${market_cap/1e6:.2f}M"
        elif market_cap >= 1e3:
            return f"${market_cap/1e3:.2f}K"
        else:
            return f"${market_cap:.2f}"
    
    def format_change(self, change):
        """Format price change with color coding"""
        if change is None:
            return "N/A"
        
        if change >= 0:
            return f"{Fore.GREEN}+{change:.2f}%{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}{change:.2f}%{Style.RESET_ALL}"
    
    def get_last_refresh_time(self):
        """Get the last data refresh time"""
        if self.last_refresh:
            return self.last_refresh.strftime("%Y-%m-%d %H:%M:%S")
        return "Never"
