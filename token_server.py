"""
LiveKit token server for the Bantu voice agent.
Run this so a browser client can get a token and connect to the agent.
"""
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv(".env.local")

# Optional: use livekit-api for token generation
try:
    from livekit import api
    HAS_LIVEKIT_API = True
except ImportError:
    HAS_LIVEKIT_API = False

app = Flask(__name__)
CORS(app)

# Default agent dispatch so Bantu joins when a client connects
DEFAULT_ROOM_CONFIG = {
    "agents": [{"agent_name": "Bantu"}]
}


def create_token(body):
    if not HAS_LIVEKIT_API:
        raise RuntimeError("Install livekit-api: pip install livekit-api")
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    if not api_key or not api_secret:
        raise ValueError("LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set in .env.local")
    token = api.AccessToken(api_key, api_secret)
    room_name = body.get("room_name") or "bantu-room"
    token = token.with_grants(api.VideoGrants(room_join=True, room=room_name))
    room_config = body.get("room_config") or DEFAULT_ROOM_CONFIG
    token = token.with_room_config(room_config)
    token = token.with_identity(body.get("participant_identity") or "user")
    token = token.with_name(body.get("participant_name") or "User")
    if body.get("participant_metadata"):
        token = token.with_metadata(body["participant_metadata"])
    if body.get("participant_attributes"):
        token = token.with_attributes(body["participant_attributes"])
    return token.to_jwt()


@app.route("/getToken", methods=["POST", "OPTIONS"])
def get_token():
    if request.method == "OPTIONS":
        return "", 204
    try:
        body = request.get_json(silent=True) or {}
        participant_token = create_token(body)
        server_url = os.getenv("LIVEKIT_URL")
        if not server_url:
            return jsonify({"error": "LIVEKIT_URL not set in .env.local"}), 500
        return jsonify({
            "server_url": server_url,
            "participant_token": participant_token,
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Token server: POST http://localhost:5000/getToken")
    print("Open frontend/index.html in a browser (or serve it) to connect to Bantu.")
    app.run(host="0.0.0.0", port=5000, debug=True)
