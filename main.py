#!/usr/bin/env python3
"""
CryptoBuddy Pro - Advanced CLI Cryptocurrency Advisor Chatbot
Main application entry point
"""

import sys
import os
from datetime import datetime
from colorama import init, Fore, Style
from chat_logic import CryptoChatBot

def print_banner():
    """Display the CryptoBuddy Pro banner"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    🚀 CryptoBuddy Pro 🚀                     ║
║              Your AI-Powered Crypto Advisor                  ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}💡 Ask me about cryptocurrencies! I can help with:
   • Live prices and market data
   • Coin comparisons and analysis
   • Sustainability and risk assessments
   • Investment recommendations
   • Market trends and insights

{Fore.RED}⚠️  DISCLAIMER: Cryptocurrency investments are highly risky.
   Always do your own research before making any investment decisions!{Style.RESET_ALL}

{Fore.GREEN}Type 'help' for commands or 'quit' to exit.{Style.RESET_ALL}
"""
    print(banner)

def print_help():
    """Display help information"""
    help_text = f"""
{Fore.CYAN}🔧 Available Commands:{Style.RESET_ALL}
{Fore.GREEN}• help{Style.RESET_ALL}           - Show this help message
{Fore.GREEN}• quit / exit{Style.RESET_ALL}    - Exit CryptoBuddy Pro
{Fore.GREEN}• status{Style.RESET_ALL}         - Show system status and last data refresh

{Fore.CYAN}📊 Example Queries:{Style.RESET_ALL}
{Fore.YELLOW}• "What's the price of Bitcoin?"
• "Which coin is trending?"
• "Give me a sustainable and low-risk option"
• "Compare Ethereum vs Solana"
• "What are the top 5 cryptocurrencies?"
• "Tell me about Cardano's sustainability"
• "Which coins have the lowest energy usage?"{Style.RESET_ALL}
"""
    print(help_text)

def main():
    """Main application loop"""
    # Initialize colorama for cross-platform colored output
    init()
    
    # Print welcome banner
    print_banner()
    
    # Initialize the chatbot
    try:
        chatbot = CryptoChatBot()
        print(f"{Fore.GREEN}✅ CryptoBuddy Pro initialized successfully!{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}❌ Error initializing CryptoBuddy Pro: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Make sure you have an internet connection for live data.{Style.RESET_ALL}")
        return
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Fore.BLUE}🧑 You: {Style.RESET_ALL}").strip()
            
            # Handle empty input
            if not user_input:
                continue
            
            # Handle special commands
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"{Fore.CYAN}👋 Thanks for using CryptoBuddy Pro! Stay safe in the crypto world!{Style.RESET_ALL}")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'status':
                chatbot.show_status()
                continue
            
            # Process the query with the chatbot
            response = chatbot.process_query(user_input)
            print(f"{Fore.MAGENTA}🤖 CryptoBuddy Pro: {Style.RESET_ALL}{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}👋 Goodbye! Thanks for using CryptoBuddy Pro!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ An error occurred: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Please try rephrasing your question or type 'help' for guidance.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()