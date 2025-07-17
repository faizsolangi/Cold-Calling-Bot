from flask import Flask, request, jsonify
from retell_utils import trigger_call

import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Cold Calling Bot Running"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Incoming call result:", data)
    # Here you can process or log the result
    return jsonify({"status": "received"}), 200

@app.route('/trigger-call', methods=['GET'])
def trigger():
    customer = {
        "name": "John Doe",
        "phone": "+923365780455",  # Use a verified number for testing
        "order_id": "12345",
        "item": "Wireless Mouse",
        "address": "123 Main Street",
        "eta": "3-5 business days"
    }
    response = initiate_call(customer)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)  # Render default port

