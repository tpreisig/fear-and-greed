import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

def fetch_data():
    api_key = os.getenv("COINMARKETCAP_API_KEY")
    if not api_key:
        print( "‼️ API key not found ‼️\nEnsure COINMARKETCAP_API_KEY is set in the .env file.")

    url = "https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical?limit=100"
    headers = {"X-CMC_PRO_API_KEY": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        print(f"Data from Coinmarketcap API ⬇️\n{json.dumps(result["data"], indent=2)}")
    except requests.RequestException as e:
        print(e)
    
fetch_data()

