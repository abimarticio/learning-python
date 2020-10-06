from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    id = request.args.get("id", None)
    if id is None:
        return "ID not found"
    else:
        return " Opening database entry #{}".format(id)