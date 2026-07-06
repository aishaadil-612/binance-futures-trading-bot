from bot.client import BinanceClient

client = BinanceClient().get_client()

print(client.futures_account_balance())