"""Exchange connector using ccxt for Korean exchanges."""

from typing import Optional
import ccxt


class Exchange:
    """Wrapper around ccxt exchange with basic helpers."""

    def __init__(self, exchange_id: str, api_key: Optional[str] = None, secret: Optional[str] = None):
        cls = getattr(ccxt, exchange_id)
        self.client = cls({'apiKey': api_key, 'secret': secret})

    def load_markets(self):
        return self.client.load_markets()

    def fetch_ohlcv(self, symbol: str, timeframe: str = '1m', limit: int = 200):
        return self.client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    def get_current_price(self, symbol: str) -> float:
        ticker = self.client.fetch_ticker(symbol)
        return ticker['last']
