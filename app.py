from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/static_data.json")
def static_data():
    return send_from_directory(".", "static_data.json")

if __name__ == "__main__":
    app.run(debug=True)
