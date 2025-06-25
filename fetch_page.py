import os
import requests
from dotenv import load_dotenv

load_dotenv()

BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
def fetch_page_text(url: str) -> str:
    api_url = f"https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}"
    payload = {
        "url": url,
        "gotoOptions": {
            "waitUntil": "networkidle0"
        }
    }
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result.get("data", "No content retrieved")
    else:
        return f"Error: {response.status_code} - {response.text}"
