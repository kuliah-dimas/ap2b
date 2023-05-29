from flask import Flask, request, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


users = {}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and check_password_hash(users.get(username), password=password):
            return f"Welcome {username}"
        else:
            return 'Invalid Username or Password, click here for register user. <a href="' + url_for('login') + '">Here to back</a>'
    else:
        return render_template('login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return 'Username has already registered, click' + url_for('register') + 'to back register'
        else:
            users[username] = generate_password_hash(password)
            return 'Registration successfull, check <a href="' + url_for('login') + '"> here </a> to login'

    else:
        return render_template('register.html')


if __name__ == "__main__":
    app.run()
