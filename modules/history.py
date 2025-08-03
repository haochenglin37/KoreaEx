"""Trade history storage."""

from pathlib import Path
from typing import Dict, List
import pandas as pd


class TradeHistory:
    """Store trade records in a CSV file."""

    def __init__(self, path: Path):
        self.path = path
        if not self.path.exists():
            df = pd.DataFrame(columns=["timestamp", "symbol", "side", "price", "amount"])
            df.to_csv(self.path, index=False)

    def append(self, record: Dict):
        df = pd.DataFrame([record])
        df.to_csv(self.path, mode="a", header=False, index=False)

    def load(self) -> List[Dict]:
        return pd.read_csv(self.path).to_dict("records")
