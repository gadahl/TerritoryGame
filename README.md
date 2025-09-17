# Territory Game Sample Project

## Technologies Used
- **Python 3**
- **Flask** (web framework)
- **HTML** (for templates)
- **JavaScript** (for client-side interactivity)


## Project File Structure
```
SampleFlask/
├── main.py                # Main Flask application
├── README.md              # Project overview
├── home-spectator.html    # Spectator view template
├── home-player.html       # Player view template
└── login.html             # Login form template
```


## Contents of `app.py`
- Initializes the Flask app and sets a secret key for sessions.
- Stores public and private player info in dictionaries.
- Uses session cookies to keep users signed in individually.
- Defines several API endpoints, listed below.


### GET endpoints
A "GET" request is the default request type. It is made when you enter a URL into a web browser or when you are redirected to another URL. A successful response from the server will contain the data you requested.

- Routes that respond with HTML:
  - `/` : Main page, shows public info and private info if logged in.
  - `/login` : Presents the user with the login form.
- Routes that respond with JSON:
  - `/data/players` : Returns public player info as JSON.
- Routes that redirect you to another URL:
  - `/logout` : Logs out the current user and redirects to the main page.


### POST endpoints 
A "POST" request is made when you submit an HTML form. The data is sent to the server and it processes your request. It should then redirect you to the page you expect it to.

- `/login` : Logs in the user if they provide valid credentials.
  - `username: string` - the username of the user to sign in as
- `/set_strategy` : Sets the strategy of a logged-in player.
  - `strategy: string` - the strategy to change to


## HTML Files
- **home-spectator.html**: Spectator view, shows public info for all players.
- **home-player.html**: Player view, same as spectator view, but also includes private info and strategy options for the logged-in player.
- **login.html**: Login form for users to enter credentials.

Each HTML file is loaded and rendered using Flask's `render_template_string`, allowing dynamic content to be displayed based on the user's session and actions.

## Package manager (`uv`)

[`uv`](https://github.com/astral-sh/uv) is the package manager that was used to set up this project (so you might want to use it too). It functions similarly to Rust's `cargo` tool. It's pretty nice to work with!

### Installation

| Platform | Command                                                                                  | 
|----------|------------------------------------------------------------------------------------------|
| Windows  | ```powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"```|
| Linux    | ```curl -Ls https://astral.sh/uv/install.sh \| bash```                                   |

[//]: # (comment: make sure to replace "\|" with "|" if you're copying directly from this md file)

### Usage

Before you run the program for the first time, run `uv sync`, which sets up all of the necessary packages and a virtual environment.

Use `uv run python main.py` to start the program inside of its virtual environment. No need to activate or deactivate virtual environments, just prefix the command with "uv run".