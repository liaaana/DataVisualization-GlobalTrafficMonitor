from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/data", methods=["POST"])
def receive():
    data = request.get_json()
    if isinstance(data, list):
        socketio.emit("new_packets", data)
        return jsonify({"ok": True, "count": len(data)}), 200
    return jsonify({"error": "bad request"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
