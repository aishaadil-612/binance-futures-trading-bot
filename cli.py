"""
cli.py

Command Line Interface for Binance Futures Testnet Trading Bot.
"""

import argparse
import sys

from bot.orders import OrderManager
from bot.validators import validate_inputs, ValidationError
from bot.logging_config import logger


def parse_arguments():
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT orders)"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        # Validate inputs
        order = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        logger.info("Validated user input.")

        manager = OrderManager()

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol    : {order['symbol']}")
        print(f"Side      : {order['side']}")
        print(f"Type      : {order['order_type']}")
        print(f"Quantity  : {order['quantity']}")

        if order["order_type"] == "LIMIT":
            print(f"Price     : {order['price']}")

        print("===================================\n")

        if order["order_type"] == "MARKET":
            response = manager.place_market_order(
                symbol=order["symbol"],
                side=order["side"],
                quantity=order["quantity"],
            )

        else:
            response = manager.place_limit_order(
                symbol=order["symbol"],
                side=order["side"],
                quantity=order["quantity"],
                price=order["price"],
            )

        manager.print_order_summary(response)

        print("✅ Order placed successfully.")

    except ValidationError as e:
        logger.error(e)
        print(f"\n❌ Validation Error: {e}")

    except Exception as e:
        logger.exception(e)
        print(f"\n❌ Error: {e}")

        sys.exit(1)


if __name__ == "__main__":
    main()