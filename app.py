from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Use DATABASE_URL from environment variables
app.config["MONGO_URI"] = os.getenv("DATABASE_URL")

mongo = PyMongo(app)

@app.route("/")
def home():
    return "MongoDB Connected Successfully!"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the port Render provides
    app.run(host="0.0.0.0", port=port)

