from flask import Flask
import os
app = Flask(__name__)


@app.route("/read/<file>/", methods=["GET"])
def read_file(file):
    command = f"cat {file}"
    return os.popen(command).read()


@app.route("/")
def index():
    return "[!] Welcome to system file reader app"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
