import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")
secret = os.getenv("API_SECRET")

print("API_KEY loaded:", key is not None)
print("API_SECRET loaded:", secret is not None)

if key:
    print("API_KEY starts with:", key[:6] + "...")