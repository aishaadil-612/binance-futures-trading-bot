"""
orders.py

Contains reusable functions for placing Binance Futures Testnet orders.
"""

import logging
from binance.enums import (
    SIDE_BUY,
    SIDE_SELL,
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
)
from binance.exceptions import BinanceAPIException, BinanceRequestException

from .client import BinanceClient

from .logging_config import logger


class OrderManager:
    """
    Handles all Binance Futures order operations.
    """

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """
        Place a MARKET BUY or SELL order.
        """

        try:
            logger.info(
                "Placing MARKET order | Symbol=%s Side=%s Quantity=%s",
                symbol,
                side,
                quantity,
            )

            response = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity,
            )

            logger.info("Order Success: %s", response)

            return response

        except BinanceAPIException as e:
            logger.error("Binance API Error: %s", e)
            raise

        except BinanceRequestException as e:
            logger.error("Network Error: %s", e)
            raise

        except Exception as e:
            logger.exception("Unexpected Error")
            raise RuntimeError(str(e))

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ):
        """
        Place a LIMIT BUY or SELL order.
        """

        try:
            logger.info(
                "Placing LIMIT order | Symbol=%s Side=%s Qty=%s Price=%s",
                symbol,
                side,
                quantity,
                price,
            )

            response = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC,
            )

            logger.info("Order Success: %s", response)

            return response

        except BinanceAPIException as e:
            logger.error("Binance API Error: %s", e)
            raise

        except BinanceRequestException as e:
            logger.error("Network Error: %s", e)
            raise

        except Exception as e:
            logger.exception("Unexpected Error")
            raise RuntimeError(str(e))

    @staticmethod
    def print_order_summary(response):
        """
        Print formatted order response.
        """

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Symbol        : {response.get('symbol')}")
        print(f"Status        : {response.get('status')}")
        print(f"Side          : {response.get('side')}")
        print(f"Type          : {response.get('type')}")
        print(f"Quantity      : {response.get('origQty')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Price         : {response.get('price')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")
        print("====================================\n")