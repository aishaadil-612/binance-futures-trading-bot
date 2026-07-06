from bot.client import BinanceClient

client = BinanceClient()

if client.ping():
    print("✅ Connected to Binance Futures Testnet!")
from bot.orders import OrderManager

manager = OrderManager()

# MARKET BUY
response = manager.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
)

manager.print_order_summary(response)        
from bot.validators import validate_inputs

data = validate_inputs(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.001
)

print(data)