from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # This ensures it runs on Render
