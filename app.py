from flask import Flask
from flask import request
import logging
import os

app = Flask(__name__, static_folder='/opt/defaultsite')

logging.basicConfig(filename='/tmp/demo.log', level=logging.DEBUG)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.route("/")
def hello():
    if os.path.isdir('/home/site/deployments') and len(next(os.walk('/home/site/deployments'))[1]) > 1:
        return app.send_static_file('hostingstart_dep.html')
    else:
        return app.send_static_file('hostingstart.html')
