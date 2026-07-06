"""
client.py

Binance Futures Testnet client wrapper.
"""

import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# Load environment variables
load_dotenv()


class BinanceClient:
    """
    Wrapper class for Binance Futures Testnet client.
    """

    TESTNET_URL = "https://testnet.binancefuture.com"

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "API_KEY and API_SECRET must be set in the .env file."
            )

        try:
            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
            )

            # Point to Futures Testnet
            self.client.FUTURES_URL = self.TESTNET_URL

        except Exception as e:
            raise ConnectionError(
                f"Failed to initialize Binance client: {e}"
            )

    def get_client(self):
        """
        Returns the initialized Binance client.
        """
        return self.client

    def ping(self):
        """
        Test connectivity with Binance.
        """
        try:
            self.client.futures_ping()
            return True
        except BinanceRequestException as e:
            raise ConnectionError(f"Network error: {e}")
        except BinanceAPIException as e:
            raise RuntimeError(f"Binance API error: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

    def get_account_balance(self):
        """
        Returns futures account balances.
        """
        try:
            return self.client.futures_account_balance()
        except BinanceAPIException as e:
            raise RuntimeError(f"API Error: {e}")