'''
SmartTradeAI - Feedback System
This file contains the implementation of an explanatory feedback system.
'''
class FeedbackSystem:
    def __init__(self):
        # Initialize feedback system
        pass
    def provide_feedback(self, trade_decision):
        # Provide detailed feedback for each trade decision made by the AI
        if trade_decision == "Buy":
            return "The AI decided to buy based on market conditions."
        elif trade_decision == "Sell":
            return "The AI decided to sell based on market conditions."
        else:
            return "The AI decided to hold based on market conditions."