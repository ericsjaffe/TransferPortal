from flask import Flask, render_template, jsonify
from scraper import get_ranking_data

app = Flask(__name__)

@app.route("/")
def home():
    updates = get_ranking_data()
    return render_template("index.html", updates=updates)

@app.route("/api/updates")
def api_updates():
    return jsonify(get_ranking_data())

if __name__ == "__main__":
    app.run(debug=True)
