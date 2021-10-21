from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder="templates")


@app.route("", methods=["GET","POST"])
def index():

    return render_template(
       "index.html",
    )


app.run(addr="0.0.0.0", port=8000)