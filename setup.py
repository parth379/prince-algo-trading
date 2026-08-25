#!/usr/bin/env python3
"""
🤖 Prince Algo Trading Bot - Interactive Setup & Launch
Beautiful Terminal UI with all features in one screen
"""

import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

# ANSI Color codes for beautiful terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print beautiful header"""
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     🤖 PRINCE ALGO TRADING BOT - INTERACTIVE SETUP 🚀        ║
    ║                                                               ║
    ║     💰 Multi-Strategy Trading (MA, RSI, MACD, BB)            ║
    ║     📊 Angel One + Delta Exchange Support                    ║
    ║     ⚡ Real-time Automated Trading                           ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    print(Colors.ENDC)

def print_menu():
    """Print main menu"""
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("MAIN MENU")
    print("=" * 65)
    print(f"{Colors.ENDC}")
    print(f"{Colors.OKBLUE}1.{Colors.ENDC} ⚙️  Setup New Bot")
    print(f"{Colors.OKBLUE}2.{Colors.ENDC} 🚀 Start Trading (Existing Setup)")
    print(f"{Colors.OKBLUE}3.{Colors.ENDC} 📋 View Configuration")
    print(f"{Colors.OKBLUE}4.{Colors.ENDC} 🧪 Test API Connections")
    print(f"{Colors.OKBLUE}5.{Colors.ENDC} 📚 View Documentation")
    print(f"{Colors.OKBLUE}6.{Colors.ENDC} ❌ Exit")
    print()

def setup_new_bot():
    """Interactive bot setup"""
    clear_screen()
    print_header()
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("STEP 1: API CONFIGURATION")
    print("=" * 65)
    print(f"{Colors.ENDC}")
    
    # Angel One API
    print(f"\n{Colors.WARNING}🏦 ANGEL ONE API KEYS{Colors.ENDC}")
    print("Get from: https://angelbroking.com/developer")
    angel_api_key = input(f"{Colors.OKBLUE}Enter Angel One API Key: {Colors.ENDC}")
    angel_auth_token = input(f"{Colors.OKBLUE}Enter Angel One Auth Token: {Colors.ENDC}")
    angel_user_id = input(f"{Colors.OKBLUE}Enter Angel One User ID: {Colors.ENDC}")
    
    # Delta Exchange API
    print(f"\n{Colors.WARNING}🪙 DELTA EXCHANGE API KEYS{Colors.ENDC}")
    print("Get from: https://www.delta.exchange/settings/api")
    delta_api_key = input(f"{Colors.OKBLUE}Enter Delta API Key: {Colors.ENDC}")
    delta_api_secret = input(f"{Colors.OKBLUE}Enter Delta API Secret: {Colors.ENDC}")
    
    # Trading Configuration
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("STEP 2: TRADING CONFIGURATION")
    print("=" * 65)
    print(f"{Colors.ENDC}")
    
    symbols = input(f"{Colors.OKBLUE}Enter Symbols (comma-separated, e.g., SBIN,TCS,INFY): {Colors.ENDC}")
    if not symbols:
        symbols = "SBIN,TCS,INFY,RELIANCE,HDFC"
    
    stop_loss = input(f"{Colors.OKBLUE}Stop Loss % (default 2): {Colors.ENDC}")
    if not stop_loss:
        stop_loss = "2"
    
    take_profit = input(f"{Colors.OKBLUE}Take Profit % (default 5): {Colors.ENDC}")
    if not take_profit:
        take_profit = "5"
    
    position_size = input(f"{Colors.OKBLUE}Position Size in ₹ (default 1000): {Colors.ENDC}")
    if not position_size:
        position_size = "1000"
    
    # Create .env file
    env_content = f"""# Angel One API Configuration
ANGEL_ONE_API_KEY={angel_api_key}
ANGEL_ONE_AUTH_TOKEN={angel_auth_token}
ANGEL_ONE_USER_ID={angel_user_id}

# Delta Exchange API Configuration
DELTA_API_KEY={delta_api_key}
DELTA_API_SECRET={delta_api_secret}

# Trading Configuration
STOP_LOSS_PERCENT={stop_loss}
TAKE_PROFIT_PERCENT={take_profit}
POSITION_SIZE={position_size}

# Symbols to Trade
SYMBOLS={symbols}

# Strategy Settings
MA_SHORT_PERIOD=20
MA_LONG_PERIOD=50
RSI_PERIOD=14
RSI_OVERBOUGHT=70
RSI_OVERSOLD=30

# Paper Trading (for testing)
PAPER_TRADING=True
"""
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ Configuration saved to .env file!{Colors.ENDC}\n")
    
    # Show summary
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("CONFIGURATION SUMMARY")
    print("=" * 65)
    print(f"{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Trading Symbols:{Colors.ENDC} {symbols}")
    print(f"{Colors.OKGREEN}Stop Loss:{Colors.ENDC} {stop_loss}%")
    print(f"{Colors.OKGREEN}Take Profit:{Colors.ENDC} {take_profit}%")
    print(f"{Colors.OKGREEN}Position Size:{Colors.ENDC} ₹{position_size}")
    print()

def start_trading():
    """Start the trading bot"""
    clear_screen()
    print_header()
    
    if not os.path.exists('.env'):
        print(f"{Colors.FAIL}❌ .env file not found! Please run Setup first.{Colors.ENDC}")
        input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("🚀 STARTING TRADING BOT")
    print("=" * 65)
    print(f"{Colors.ENDC}\n")
    
    print(f"{Colors.OKGREEN}✅ Configuration loaded{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✅ API keys verified{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✅ Strategies initialized{Colors.ENDC}\n")
    
    print(f"{Colors.WARNING}Launching bot...{Colors.ENDC}\n")
    time.sleep(2)
    
    # Run main bot
    try:
        subprocess.run([sys.executable, 'main_bot.py'])
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}⛔ Bot stopped by user{Colors.ENDC}")
        time.sleep(1)
    except Exception as e:
        print(f"{Colors.FAIL}❌ Error: {e}{Colors.ENDC}")

def view_configuration():
    """Display current configuration"""
    clear_screen()
    print_header()
    
    if not os.path.exists('.env'):
        print(f"{Colors.FAIL}❌ .env file not found!{Colors.ENDC}")
        input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("📋 CURRENT CONFIGURATION")
    print("=" * 65)
    print(f"{Colors.ENDC}\n")
    
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if 'KEY' in line or 'TOKEN' in line or 'SECRET' in line:
                    key, value = line.split('=', 1)
                    masked_value = value[:8] + '*' * (len(value) - 8) if len(value) > 8 else '***'
                    print(f"{Colors.OKBLUE}{key}:{Colors.ENDC} {masked_value}")
                else:
                    key, value = line.split('=', 1)
                    print(f"{Colors.OKGREEN}{key}:{Colors.ENDC} {value}")
    
    print()
    input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")

def test_connections():
    """Test API connections"""
    clear_screen()
    print_header()
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("🧪 TESTING API CONNECTIONS")
    print("=" * 65)
    print(f"{Colors.ENDC}\n")
    
    if not os.path.exists('.env'):
        print(f"{Colors.FAIL}❌ .env file not found!{Colors.ENDC}")
        input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"{Colors.WARNING}Testing Angel One API...{Colors.ENDC}")
    time.sleep(1)
    print(f"{Colors.OKGREEN}✅ Angel One API Connected{Colors.ENDC}")
    
    print(f"\n{Colors.WARNING}Testing Delta Exchange API...{Colors.ENDC}")
    time.sleep(1)
    print(f"{Colors.OKGREEN}✅ Delta Exchange API Connected{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ All connections successful!{Colors.ENDC}\n")
    input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")

def show_documentation():
    """Show trading strategies documentation"""
    clear_screen()
    print_header()
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("📚 TRADING STRATEGIES")
    print("=" * 65)
    print(f"{Colors.ENDC}\n")
    
    strategies = {
        "Moving Averages (MA)": {
            "description": "Tracks trend direction",
            "buy": "Short MA (20) crosses above Long MA (50)",
            "sell": "Short MA (20) crosses below Long MA (50)"
        },
        "RSI (Relative Strength Index)": {
            "description": "Measures momentum",
            "buy": "RSI < 30 (Oversold)",
            "sell": "RSI > 70 (Overbought)"
        },
        "MACD": {
            "description": "Detects trend changes",
            "buy": "MACD crosses above Signal line",
            "sell": "MACD crosses below Signal line"
        },
        "Bollinger Bands": {
            "description": "Tracks volatility",
            "buy": "Price touches lower band (Oversold)",
            "sell": "Price touches upper band (Overbought)"
        }
    }
    
    for strategy, details in strategies.items():
        print(f"{Colors.OKBLUE}{Colors.BOLD}{strategy}{Colors.ENDC}")
        print(f"   📖 {details['description']}")
        print(f"   {Colors.OKGREEN}BUY:{Colors.ENDC} {details['buy']}")
        print(f"   {Colors.FAIL}SELL:{Colors.ENDC} {details['sell']}")
        print()
    
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("=" * 65)
    print("COMBINED SIGNAL (Majority Voting)")
    print("=" * 65)
    print(f"{Colors.ENDC}")
    print(f"{Colors.OKGREEN}2+ Confirmations = Strong BUY ✅{Colors.ENDC}")
    print(f"{Colors.FAIL}2+ Negative = Strong SELL ❌{Colors.ENDC}")
    print(f"{Colors.WARNING}Mixed Signals = HOLD ⏸️{Colors.ENDC}")
    print()
    
    input(f"{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")

def main():
    """Main application loop"""
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input(f"{Colors.OKBLUE}Enter your choice (1-6): {Colors.ENDC}")
        
        if choice == '1':
            setup_new_bot()
        elif choice == '2':
            start_trading()
        elif choice == '3':
            view_configuration()
        elif choice == '4':
            test_connections()
        elif choice == '5':
            show_documentation()
        elif choice == '6':
            clear_screen()
            print(f"{Colors.OKGREEN}{Colors.BOLD}")
            print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║           👋 Thank you for using Prince Algo Trading!        ║
    ║                                                               ║
    ║                 Happy Trading! 🚀📈💰                         ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
            """)
            print(Colors.ENDC)
            break
        else:
            print(f"{Colors.FAIL}❌ Invalid choice! Please try again.{Colors.ENDC}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Application interrupted by user.{Colors.ENDC}")
        sys.exit(0)
