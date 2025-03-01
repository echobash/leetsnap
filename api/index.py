from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask API on Vercel."

# Required for Vercel
def handler(event, context):
    return app(event, context)

