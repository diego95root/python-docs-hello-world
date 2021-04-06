from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by 0xd0m7 (<a href=https://hackerone.com/0xd0m7>https://hackerone.com/0xd0m7</a>)"
