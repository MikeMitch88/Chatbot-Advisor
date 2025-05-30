# Chatbot-Advisor
CLI-based Cryptocurrency Advisor Chatbot
# 🚀 CryptoBuddy Pro - Advanced CLI Cryptocurrency Advisor

An intelligent command-line cryptocurrency advisor powered by AI, real-time data, and natural language processing.

## ✨ Features

- **🔴 Real-time Data**: Live cryptocurrency prices, market caps, and 24h changes via CoinGecko API
- **🧠 Natural Language Processing**: Understand queries using NLTK with sentiment analysis
- **📊 Rich Visualizations**: Colored terminal output, tables, and text-based graphics
- **🌱 Sustainability Focus**: Environmental impact analysis and green crypto recommendations
- **📈 Investment Insights**: Risk assessment, trend analysis, and personalized advice
- **💬 Smart Conversations**: Intent detection and context-aware responses
- **⚡ Performance**: Intelligent caching system for fast responses

## 🏗️ Project Structure

```
cryptobuddy-pro/
├── main.py           # Main application entry point
├── crypto_data.py    # Local cryptocurrency database
├── nlp_utils.py      # NLP processing and sentiment analysis
├── api_utils.py      # CoinGecko API integration
├── chat_logic.py     # Core chatbot logic and responses
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Internet connection (for real-time data)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download NLTK Data
The application will automatically download required NLTK data on first run, or you can pre-download:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
```

### Step 3: Run CryptoBuddy Pro
```bash
python main.py
```

## 💬 Usage Examples

### Price Queries
```
🧑 You: What's the price of Bitcoin?
🤖 CryptoBuddy Pro: ₿ **Bitcoin (BTC)**
💰 Current Price: $43,250.50
📈 24h Change: +2.45%
🏆 Market Cap: $847.2B
📅 Founded: 2009 by Satoshi Nakamoto
```

### Cryptocurrency Comparisons
```
🧑 You: Compare Ethereum vs Cardano
🤖 CryptoBuddy Pro: 📊 **Cryptocurrency Comparison**
┌──────────────────┬────────┬──────────┬───────────┬─────────────┬──────────────┬────────────┐
│ Cryptocurrency   │ Symbol │ Price    │ 24h Change│ Energy Use  │ Sustainability│ Risk Level │
├──────────────────┼────────┼──────────┼───────────┼─────────────┼──────────────┼────────────┤
│ Ξ Ethereum       │ ETH    │ $2,650.30│ +1.23%    │ Medium      │ 6/10         │ Medium     │
│ ₳ Cardano        │ ADA    │ $0.4850  │ +0.87%    │ Low         │ 8/10         │ Medium     │
└──────────────────┴────────┴──────────┴───────────┴─────────────┴──────────────┴────────────┘
```

### Sustainability Recommendations
```
🧑 You: Give me sustainable crypto options
🤖 CryptoBuddy Pro: 🌱 **Most Sustainable Cryptocurrency Options:**
┌──────────────────┬────────┬──────────┬─────────────┬──────────────┬─────────────────────────┐
│ Cryptocurrency   │ Symbol │ Price    │ Energy Use  │ Sustainability│ Consensus               │
├──────────────────┼────────┼──────────┼─────────────┼──────────────┼─────────────────────────┤
│ ⬢ Polygon        │ MATIC  │ $0.8945  │ Very Low    │ 9/10         │ Proof of Stake          │
│ ◈ Algorand       │ ALGO   │ $0.1678  │ Very Low    │ 9/10         │ Pure Proof of Stake     │
│ ₳ Cardano        │ ADA    │ $0.4850  │ Low         │ 8/10         │ Proof of Stake          │
└──────────────────┴────────┴──────────┴─────────────┴──────────────┴─────────────────────────┘
```

### Trending Cryptocurrencies
```
🧑 You: Which coins are trending?
🤖 CryptoBuddy Pro: 🔥 **Trending Cryptocurrencies Right Now:**

1. 🚀 **Solana** (SOL)
   📊 Market Cap Rank: #5

2. 🚀 **Chainlink** (LINK)
   📊 Market Cap Rank: #12

3. 🚀 **Polygon** (MATIC)
   📊 Market Cap Rank: #15
```

## 🎯 Supported Query Types

### Price & Market Data
- "What's the price of [cryptocurrency]?"
- "How much does Bitcoin cost?"
- "Current Ethereum price"

### Comparisons
- "Compare Bitcoin vs Ethereum"
- "Difference between Cardano and Solana"
- "Which is better: ADA or ALGO?"

### Investment Advice
- "Should I invest in Bitcoin?"
- "Recommend me a good cryptocurrency"
- "Best crypto to buy now"

### Sustainability & Environment
- "Most sustainable cryptocurrencies"
- "Green crypto options"
- "Low energy blockchain"

### Risk Assessment
- "Low risk cryptocurrency"
- "Safe crypto investment"
- "Conservative options"

### Market Trends
- "Top 10 cryptocurrencies"
- "Trending coins"
- "What's hot in crypto?"

## 🔧 Technical Features

### NLP Capabilities
- **Tokenization**: Break down user queries into meaningful components
- **Lemmatization**: Normalize words to their base forms
- **Stop Word Removal**: Filter out common words for better analysis
- **Intent Detection**: Understand what users are asking for
- **Sentiment Analysis**: Gauge user sentiment for investment confidence
- **Entity Extraction**: Identify cryptocurrency names and symbols

### API Integration
- **Real-time Data**: Live prices from CoinGecko API
- **Intelligent Caching**: 5-minute cache for optimal performance
- **Error Handling**: Graceful fallbacks when API is unavailable
- **Rate Limiting**: Respectful API usage

### Local Database
Rich cryptocurrency information including:
- Basic info (name, symbol, founder, launch year)
- Environmental impact (energy usage, sustainability score)
- Risk assessment and market classification
- Technical details (consensus mechanism)
- Descriptive information

## 📊 Cryptocurrency Database

Currently includes data for:
- Bitcoin (BTC) - The original cryptocurrency
- Ethereum (ETH) - Smart contract platform
- Cardano (ADA) - Research-driven blockchain
- Solana (SOL) - High-speed blockchain
- Polygon (MATIC) - Ethereum scaling solution
- Algorand (ALGO) - Carbon-negative blockchain
- Chainlink (LINK) - Decentralized oracle network
- Litecoin (LTC) - Digital silver
- Stellar (XLM) - Cross-border payment network
- Tezos (XTZ) - Self-amending blockchain

## 🎨 Visual Features

- **Colored Output**: Different colors for different types of information
- **Emojis & Icons**: Visual indicators for cryptocurrencies and sections
- **Tables**: Clean, formatted comparisons using tabulate
- **Progress Indicators**: Loading states and status updates
- **Consistent Branding**: Professional CryptoBuddy Pro theming

## ⚠️ Important Disclaimers

**CryptoBuddy Pro provides educational information only. Key points:**

- 🚫 **Not Financial Advice**: All information is for educational purposes
- ⚠️ **High Risk**: Cryptocurrency investments are extremely volatile
- 🔍 **Do Your Research**: Always conduct thorough research before investing
- 💰 **Risk Management**: Only invest what you can afford to lose
- 📊 **Market Volatility**: Crypto markets can change rapidly
- 🌐 **Regulatory Risk**: Cryptocurrency regulations vary by jurisdiction

## 🔧 Advanced Usage

### Command Line Options
```bash
python main.py              # Standard interactive mode
python main.py --help       # Show available options (if implemented)
```

### Available Commands Within the App
```
help     - Show available commands and examples
status   - Display system status and last data refresh
quit     - Exit CryptoBuddy Pro
exit     - Exit CryptoBuddy Pro
```

### Custom Queries
The NLP engine supports natural language, so you can ask questions like:
- "Tell me about the environmental impact of Bitcoin"
- "I'm looking for a stable investment option"
- "What's the difference in energy usage between Ethereum and Cardano?"
- "Show me the top 5 cryptocurrencies by market cap"

## 🚨 Troubleshooting

### Common Issues

**NLTK Data Not Found**
```
Solution: The app will auto-download NLTK data, but if issues persist:
python -c "import nltk; nltk.download('all')"
```

**API Connection Issues**
```
Check your internet connection
CoinGecko API might be temporarily unavailable
The app will show cached data when possible
```

**Import Errors**
```
Ensure all dependencies are installed:
pip install -r requirements.txt
```

**Performance Issues**
```
Clear cache by restarting the application
Check your internet connection speed
Consider using the app during off-peak hours
```

## 🌟 Contributing

We welcome contributions! Areas for improvement:
- Additional cryptocurrency data
- New query types and intents
- Enhanced sentiment analysis
- More sophisticated risk models
- Additional API integrations
- Improved error handling

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Support

For support, feature requests, or bug reports:
- Check the troubleshooting section
- Review the usage examples
- Ensure you have the latest version

---

**Remember: CryptoBuddy Pro is a tool for education and research. Always consult with financial professionals before making investment decisions!** 🚀💎
