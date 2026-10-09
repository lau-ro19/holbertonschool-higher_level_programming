#!/usr/bin/python3
"""
A simple RESTful API built using Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Status endpoint."""
    return "OK"


@app.route('/data')
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object of a specific user or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
