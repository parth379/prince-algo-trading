import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
ANGEL_ONE_API_KEY = os.getenv('ANGEL_ONE_API_KEY')
ANGEL_ONE_AUTH_TOKEN = os.getenv('ANGEL_ONE_AUTH_TOKEN')
ANGEL_ONE_USER_ID = os.getenv('ANGEL_ONE_USER_ID')

DELTA_API_KEY = os.getenv('DELTA_API_KEY')
DELTA_API_SECRET = os.getenv('DELTA_API_SECRET')

# Trading Configuration
SYMBOLS = os.getenv('SYMBOLS', 'SBIN,TCS,INFY').split(',')
STOP_LOSS_PERCENT = float(os.getenv('STOP_LOSS_PERCENT', 2))
TAKE_PROFIT_PERCENT = float(os.getenv('TAKE_PROFIT_PERCENT', 5))
POSITION_SIZE = float(os.getenv('POSITION_SIZE', 1000))

# Strategy Parameters
MA_SHORT_PERIOD = int(os.getenv('MA_SHORT_PERIOD', 20))
MA_LONG_PERIOD = int(os.getenv('MA_LONG_PERIOD', 50))
RSI_PERIOD = int(os.getenv('RSI_PERIOD', 14))
RSI_OVERBOUGHT = int(os.getenv('RSI_OVERBOUGHT', 70))
RSI_OVERSOLD = int(os.getenv('RSI_OVERSOLD', 30))

# Bot Settings
SCAN_INTERVAL = 5  # minutes
LOG_FILE = 'logs/trading_bot.log'
TRADE_LOG_FILE = 'logs/trades.csv'

# Paper Trading Mode (for testing)
PAPER_TRADING = os.getenv('PAPER_TRADING', 'True') == 'True'
