from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
datos_actuales = {}

@app.route('/')
def home():
    return "API de temperatura funcionando"

@app.route('/temperatura', methods=['POST'])
def recibir_temperatura():
    global datos_actuales
    data = request.get_json()
    datos_actuales = {
        "temperatura": data.get("temperatura"),
        "humedad": data.get("humedad"),
        "timestamp": datetime.now().isoformat()
    }
    return jsonify({"estado": "ok"}), 200

@app.route('/temperatura', methods=['GET'])
def obtener_temperatura():
    return jsonify(datos_actuales), 200
