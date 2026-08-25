import pandas as pd
import numpy as np
from strategies import TradingStrategies
from datetime import datetime

class BackTester:
    """
    Backtest trading strategies on historical data
    """
    
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.strategies = TradingStrategies()
        self.trades = []
    
    def load_sample_data(self, symbol):
        """Load sample OHLC data (for testing)"""
        # This would load real data from CSV or API
        # For now, returning dummy data
        pass
    
    def run_backtest(self, df, symbol):
        """Run backtest on historical data"""
        positions = {}
        trade_history = []
        
        for i in range(len(df) - 1):
            current_df = df[:i+1].copy()
            
            signal, analyzed_df, individual_signals = self.strategies.combined_signal(current_df)
            current_price = df['close'].iloc[i]
            
            # BUY Signal
            if signal == 1 and symbol not in positions:
                qty = int(self.capital * 0.1 / current_price)
                positions[symbol] = {
                    'entry_price': current_price,
                    'qty': qty,
                    'entry_index': i
                }
                trade_history.append({
                    'type': 'BUY',
                    'price': current_price,
                    'qty': qty,
                    'index': i
                })
            
            # SELL Signal
            elif signal == -1 and symbol in positions:
                position = positions[symbol]
                profit = (current_price - position['entry_price']) * position['qty']
                
                trade_history.append({
                    'type': 'SELL',
                    'price': current_price,
                    'qty': position['qty'],
                    'profit': profit,
                    'index': i
                })
                
                self.capital += profit
                del positions[symbol]
        
        return trade_history
    
    def print_backtest_report(self, trades, symbol):
        """Print backtest results"""
        buy_trades = [t for t in trades if t['type'] == 'BUY']
        sell_trades = [t for t in trades if t['type'] == 'SELL']
        total_profit = sum([t.get('profit', 0) for t in sell_trades])
        
        print("\n" + "="*60)
        print(f"📊 Backtest Report: {symbol}")
        print("="*60)
        print(f"Initial Capital: ₹{self.initial_capital:.2f}")
        print(f"Final Capital: ₹{self.capital:.2f}")
        print(f"Total Profit: ₹{total_profit:.2f}")
        print(f"Return: {((self.capital - self.initial_capital) / self.initial_capital * 100):.2f}%")
        print(f"\nBuy Signals: {len(buy_trades)}")
        print(f"Sell Signals: {len(sell_trades)}")
        print(f"Win Rate: {(len([t for t in sell_trades if t.get('profit', 0) > 0]) / len(sell_trades) * 100) if sell_trades else 0:.2f}%")

if __name__ == "__main__":
    print("Backtest module loaded. Use with your historical data.")
