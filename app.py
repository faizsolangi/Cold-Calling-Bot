from flask import Flask
from retell_utils import trigger_call

app = Flask(__name__)

@app.route('/')
def home():
    return 'Cold Calling Bot Running'

@app.route('/start')
def start():
    trigger_call()
    return 'Call initiated'


