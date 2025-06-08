from flask import Flask, render_template, send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open("static_data.json") as f:
        players = json.load(f)
    return render_template('index.html', players=players)

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
