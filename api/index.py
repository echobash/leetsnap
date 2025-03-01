from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Welcome to Vercel with Python!"

# Required for Vercel (acts as entry point)
def handler(event, context):
    return app(event, context)
