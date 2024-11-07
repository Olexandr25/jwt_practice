from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "e2897bbd861545eeac3a7f29bd3a7a2a"


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return jsonify({"message": "Token is invalid!"}), 403

        return func(*args, **kwargs)

    return decorated


@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return "You are logged in!"


@app.route("/public")
def public():
    return "Public page"


@app.route("/auth")
@token_required
def auth():
    return "You are authorized!"


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":
        session["logged_in"] = True
        token = jwt.encode(
            {
                "user": username,
                "expiration": str(datetime.now() + timedelta(seconds=120)),
            },
            app.config["SECRET_KEY"],
        )
        return jsonify({"token": token})
    else:
        return make_response(
            "Could not verify!",
            403,
            {"WWW-Authenticate": "Basic realm='Login Required'"},
        )


if __name__ == "__main__":
    app.run(debug=True)
