# KoreaEx

A simple prototype trading bot that monitors new coin listings on Korean cryptocurrency exchanges and applies a listing strategy.

## Project structure

```
trading_bot/
├── config/
│   ├── .env
│   └── config.yaml
├── logs/
├── modules/
│   ├── spider.py
│   ├── exchange.py
│   ├── strategy.py
│   ├── executor.py
│   └── history.py
├── main.py
├── requirements.txt
└── README.md
```

## Usage

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Fill in `config/.env` with your API credentials.

3. Run the bot:

```
python main.py
```

The `config/config.yaml` file contains the default strategy parameters (taken from optimisation results). The bot currently logs detected new listings and shows how modules interact; extend `strategy` and `executor` modules for real trading.
