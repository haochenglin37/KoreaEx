"""Execution module handling orders."""

import logging


class Executor:
    """Simple executor that logs buy and sell actions."""

    def __init__(self, exchange):
        self.exchange = exchange
        self.logger = logging.getLogger(__name__)

    def market_buy(self, symbol: str, amount: float):
        self.logger.info(f"Buying {amount} {symbol}")
        # self.exchange.client.create_market_buy_order(symbol, amount)

    def market_sell(self, symbol: str, amount: float):
        self.logger.info(f"Selling {amount} {symbol}")
        # self.exchange.client.create_market_sell_order(symbol, amount)
