# app.py (Updated)
from flask import Flask, jsonify, send_from_directory
from gpu_clustering import get_system_info

app = Flask(__name__)

@app.route("/api/system_info", methods=["GET"])
def system_info():
    info = get_system_info()
    return jsonify(info)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return send_from_directory('.', 'dashboard.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
