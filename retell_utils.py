import os
import requests

RETELL_API_KEY = os.getenv("key_fe87c015f66da9c63172af922d16")

def initiate_call(customer):
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "phone_number": customer["+923365780455"],
        "bot_id": "<agent_f2d66f5750d5e205e96026687c>",  # Replace with your Retell Bot ID
        "webhook_url": "<https://cold-calling-bot.onrender.com/>/webhook",
        "metadata": customer
    }

    response = requests.post("https://api.retellai.com/v1/calls", headers=headers, json=payload)
    return response.json()
