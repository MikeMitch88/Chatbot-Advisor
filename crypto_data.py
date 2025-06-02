"""
CryptoBuddy Pro - Local Cryptocurrency Database
Contains detailed information about various cryptocurrencies
"""

# Comprehensive cryptocurrency database with detailed information
CRYPTO_DATABASE = {
    "bitcoin": {
        "symbol": "BTC",
        "name": "Bitcoin",
        "coingecko_id": "bitcoin",
        "founder": "Satoshi Nakamoto",
        "launch_year": 2009,
        "energy_use": "high",
        "sustainability_score": 3,
        "risk_level": "medium",
        "description": "The first and largest cryptocurrency by market cap",
        "consensus": "Proof of Work",
        "icon": "₿"
    },
    "ethereum": {
        "symbol": "ETH",  
        "name": "Ethereum",
        "coingecko_id": "ethereum",
        "founder": "Vitalik Buterin",
        "launch_year": 2015,
        "energy_use": "medium",
        "sustainability_score": 6,
        "risk_level": "medium",
        "description": "Smart contract platform and second-largest cryptocurrency",
        "consensus": "Proof of Stake",
        "icon": "Ξ"
    },
    "cardano": {
        "symbol": "ADA",
        "name": "Cardano", 
        "coingecko_id": "cardano",
        "founder": "Charles Hoskinson",
        "launch_year": 2017,
        "energy_use": "low",
        "sustainability_score": 8,
        "risk_level": "medium",
        "description": "Research-driven blockchain platform focused on sustainability",
        "consensus": "Proof of Stake",
        "icon": "₳"
    },
    "solana": {
        "symbol": "SOL",
        "name": "Solana",
        "coingecko_id": "solana", 
        "founder": "Anatoly Yakovenko",
        "launch_year": 2020,
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "high",
        "description": "High-speed blockchain for decentralized apps",
        "consensus": "Proof of Stake + Proof of History",
        "icon": "◎"
    },
    "polygon": {
        "symbol": "MATIC",
        "name": "Polygon",
        "coingecko_id": "matic-network",
        "founder": "Jaynti Kanani",
        "launch_year": 2017,
        "energy_use": "very_low", 
        "sustainability_score": 9,
        "risk_level": "medium",
        "description": "Ethereum scaling solution with low energy consumption",
        "consensus": "Proof of Stake",
        "icon": "⬢"
    },
    "algorand": {
        "symbol": "ALGO",
        "name": "Algorand",
        "coingecko_id": "algorand",
        "founder": "Silvio Micali",
        "launch_year": 2019,
        "energy_use": "very_low",
        "sustainability_score": 9,
        "risk_level": "medium",
        "description": "Carbon-negative blockchain with pure proof-of-stake",
        "consensus": "Pure Proof of Stake",
        "icon": "◈"
    },
    "chainlink": {
        "symbol": "LINK",
        "name": "Chainlink",
        "coingecko_id": "chainlink",
        "founder": "Sergey Nazarov",
        "launch_year": 2017,
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "medium",
        "description": "Decentralized oracle network connecting blockchains to real-world data",
        "consensus": "Oracle Network",
        "icon": "🔗"
    },
    "litecoin": {
        "symbol": "LTC",
        "name": "Litecoin", 
        "coingecko_id": "litecoin",
        "founder": "Charlie Lee",
        "launch_year": 2011,
        "energy_use": "medium",
        "sustainability_score": 5,
        "risk_level": "low",
        "description": "Silver to Bitcoin's gold - faster transaction times",
        "consensus": "Proof of Work",
        "icon": "Ł"
    },
    "stellar": {
        "symbol": "XLM",
        "name": "Stellar",
        "coingecko_id": "stellar",
        "founder": "Jed McCaleb",
        "launch_year": 2014,
        "energy_use": "very_low",
        "sustainability_score": 9,
        "risk_level": "medium",
        "description": "Payment network for cross-border transactions",
        "consensus": "Stellar Consensus Protocol",
        "icon": "✦"
    },
    "tezos": {
        "symbol": "XTZ",
        "name": "Tezos",
        "coingecko_id": "tezos",
        "founder": "Arthur Breitman",
        "launch_year": 2018,
        "energy_use": "very_low", 
        "sustainability_score": 8,
        "risk_level": "medium",
        "description": "Self-amending blockchain with formal verification",
        "consensus": "Liquid Proof of Stake",
        "icon": "ꜩ"
    }
}

# Energy usage mapping for scoring
ENERGY_LEVELS = {
    "very_low": 1,
    "low": 2, 
    "medium": 3,
    "high": 4,
    "very_high": 5
}

# Risk level mapping
RISK_LEVELS = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "very_high": 4
}

def get_crypto_by_symbol(symbol):
    """Get cryptocurrency data by symbol"""
    symbol = symbol.upper()
    for crypto in CRYPTO_DATABASE.values():
        if crypto["symbol"] == symbol:
            return crypto
    return None

def get_crypto_by_name(name):
    """Get cryptocurrency data by name (case-insensitive)"""
    name = name.lower()
    if name in CRYPTO_DATABASE:
        return CRYPTO_DATABASE[name]
    
    # Try partial matching
    for key, crypto in CRYPTO_DATABASE.items():
        if name in key or name in crypto["name"].lower():
            return crypto
    return None

def get_sustainable_cryptos(min_score=7):
    """Get cryptocurrencies with high sustainability scores"""
    sustainable = []
    for crypto in CRYPTO_DATABASE.values():
        if crypto["sustainability_score"] >= min_score:
            sustainable.append(crypto)
    return sustainable

def get_low_risk_cryptos():
    """Get cryptocurrencies with low risk levels"""
    low_risk = []
    for crypto in CRYPTO_DATABASE.values():
        if crypto["risk_level"] == "low":
            low_risk.append(crypto)
    return low_risk

def get_low_energy_cryptos():
    """Get cryptocurrencies with low energy usage"""
    low_energy = []
    for crypto in CRYPTO_DATABASE.values():
        if crypto["energy_use"] in ["very_low", "low"]:
            low_energy.append(crypto)
    return low_energy

def get_all_cryptos():
    """Get all cryptocurrencies in the database"""
    return list(CRYPTO_DATABASE.values())