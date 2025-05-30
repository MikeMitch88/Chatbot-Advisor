"""
CryptoBuddy Pro - NLP Utilities
Natural Language Processing for query understanding and intent detection
"""

import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from colorama import Fore, Style


nltk.download('vader_lexicon')

class NLPProcessor:
    """Natural Language Processing utilities for CryptoBuddy Pro"""
    
    def __init__(self):
        """Initialize NLP components"""
        self.lemmatizer = WordNetLemmatizer()
        self.sia = SentimentIntensityAnalyzer()
        
        # Download required NLTK data
        self._download_nltk_data()
        
        # Load stop words
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            self.stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'])
        
        # Define intent patterns
        self.intent_patterns = {
            'price_query': [
                r'\b(price|cost|value|worth)\b.*\b(of|for)\b',
                r'\bhow much\b.*\bcost\b',
                r'\bwhat.*price\b',
                r'\bcurrent.*price\b'
            ],
            'comparison': [
                r'\bcompare\b.*\bvs?\b',
                r'\bcompare\b.*\band\b',  
                r'\bdifference.*between\b',
                r'\bwhich.*better\b',
                r'\b(vs|versus)\b'
            ],
            'trending': [
                r'\btrending\b',
                r'\bhot\b.*\bcoin\b',
                r'\bpopular\b.*\bcrypto\b',
                r'\bwhat.*rising\b',
                r'\btop.*coin\b'
            ],
            'sustainable': [
                r'\bsustainable\b',
                r'\bgreen\b.*\bcrypto\b',
                r'\beco.?friendly\b',
                r'\benvironmental\b',
                r'\blow.*energy\b'
            ],
            'low_risk': [
                r'\blow.?risk\b',
                r'\bsafe\b.*\binvestment\b',
                r'\bstable\b.*\bcoin\b',
                r'\bconservative\b',
                r'\bsecure\b.*\boption\b'
            ],
            'advice': [
                r'\bshould.*invest\b',
                r'\brecommend\b',
                r'\badvice\b',
                r'\bsuggest\b',
                r'\bbest.*buy\b'
            ],
            'top_coins': [
                r'\btop\b.*\d+',
                r'\bbest\b.*\d+',
                r'\\klargest\b.*\d+',
                r'\blist.*coin\b'
            ]
        }
        
        # Cryptocurrency name patterns
        self.crypto_patterns = [
            r'\bbitcoin\b', r'\bbtc\b',
            r'\bethereum\b', r'\beth\b', 
            r'\bcardano\b', r'\bada\b',
            r'\bsolana\b', r'\bsol\b',
            r'\bpolygon\b', r'\bmatic\b',
            r'\balgorand\b', r'\balgo\b',
            r'\bchainlink\b', r'\blink\b',
            r'\blitecoin\b', r'\bltc\b',
            r'\bstellar\b', r'\bxlm\b',
            r'\btezos\b', r'\bxtz\b'
        ]
    
    def _download_nltk_data(self):
        """Download required NLTK data"""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            print(f"{Fore.YELLOW}📥 Downloading NLTK data...{Style.RESET_ALL}")
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        
        try:
            nltk.data.find('corpora/omw-1.4')
        except LookupError:
            nltk.download('omw-1.4', quiet=True)
        
        try:
            nltk.data.find('vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon', quiet=True)
    
    def preprocess_text(self, text):
        """Preprocess text: tokenize, remove stop words, lemmatize"""
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize
        try:
            tokens = word_tokenize(text)
        except:
            # Fallback tokenization
            tokens = re.findall(r'\b\w+\b', text)
        
        # Remove stop words and lemmatize
        processed_tokens = []
        for token in tokens:
            if token not in self.stop_words and len(token) > 2:
                try:
                    lemmatized = self.lemmatizer.lemmatize(token)
                    processed_tokens.append(lemmatized)
                except:
                    processed_tokens.append(token)
        
        return processed_tokens
    
    def detect_intent(self, text):
        """Detect user intent from text"""
        text = text.lower()
        detected_intents = []
        
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    detected_intents.append(intent)
                    break
        
        return detected_intents if detected_intents else ['general_query']
    
    def extract_cryptocurrencies(self, text):
        """Extract cryptocurrency names/symbols from text"""
        text = text.lower()
        found_cryptos = []
        
        for pattern in self.crypto_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            found_cryptos.extend(matches)
        
        # Remove duplicates and normalize
        unique_cryptos = []
        for crypto in found_cryptos:
            crypto = crypto.lower()
            if crypto not in [c.lower() for c in unique_cryptos]:
                unique_cryptos.append(crypto)
        
        return unique_cryptos
    
    def extract_numbers(self, text):
        """Extract numbers from text"""
        numbers = re.findall(r'\b\d+\b', text)
        return [int(num) for num in numbers]
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of the text"""
        try:
            scores = self.sia.polarity_scores(text)
            
            # Determine overall sentiment
            if scores['compound'] >= 0.05:
                sentiment = 'positive'
            elif scores['compound'] <= -0.05:
                sentiment = 'negative' 
            else:
                sentiment = 'neutral'
            
            return {
                'sentiment': sentiment,
                'confidence': abs(scores['compound']),
                'scores': scores
            }
        except:
            return {
                'sentiment': 'neutral',
                'confidence': 0.0,
                'scores': {'compound': 0.0, 'pos': 0.0, 'neu': 1.0, 'neg': 0.0}
            }
    
    def get_confidence_level(self, sentiment_analysis):
        """Get investment confidence level based on sentiment"""
        confidence = sentiment_analysis['confidence']
        sentiment = sentiment_analysis['sentiment']
        
        if sentiment == 'positive' and confidence > 0.7:
            return f"{Fore.GREEN}High Confidence 📈{Style.RESET_ALL}"
        elif sentiment == 'positive' and confidence > 0.3:
            return f"{Fore.YELLOW}Moderate Confidence 📊{Style.RESET_ALL}"
        elif sentiment == 'negative':
            return f"{Fore.RED}Low Confidence 📉{Style.RESET_ALL}"
        else:
            return f"{Fore.BLUE}Neutral 🔄{Style.RESET_ALL}"
    
    def normalize_crypto_name(self, crypto_name):
        """Normalize cryptocurrency name for database lookup"""
        crypto_name = crypto_name.lower().strip()
        
        # Handle common variations
        name_mappings = {
            'btc': 'bitcoin',
            'eth': 'ethereum', 
            'ada': 'cardano',
            'sol': 'solana',
            'matic': 'polygon',
            'algo': 'algorand',
            'link': 'chainlink',
            'ltc': 'litecoin',
            'xlm': 'stellar',
            'xtz': 'tezos'
        }
        
        return name_mappings.get(crypto_name, crypto_name)