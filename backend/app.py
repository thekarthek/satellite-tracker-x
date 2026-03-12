from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Satellite Tracker Running"

@app.route("/satellite")
def satellite():

    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)