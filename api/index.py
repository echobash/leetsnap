from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World! Flask API on Vercel."})

# Vercel requires a proper handler function
from mangum import Mangum
handler = Mangum(app)

