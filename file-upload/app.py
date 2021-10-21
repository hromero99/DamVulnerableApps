from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os
app = Flask(__name__, template_folder="templates")
UPLOAD_FOLDER = "media"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(f"media/{file.filename}")

    return render_template(
       "index.html",
    )


@app.route("/image/<image>", methods=["GET"])
def images(image):
    if image in os.listdir("media"):
        return image
    else:
        return "None"



app.run(host="0.0.0.0", port=8000)
