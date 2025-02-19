from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def index(name):
    return render_template("home.html", content=name, r=3)


if __name__ == '__main__':
    app.run()
