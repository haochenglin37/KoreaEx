"""Strategy module for trading newly listed coins."""

from dataclasses import dataclass
from typing import Dict
import time


@dataclass
class StrategyConfig:
    take_profit: float = 15               # percent
    pullback_threshold: float = 0.15      # fraction
    add_position_interval: float = 0.15   # fraction
    max_add_times: int = 4
    high_lookback_hours: int = 8
    min_high_age_hours: int = 3
    listing_delay_hours: int = 2
    initial_position: float = 10
    position_multiplier: float = 2


class ListingStrategy:
    """Implements the entry and exit logic for newly listed coins."""

    def __init__(self, config: StrategyConfig):
        self.config = config
        self.entry_price: Dict[str, float] = {}
        self.high_price: Dict[str, float] = {}
        self.add_times: Dict[str, int] = {}
        self.listing_time: Dict[str, float] = {}

    def record_listing_time(self, symbol: str):
        self.listing_time.setdefault(symbol, time.time())

    def should_buy(self, symbol: str, current_price: float) -> bool:
        listing_time = self.listing_time.get(symbol)
        if listing_time is None:
            return False
        if time.time() - listing_time < self.config.listing_delay_hours * 3600:
            return False
        self.entry_price.setdefault(symbol, current_price)
        self.high_price.setdefault(symbol, current_price)
        self.add_times.setdefault(symbol, 0)
        return True

    def update_high(self, symbol: str, current_price: float):
        high = self.high_price.get(symbol, current_price)
        if current_price > high:
            self.high_price[symbol] = current_price
        return self.high_price[symbol]

    def should_add_position(self, symbol: str, current_price: float) -> bool:
        base = self.entry_price.get(symbol)
        if base is None:
            return False
        add_times = self.add_times.get(symbol, 0)
        target = base * (1 + self.config.add_position_interval * (add_times + 1))
        if current_price >= target and add_times < self.config.max_add_times:
            self.add_times[symbol] = add_times + 1
            return True
        return False

    def should_take_profit(self, symbol: str, current_price: float) -> bool:
        base = self.entry_price.get(symbol)
        if base is None:
            return False
        profit = (current_price - base) / base * 100
        if profit >= self.config.take_profit:
            return True
        pullback = 1 - current_price / self.high_price.get(symbol, current_price)
        if pullback >= self.config.pullback_threshold:
            return True
        return False
