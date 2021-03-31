from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='/tmp/demo.log', level=logging.DEBUG)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.route("/")
def hello():
    return "Hello, World!"
