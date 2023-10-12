import json
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Load data from the JSON file
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)["data"]

# Check the status of the external API
def check_api_status():
    try:
        api_status_response = requests.get("https://www.travel-advisory.info/api")
        api_status = api_status_response.json()["api_status"]
        return api_status
    except Exception as e:
        return {"error": str(e)}

# Convert country name to country code
def convert_to_country_code(country_name, data):
    for code, country_data in data.items():
        if country_data["name"].lower() == country_name.lower():
            return code
    return "Country not found"

@app.route("/health")
def health():
    return "Service is healthy"

@app.route("/diag")
def diag():
    api_status = check_api_status()
    return jsonify(api_status)

@app.route("/convert/<string:country_name>")
def convert(country_name):
    data = load_data()
    country_code = convert_to_country_code(country_name, data)
    return jsonify({"country_name": country_name, "country_code": country_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
