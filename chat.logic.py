"""
CryptoBuddy Pro - Chat Logic
Main chat processing and response generation
"""

import random
from datetime import datetime
from colorama import Fore, Style
from tabulate import tabulate
from api_utils import CoinGeckoAPI
from nlp_utils import NLPProcessor
from crypto_data import (
    CRYPTO_DATABASE, get_crypto_by_name, get_crypto_by_symbol,
    get_sustainable_cryptos, get_low_risk_cryptos, get_low_energy_cryptos,
    get_all_cryptos
)

class CryptoChatBot:
    """Main chatbot class for CryptoBuddy Pro"""
    
    def __init__(self):
        """Initialize the chatbot with API and NLP components"""
        self.api = CoinGeckoAPI()
        self.nlp = NLPProcessor()
        self.disclaimer = f"\n{Fore.RED}⚠️  Remember: Cryptocurrency investments are highly risky. Always do your own research!{Style.RESET_ALL}"
                # Friendly responses for various scenarios
        self.friendly_responses = {
            'greeting': [
                "Hello! I'm CryptoBuddy Pro, your crypto advisor! 🚀",
                "Hey there! Ready to explore the crypto world together? 💎",
                "Welcome! Let's dive into some cryptocurrency insights! 🌟"
            ],
            'fallback': [
                "I'm not sure I understand that completely. Could you rephrase your question?",
                "That's an interesting question! Could you be more specific?",
                "I'd love to help! Can you clarify what you're looking for?"
            ],
            'no_data': [
                "I couldn't find data for that cryptocurrency right now.",
                "That coin isn't in my database or the API might be having issues.",
                "I don't have information on that particular cryptocurrency."
            ]
        }
    
    def process_query(self, user_input):
        """Process user query and generate appropriate response"""
        try:
            # Analyze sentiment
            sentiment = self.nlp.analyze_sentiment(user_input)
            
            # Detect intents
            intents = self.nlp.detect_intent(user_input)
            
            # Extract cryptocurrencies mentioned
            mentioned_cryptos = self.nlp.extract_cryptocurrencies(user_input)
            
            # Extract numbers (for top N queries)
            numbers = self.nlp.extract_numbers(user_input)
            
            # Process based on detected intents
            response = ""
            
            if 'price_query' in intents:
                response = self._handle_price_query(mentioned_cryptos)
            elif 'comparison' in intents:
                response = self._handle_comparison(mentioned_cryptos)
            elif 'trending' in intents:
                response = self._handle_trending_query()
            elif 'sustainable' in intents:
                response = self._handle_sustainable_query()
            elif 'low_risk' in intents:
                response = self._handle_low_risk_query()
            elif 'top_coins' in intents:
                limit = numbers[0] if numbers else 5
                response = self._handle_top_coins_query(limit)
            elif 'advice' in intents:
                response = self._handle_advice_query(mentioned_cryptos, sentiment)
            else:
                response = self._handle_general_query(user_input, mentioned_cryptos)
            
            # Add sentiment-based confidence if it's investment-related
            if any(intent in intents for intent in ['advice', 'comparison', 'sustainable', 'low_risk']):
                confidence = self.nlp.get_confidence_level(sentiment)
                response += f"\n\n💡 Market Sentiment: {confidence}"
            
            return response + self.disclaimer
            
        except Exception as e:
            return f"I encountered an error processing your request: {e}{self.disclaimer}"
    
    def _handle_price_query(self, cryptos):
        """Handle price-related queries"""
        if not cryptos:
            return "Please specify which cryptocurrency you'd like to know the price of!"
        
        responses = []
        for crypto_name in cryptos:
            normalized_name = self.nlp.normalize_crypto_name(crypto_name)
            crypto_data = get_crypto_by_name(normalized_name)
            
            if crypto_data:
                price_data = self.api.get_coin_price(crypto_data['coingecko_id'])
                if price_data:
                    price = self.api.format_price(price_data.get('usd'))
                    change = self.api.format_change(price_data.get('usd_24h_change'))
                    market_cap = self.api.format_market_cap(price_data.get('usd_market_cap'))
                    
                    response = f"""
{crypto_data['icon']} **{crypto_data['name']} ({crypto_data['symbol']})**
💰 Current Price: {price}
📈 24h Change: {change}
🏆 Market Cap: {market_cap}
📅 Founded: {crypto_data['launch_year']} by {crypto_data['founder']}
"""
                    responses.append(response)
                else:
                    responses.append(f"❌ Sorry, I couldn't fetch current price data for {crypto_data['name']}.")
            else:
                responses.append(f"❌ I don't have information about '{crypto_name}' in my database.")
        
        return "\n".join(responses) if responses else random.choice(self.friendly_responses['no_data'])
    
    def _handle_comparison(self, cryptos):
        """Handle cryptocurrency comparison queries"""
        if len(cryptos) < 2:
            return "Please specify at least two cryptocurrencies to compare!"
        
        comparison_data = []
        valid_cryptos = []
        
        for crypto_name in cryptos[:3]:  # Limit to 3 for readability
            normalized_name = self.nlp.normalize_crypto_name(crypto_name)
            crypto_data = get_crypto_by_name(normalized_name)
            
            if crypto_data:
                price_data = self.api.get_coin_price(crypto_data['coingecko_id'])
                
                row = [
                    f"{crypto_data['icon']} {crypto_data['name']}",
                    crypto_data['symbol'],
                    self.api.format_price(price_data.get('usd') if price_data else None),
                    self.api.format_change(price_data.get('usd_24h_change') if price_data else None),
                    crypto_data['energy_use'].title(),
                    f"{crypto_data['sustainability_score']}/10",
                    crypto_data['risk_level'].title()
                ]
                comparison_data.append(row)
                valid_cryptos.append(crypto_data)
        
        if not comparison_data:
            return "I couldn't find data for the cryptocurrencies you mentioned."
        
        headers = ["Cryptocurrency", "Symbol", "Price", "24h Change", "Energy Use", "Sustainability", "Risk Level"]
        table = tabulate(comparison_data, headers=headers, tablefmt="grid")
        
        return f"📊 **Cryptocurrency Comparison**\n```\n{table}\n```"
    
    def _handle_trending_query(self):
        """Handle trending cryptocurrency queries"""
        trending = self.api.get_trending_coins()
        
        if not trending:
            return "❌ I couldn't fetch trending data right now. Please try again later."
        
        response = "🔥 **Trending Cryptocurrencies Right Now:**\n\n"
        
        for i, coin in enumerate(trending[:7], 1):
            coin_data = coin.get('item', {})
            name = coin_data.get('name', 'Unknown')
            symbol = coin_data.get('symbol', 'N/A')
            rank = coin_data.get('market_cap_rank', 'N/A')
            
            response += f"{i}. 🚀 **{name}** ({symbol})\n"
            response += f"   📊 Market Cap Rank: #{rank}\n\n"
        
        return response
    
    def _handle_sustainable_query(self):
        """Handle sustainability-related queries"""
        sustainable_cryptos = get_sustainable_cryptos(min_score=7)
        
        if not sustainable_cryptos:
            return "I don't have any cryptocurrencies with high sustainability scores in my database."
        
        response = "🌱 **Most Sustainable Cryptocurrency Options:**\n\n"
        
        sustainable_data = []
        for crypto in sustainable_cryptos:
            price_data = self.api.get_coin_price(crypto['coingecko_id'])
            price = self.api.format_price(price_data.get('usd') if price_data else None)
            
            row = [
                f"{crypto['icon']} {crypto['name']}",
                crypto['symbol'],
                price,
                crypto['energy_use'].replace('_', ' ').title(),
                f"{crypto['sustainability_score']}/10",
                crypto['consensus']
            ]
            sustainable_data.append(row)
        
        headers = ["Cryptocurrency", "Symbol", "Price", "Energy Use", "Sustainability", "Consensus"]
        table = tabulate(sustainable_data, headers=headers, tablefmt="grid")
        
        return f"{response}```\n{table}\n```\n\n💡 These cryptocurrencies use energy-efficient consensus mechanisms!"
    
    def _handle_low_risk_query(self):
        """Handle low-risk investment queries"""
        low_risk_cryptos = get_low_risk_cryptos()
        
        if not low_risk_cryptos:
            return "Based on my analysis, I don't have any cryptocurrencies classified as low-risk. Remember, all crypto investments carry significant risk!"
        
        response = "🛡️ **Lower Risk Cryptocurrency Options:**\n\n"
        
        risk_data = []
        for crypto in low_risk_cryptos:
            price_data = self.api.get_coin_price(crypto['coingecko_id'])
            price = self.api.format_price(price_data.get('usd') if price_data else None)
            market_cap = self.api.format_market_cap(price_data.get('usd_market_cap') if price_data else None)
            
            row = [
                f"{crypto['icon']} {crypto['name']}",
                crypto['symbol'],
                price,
                market_cap,
                crypto['risk_level'].title(),
                str(crypto['launch_year'])
            ]
            risk_data.append(row)
        
        headers = ["Cryptocurrency", "Symbol", "Price", "Market Cap", "Risk Level", "Est. Year"]
        table = tabulate(risk_data, headers=headers, tablefmt="grid")
        
        return f"{response}```\n{table}\n```\n\n⚠️ Even 'low-risk' crypto investments can be volatile!"
    
    def _handle_top_coins_query(self, limit=5):
        """Handle top cryptocurrencies queries"""
        top_coins = self.api.get_top_coins(limit=min(limit, 20))
        
        if not top_coins:
            return "❌ I couldn't fetch the top cryptocurrencies right now. Please try again later."
        
        response = f"🏆 **Top {len(top_coins)} Cryptocurrencies by Market Cap:**\n\n"
        
        top_data = []
        for i, coin in enumerate(top_coins, 1):
            name = coin.get('name', 'Unknown')
            symbol = coin.get('symbol', 'N/A').upper()
            price = self.api.format_price(coin.get('current_price'))
            change = self.api.format_change(coin.get('price_change_percentage_24h'))
            market_cap = self.api.format_market_cap(coin.get('market_cap'))
            
            row = [i, f"{name}", symbol, price, change, market_cap]
            top_data.append(row)
        
        headers = ["Rank", "Name", "Symbol", "Price", "24h Change", "Market Cap"]
        table = tabulate(top_data, headers=headers, tablefmt="grid")
        
        return f"{response}```\n{table}\n```"
    
    def _handle_advice_query(self, cryptos, sentiment):
        """Handle investment advice queries"""
        response = "💡 **CryptoBuddy Pro Investment Insights:**\n\n"
        
        if cryptos:
            # Specific crypto advice
            for crypto_name in cryptos:
                normalized_name = self.nlp.normalize_crypto_name(crypto_name)
                crypto_data = get_crypto_by_name(normalized_name)
                
                if crypto_data:
                    price_data = self.api.get_coin_price(crypto_data['coingecko_id'])
                    
                    response += f"{crypto_data['icon']} **{crypto_data['name']} Analysis:**\n"
                    response += f"🎯 Risk Level: {crypto_data['risk_level'].title()}\n"
                    response += f"🌱 Sustainability Score: {crypto_data['sustainability_score']}/10\n"
                    response += f"⚡ Energy Usage: {crypto_data['energy_use'].replace('_', ' ').title()}\n"
                    
                    if price_data:
                        change = price_data.get('usd_24h_change', 0)
                        if change > 5:
                            response += f"📈 Strong upward momentum (+{change:.2f}%)\n"
                        elif change < -5:
                            response += f"📉 Experiencing downward pressure ({change:.2f}%)\n"
                        else:
                            response += f"📊 Relatively stable movement ({change:.2f}%)\n"
                    
                    response += f"📝 {crypto_data['description']}\n\n"
        else:
            # General advice
            response += "🎯 **General Investment Principles:**\n\n"
            response += "1. 🏦 **Diversification**: Don't put all eggs in one basket\n"
            response += "2. 📚 **Research**: Understand the technology and team\n"
            response += "3. 💰 **Risk Management**: Only invest what you can afford to lose\n"
            response += "4. 🕐 **Long-term Thinking**: Crypto markets are highly volatile\n"
            response += "5. 🌱 **Consider Sustainability**: Look at environmental impact\n\n"
            
            # Suggest some balanced options
            sustainable = get_sustainable_cryptos()[:2]
            if sustainable:
                response += "🌿 **Sustainable Options to Consider:**\n"
                for crypto in sustainable:
                    response += f"• {crypto['icon']} {crypto['name']} - {crypto['description']}\n"
        
        return response
    
    def _handle_general_query(self, user_input, cryptos):
        """Handle general queries and fallback responses"""
        if any(word in user_input.lower() for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.friendly_responses['greeting'])
        
        if cryptos:
            # If cryptos are mentioned, provide general info
            responses = []
            for crypto_name in cryptos:
                normalized_name = self.nlp.normalize_crypto_name(crypto_name)
                crypto_data = get_crypto_by_name(normalized_name)
                
                if crypto_data:
                    response = f"\n{crypto_data['icon']} **{crypto_data['name']} ({crypto_data['symbol']}) Overview:**\n"
                    response += f"📅 Founded: {crypto_data['launch_year']} by {crypto_data['founder']}\n"
                    response += f"📝 {crypto_data['description']}\n"
                    response += f"🔧 Consensus: {crypto_data['consensus']}\n"
                    response += f"🌱 Sustainability: {crypto_data['sustainability_score']}/10\n"
                    responses.append(response)
            
            return "\n".join(responses) if responses else random.choice(self.friendly_responses['no_data'])
        
        return random.choice(self.friendly_responses['fallback'])
    
    def show_status(self):
        """Show system status and last refresh time"""
        status = f"""
{Fore.CYAN}📊 **CryptoBuddy Pro System Status**{Style.RESET_ALL}

🕐 Last Data Refresh: {self.api.get_last_refresh_time()}
📈 API Status: {'✅ Connected' if self.api else '❌ Disconnected'}
🧠 NLP Engine: ✅ Active
💾 Local Database: {len(CRYPTO_DATABASE)} cryptocurrencies
🌐 Cache Status: {'✅ Active' if self.api.cache else '❌ Empty'}

{Fore.GREEN}System is running normally!{Style.RESET_ALL}
"""
        print(status)
	
