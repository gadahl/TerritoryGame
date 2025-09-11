from flask import Flask, render_template_string, redirect, jsonify, request, session

app = Flask(__name__)

app.secret_key = "secret_heehoo"


player_info_public = {
    "Alice": {"territories": ["Hawaii", "Madagascar"]},
    "Bob": {"territories": ["Iceland", "Greenland"]},
    "Charlie": {"territories": ["Australia"]},
}

player_info_private = {
    "Alice": {"food": 5000, "gold": 3000, "strategy": "Idle"},
    "Bob": {"food": 4500, "gold": 3500, "strategy": "Idle"},
    "Charlie": {"food": 6000, "gold": 2000, "strategy": "Idle"},
}

strategies = ["Attack", "Fortify", "Research", "Idle"]


# this is the main page of the app where you see all players' public info and, if logged in, your private info
@app.route("/")
def index():
    username = session.get("username")
    if (username is None):
        with open("client/home-spectator.html") as f:
            html_content = f.read()
        return render_template_string(html_content)
    else:
        with open("client/home-player.html") as f:
            html_content = f.read()
        return render_template_string(html_content, 
                username=username, 
                secrets=player_info_private[username],
                strategies=strategies)

# endpoint that just serves the public player info as JSON
@app.route("/data/players")
def get_players():
    return jsonify(player_info_public)

# serves the javascript file that the HTML files use
@app.route("/script.js")
def get_js():
    with open("client/script.js") as f:
        js_content = f.read()
    return js_content, 200, {'Content-Type': 'application/javascript'}

# login page, both GET (returns the login page to the user) and POST (processes the login form)
@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        with open("client/login.html") as f:
            html_content = f.read()
        return render_template_string(html_content)
    
    else:
        username = request.form.get("username")
        if username not in player_info_public:
            return "User not found", 404
        session["username"] = username
        return redirect("/")

# clears the session and returns to the home page
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

# endpoint to set your strategy, only accessible if logged in
@app.route("/set_strategy", methods=["POST"])
def set_strategy():
    username = session.get("username")
    if not username or username not in player_info_private:
        return "Unauthorized", 401
    strategy = request.form.get("strategy")
    if strategy not in strategies:
        return "Invalid strategy", 400
    player_info_private[username]["strategy"] = strategy
    return redirect("/")