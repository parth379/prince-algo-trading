import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator, MACD
from ta.volatility import BollingerBands

class TradingStrategies:
    """
    Combined Trading Strategies:
    - Moving Averages (MA)
    - RSI (Relative Strength Index)
    - MACD (Moving Average Convergence Divergence)
    - Bollinger Bands
    """
    
    def __init__(self, short_ma=20, long_ma=50, rsi_period=14):
        self.short_ma = short_ma
        self.long_ma = long_ma
        self.rsi_period = rsi_period
    
    def moving_average_signal(self, df):
        """
        Moving Averages Strategy
        BUY: Short MA crosses above Long MA
        SELL: Short MA crosses below Long MA
        """
        df['MA_SHORT'] = df['close'].rolling(window=self.short_ma).mean()
        df['MA_LONG'] = df['close'].rolling(window=self.long_ma).mean()
        
        signal = 0
        if len(df) >= 2:
            prev_short = df['MA_SHORT'].iloc[-2]
            prev_long = df['MA_LONG'].iloc[-2]
            curr_short = df['MA_SHORT'].iloc[-1]
            curr_long = df['MA_LONG'].iloc[-1]
            
            if prev_short <= prev_long and curr_short > curr_long:
                signal = 1  # BUY
            elif prev_short >= prev_long and curr_short < curr_long:
                signal = -1  # SELL
        
        return signal, df
    
    def rsi_signal(self, df, overbought=70, oversold=30):
        """
        RSI Strategy
        BUY: RSI < 30 (Oversold)
        SELL: RSI > 70 (Overbought)
        """
        rsi = RSIIndicator(close=df['close'], window=self.rsi_period)
        df['RSI'] = rsi.rsi()
        
        signal = 0
        if len(df) > 0:
            current_rsi = df['RSI'].iloc[-1]
            if current_rsi < oversold:
                signal = 1  # BUY
            elif current_rsi > overbought:
                signal = -1  # SELL
        
        return signal, df
    
    def macd_signal(self, df):
        """
        MACD Strategy
        BUY: MACD crosses above Signal line
        SELL: MACD crosses below Signal line
        """
        macd = MACD(close=df['close'])
        df['MACD'] = macd.macd()
        df['MACD_SIGNAL'] = macd.macd_signal()
        df['MACD_DIFF'] = macd.macd_diff()
        
        signal = 0
        if len(df) >= 2:
            prev_macd = df['MACD'].iloc[-2]
            prev_signal = df['MACD_SIGNAL'].iloc[-2]
            curr_macd = df['MACD'].iloc[-1]
            curr_signal = df['MACD_SIGNAL'].iloc[-1]
            
            if prev_macd <= prev_signal and curr_macd > curr_signal:
                signal = 1  # BUY
            elif prev_macd >= prev_signal and curr_macd < curr_signal:
                signal = -1  # SELL
        
        return signal, df
    
    def bollinger_bands_signal(self, df, period=20):
        """
        Bollinger Bands Strategy
        BUY: Price touches lower band
        SELL: Price touches upper band
        """
        bb = BollingerBands(close=df['close'], window=period, window_dev=2)
        df['BB_HIGH'] = bb.bollinger_hband()
        df['BB_LOW'] = bb.bollinger_lband()
        df['BB_MID'] = bb.bollinger_mavg()
        
        signal = 0
        if len(df) > 0:
            current_price = df['close'].iloc[-1]
            upper_band = df['BB_HIGH'].iloc[-1]
            lower_band = df['BB_LOW'].iloc[-1]
            
            if current_price <= lower_band:
                signal = 1  # BUY (Oversold)
            elif current_price >= upper_band:
                signal = -1  # SELL (Overbought)
        
        return signal, df
    
    def combined_signal(self, df, overbought=70, oversold=30):
        """
        Combine all strategies and generate final signal
        Returns: 1 (Strong BUY), -1 (Strong SELL), 0 (HOLD)
        """
        signals = []
        
        # Get individual signals
        ma_sig, df = self.moving_average_signal(df)
        signals.append(ma_sig)
        
        rsi_sig, df = self.rsi_signal(df, overbought, oversold)
        signals.append(rsi_sig)
        
        macd_sig, df = self.macd_signal(df)
        signals.append(macd_sig)
        
        bb_sig, df = self.bollinger_bands_signal(df)
        signals.append(bb_sig)
        
        # Majority voting
        total_signal = sum(signals)
        
        if total_signal >= 2:
            final_signal = 1  # BUY
        elif total_signal <= -2:
            final_signal = -1  # SELL
        else:
            final_signal = 0  # HOLD
        
        return final_signal, df, {
            'MA': ma_sig,
            'RSI': rsi_sig,
            'MACD': macd_sig,
            'BB': bb_sig
        }
