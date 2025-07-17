import os
import requests

def trigger_call(agent_id: str, user_number: str, retell_api_key: str = None) -> bool:
    """
    Triggers a call via Retell AI using the agent_id and phone number.

    Args:
        agent_id (str):key_fe87c015f66da9c63172af922d16
        user_number (str):+923365780455 
        retell_api_key (str, optional): key_fe87c015f66da9c63172af922d16

    Returns:
        bool: True if the API call was successful, False otherwise.
    """

    if not retell_api_key:
        retell_api_key = os.getenv("key_fe87c015f66da9c63172af922d16")

    if not all([agent_id, user_number, retell_api_key]):
        print("❌ Missing one or more required parameters.")
        return False

    # Debug logs
    print("🚀 Triggering Retell AI call...")
    print(f"📞 Calling Number: {user_number}")
    print(f"🤖 Agent ID: {agent_id}")
    print(f"🔑 API Key starts with: {retell_api_key[:6]}...")

    headers = {
        "Authorization": f"Bearer {retell_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "agent_id": agent_id,
        "phone_number": user_number
    }

    try:
        response = requests.post("https://api.retellai.com/v1/call", json=payload, headers=headers)
        print(f"📡 Retell API Response [{response.status_code}]: {response.text}")

        if response.status_code == 200:
            print("✅ Call triggered successfully.")
            return True
        else:
            print("❌ Failed to trigger call.")
            return False

    except Exception as e:
        print(f"❗ Exception during API call: {e}")
        return False





