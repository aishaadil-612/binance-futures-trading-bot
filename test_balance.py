from bot.client import BinanceClient

client = BinanceClient().get_client()

balance = client.futures_account_balance()

print(balance)