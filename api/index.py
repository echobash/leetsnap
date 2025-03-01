from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World! Flask API on Vercel."})

# Required for Vercel serverless function
def handler(event, context):
    return app(event, context)

