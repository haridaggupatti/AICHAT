'''
SmartTradeAI - Main Application
This file contains the main entry point for the SmartTradeAI application.
'''
import tkinter as tk
from market_analysis import MarketAnalysis
from trade_execution import TradeExecution
from trading_strategies import TradingStrategies
from feedback_system import FeedbackSystem
from performance_analytics import PerformanceAnalytics
from self_improving_ai import SelfImprovingAI
from risk_management import RiskManagement
from user_interface import UserInterface
from security_compliance import SecurityCompliance
class SmartTradeAI:
    def __init__(self):
        self.root = tk.Tk()
        self.market_analysis = MarketAnalysis()
        self.trade_execution = TradeExecution()
        self.trading_strategies = TradingStrategies()
        self.feedback_system = FeedbackSystem()
        self.performance_analytics = PerformanceAnalytics()
        self.self_improving_ai = SelfImprovingAI()
        self.risk_management = RiskManagement()
        self.user_interface = UserInterface()
        self.security_compliance = SecurityCompliance()
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = SmartTradeAI()
    app.run()