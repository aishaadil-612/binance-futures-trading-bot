import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

timestamp = int(time.time() * 1000)

query = f"timestamp={timestamp}"

signature = hmac.new(
    API_SECRET.encode(),
    query.encode(),
    hashlib.sha256
).hexdigest()

url = f"{BASE_URL}/fapi/v2/balance?{query}&signature={signature}"

headers = {
    "X-MBX-APIKEY": API_KEY
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print(response.text)