"""Entry point tying together the trading bot modules."""

import time
from pathlib import Path
import os

import yaml
from dotenv import load_dotenv

from modules.exchange import Exchange
from modules.spider import ListingSpider
from modules.strategy import StrategyConfig, ListingStrategy
from modules.executor import Executor
from modules.history import TradeHistory


def load_config() -> dict:
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


def main():
    load_dotenv("config/.env")
    cfg = load_config()

    exchange = Exchange(cfg["exchange"], os.getenv("API_KEY"), os.getenv("API_SECRET"))
    spider = ListingSpider(exchange.client)
    strategy = ListingStrategy(StrategyConfig(**cfg["strategy"]))
    executor = Executor(exchange)
    history = TradeHistory(Path("logs/trades.csv"))

    while True:
        new_listings = spider.fetch_new_listings()
        for symbol in new_listings:
            print(f"New listing detected: {symbol}")
            strategy.record_listing_time(symbol)
        # Sleep to avoid spamming the exchange
        time.sleep(60)


if __name__ == "__main__":
    main()
