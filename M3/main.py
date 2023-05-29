from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about")
def about():
    return "Halo selamat datang"


@app.route("/nama")
def name():
    return "Nama saya Dimas Febriyanto"


@app.route("/npm")
def npm():
    return "NPM saya 50422430"


@app.route("/kelas")
def kelas():
    return "Kelas saya 1IA24"


@app.route("/mahasiswa")
def mahasiswa():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
