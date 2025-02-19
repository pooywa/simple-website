from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello World!'

@app.route("/<name>")
def userpage(name):
    return f"Hi {name}!"

@app.route("/first")
def firstpage():
    return redirect(url_for("userpage", name="pooya"))

if __name__ == '__main__':
    app.run()