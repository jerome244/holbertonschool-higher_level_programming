#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["JWT_SECRET_KEY"] = "your-jwt-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# -------------------- BASIC AUTH --------------------


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------- JWT AUTH --------------------


@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        additional_claims = {"role": user["role"]}
        token = create_access_token(
            identity=username, additional_claims=additional_claims
        )
        return jsonify(access_token=token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# -------------------- JWT ERROR HANDLERS --------------------


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# -------------------- RUN --------------------

if __name__ == "__main__":
    app.run()
