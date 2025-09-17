from flask import Flask, redirect, jsonify, request, session
from time import time

app = Flask(__name__)

app.secret_key = "secret_heehoo"

start_time = time()


public_games = {
    "Game1": {"players": ["Alice", "Bob"], "status": "Not Started"},
    "Game2": {"players": ["Bob", "Charlie"], "status": "In Progress"},
    "Game3": {"players": ["Alice", "Charlie"], "status": "Finished", "winner": "Alice"},
}


# this is the main page of the app where you see the list of games that are available to you
@app.route("/")
def index():
    with open("client/index.html") as f:
        content = f.read()
    return content


# endpoint that just serves the public game info as JSON
@app.route("/data/public-games")
def get_players():
    return jsonify(public_games)

# serves the JS file that the HTML uses
@app.route("/script.js")
def get_js():
    with open("client/script.js") as f:
        content = f.read()
    return content, 200, {'Content-Type': 'application/javascript'}
