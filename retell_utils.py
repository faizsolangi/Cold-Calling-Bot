import os
import requests

def trigger_call(agent_id: str, user_number: str, retell_api_key: str = None) -> bool:
    """
    Triggers a call via Retell AI using the agent_id and phone number.

    Args:
        agent_id (str): The ID of the Retell AI agent
        user_number (str): Customer phone number in international format (+92...)
        retell_api_key (str, optional): Your Retell API key (uses ENV variable if not provided)

    Returns:
        bool: True if the API call was successful, False otherwise.
    """

    if not retell_api_key:
        retell_api_key = os.getenv("RETELL_API_KEY")  # Make sure you set this in your Render environment

    if not all([agent_id, user_number, retell_api_key]):
        print("❌ Missing one or more required parameters.")
        return False

    print("🚀 Triggering Retell AI call...")
    print(f"📞 Calling Number: {user_number}")
    print(f"🤖 Agent ID: {agent_id}")
    print(f"🔑 API Key starts with: {retell_api_key[:6]}...")

    headers = {
        "Authorization": f"Bearer {retell_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "agent_id": key_fe87c015f66da9c63172af922d16,
        "customer": {
            "phone_number": +923016377754
        }
    }

    try:
        response = requests.post("https://api.retellai.com/calls", json=payload, headers=headers)
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
