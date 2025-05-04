from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
API_TOKEN = "supersecretcode"
DATA_FILE = "data.json"

def init_storage():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def verify_token(req):
    token = req.headers.get("Authorization", "")
    return token == f"{API_TOKEN}"

@app.route('/diagnosis/<patient_id>', methods=['GET'])
def get_diagnosis(patient_id):
    if not verify_token(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = load_data()
    diagnosis = data.get(patient_id)
    if diagnosis:
        return jsonify({"patient_id": patient_id, **diagnosis})
    else:
        return jsonify({"error": "Patient ID not found"}), 404

@app.route('/submit/<patient_id>', methods=['POST'])
def submit_diagnosis(patient_id):
    if not verify_token(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        new_data = request.get_json()
        required = {"name", "diagnosis", "prescription", "doctor", "recommendations"}
        if not new_data or not required.issubset(new_data):
            return jsonify({"error": "Missing required fields"}), 400

        data = load_data()
        data[patient_id] = new_data
        save_data(data)

        return jsonify({"message": "Diagnosis data submitted", "patient_id": patient_id}), 201
    except:
        return jsonify({"error": "Invalid request format"}), 400

init_storage()
app.run(debug=True)
