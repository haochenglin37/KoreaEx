"""Spider to track new coin listings on a given Korean exchange using ccxt."""

from typing import List, Set
import ccxt


class ListingSpider:
    """Fetches new coin listings from a ccxt exchange instance."""

    def __init__(self, exchange: ccxt.Exchange):
        self.exchange = exchange
        self.known_markets: Set[str] = set()

    def fetch_new_listings(self) -> List[str]:
        """Return a list of symbols that were listed since last call."""
        markets = self.exchange.load_markets()
        tickers = set(markets.keys())
        new = sorted(tickers - self.known_markets)
        self.known_markets = tickers
        return new
