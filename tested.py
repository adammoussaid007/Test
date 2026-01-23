from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML = """
<h3>Web Terminal</h3>
<form method="post">
  <input name="cmd" style="width:80%" autofocus>
  <button>Run</button>
</form>
<pre>{{ output }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        try:
            output = subprocess.check_output(
                request.form["cmd"], shell=True, stderr=subprocess.STDOUT, timeout=10
            ).decode()
        except Exception as e:
            output = str(e)
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    port = 8080 # Railway uses $PORT
    app.run(host="0.0.0.0", port=port)
