"""
Trading Bot Package

A modular Python trading bot for Binance Futures Testnet.

Modules:
- client: Binance API client wrapper
- orders: Order placement logic
- validators: Input validation
- logging_config: Logging configuration
- exceptions: Custom exception classes
"""

__version__ = "1.0.0"
__author__ = "Aisha Adil"

from .client import BinanceClient
from .orders import OrderManager

__all__ = [
    "BinanceClient",
    "OrderManager",
]