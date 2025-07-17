import os
import requests

RETELL_API_KEY = os.getenv("key_fe87c015f66da9c63172af922d16")

def initiate_call(customer):
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "phone_number": customer["phone"],
        "bot_id": "<YOUR_BOT_ID>",  # Replace with your Retell Bot ID
        "webhook_url": "<YOUR_RENDER_URL>/webhook",
        "metadata": customer
    }

    response = requests.post("https://api.retellai.com/v1/calls", headers=headers, json=payload)
    return response.json()
