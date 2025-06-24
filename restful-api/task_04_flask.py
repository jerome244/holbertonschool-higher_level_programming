#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Store full user object including username
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
