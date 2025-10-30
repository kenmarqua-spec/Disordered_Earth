from npc import *
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "🌍 Disordered Earth Web Build is Running!"

@app.route('/npc_data')
def npc_data():
    data = {
        "npc": {
            "name": "Aela",
            "age": 24,
            "job": "Hunter",
            "knowledge": ["Stone tools", "Firemaking"],
            "family": ["Tharn", "Eri"]
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)