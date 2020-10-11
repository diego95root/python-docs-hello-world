from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by GoDiego (<a href=https://hackerone.com/diegobernal>https://hackerone.com/diegobernal</a>)"
