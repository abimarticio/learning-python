from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    id = request.args.get("id", None)
    if id is None:
        return "ID not found"
    else:
        return " Opening database entry #{}".format(id)

@app.route("/get_correction/<text_input>")
def get_correction(text_input: str):
    corrections = {"rainning": "raining", "raning": "raining"}
    return (
        corrections.get(text_input)
        if text_input in corrections
        else text_input
    )

if __name__ == "__main__":
    # run the Flask app in localhost at port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)