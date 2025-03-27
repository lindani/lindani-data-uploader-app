from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=["GET"])
def home():
    return jsonify({'massage': "Welcome to the Home API!"})


if __name__== "__main__":
    app.run(debug=True, port=8080)