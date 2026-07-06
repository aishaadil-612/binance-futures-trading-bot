"""
validators.py

Validation functions for Binance Futures Trading Bot.
"""

import re


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


class ValidationError(Exception):
    """Raised when user input is invalid."""
    pass


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    Example: BTCUSDT
    """
    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    symbol = symbol.upper().strip()

    if not re.match(r"^[A-Z0-9]{6,20}$", symbol):
        raise ValidationError(
            "Invalid symbol format. Example: BTCUSDT"
        )

    return symbol


def validate_side(side: str) -> str:
    """
    Validate BUY/SELL.
    """
    if not side:
        raise ValidationError("Side is required.")

    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValidationError(
            "Side must be BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate MARKET/LIMIT.
    """
    if not order_type:
        raise ValidationError("Order type is required.")

    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity) -> float:
    """
    Validate quantity.
    """

    try:
        quantity = float(quantity)
    except (ValueError, TypeError):
        raise ValidationError(
            "Quantity must be a number."
        )

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price, order_type: str):
    """
    Validate price for LIMIT orders.
    """

    if order_type.upper() == "MARKET":
        return None

    if price is None:
        raise ValidationError(
            "Price is required for LIMIT orders."
        )

    try:
        price = float(price)
    except (ValueError, TypeError):
        raise ValidationError(
            "Price must be numeric."
        )

    if price <= 0:
        raise ValidationError(
            "Price must be greater than zero."
        )

    return price


def validate_inputs(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
):
    """
    Validate all inputs.

    Returns:
        dict
    """

    return {
        "symbol": validate_symbol(symbol),
        "side": validate_side(side),
        "order_type": validate_order_type(order_type),
        "quantity": validate_quantity(quantity),
        "price": validate_price(price, order_type),
    }