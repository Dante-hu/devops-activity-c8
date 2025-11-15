# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, World!")


@app.route("/goodbye", methods=["GET"])
def goodbye():
    return jsonify(message="Goodbye, World!")


@app.route("/mood", methods=["POST"])
def mood():
    if request.is_json:
        mood = request.json.get("mood", "unknown")
    return jsonify(message=f"I'm feeling {mood}!")


if __name__ == "__main__":
    app.run(debug=True)
