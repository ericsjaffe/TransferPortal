from flask import Flask, render_template
import json

app = Flask(__name__)

def get_static_data():
    with open("static_data.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    updates = get_static_data()
    return render_template("index.html", updates=updates)

if __name__ == "__main__":
    app.run(debug=True)
