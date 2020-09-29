from flask import Flask, url_for

# create a Flask app for sample_19
app = Flask(__name__)

# define view function for "/" url
@app.route("/")
def Hello():
    return "Hello World!"

# define view function for "/info"
@app.route("/info")
def info():
    name = "Abi"
    html = """
    <b><center>
    Hello, World!
    My name is {}
    </center></b>
    """.format(name)
    return html

@app.route("/name/<yourname>")
def display_name(yourname: str):
    return "Hello, World! {}".format(yourname)

@app.route("/age/<int:age>")
def display_age(age: int):
    return "You are {} years old".format(age)

@app.route("/say_hello")
def say_hello():
    html = """
    <a href={}> Hello, World!</a>
    """
    # url_for gives href the link to hello_from_cat
    # in other words,
    # href={} becomes href="/hello_from_cat"
    html = html.format(url_for("hello_from_cat"))
    return html

@app.route("/hello_from_cat")
def hello_from_cat():
    # links src to static/cat.jpg
    return "<img src={}>".format(
        url_for("static", filename="cat.jpg")
    )

if __name__ == "__main__":
    # run the Flask app in localhost at port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)