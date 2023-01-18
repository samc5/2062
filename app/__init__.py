from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def first():
    return render_template("1.html")



@app.route("/1", methods = ["POST", "GET"])
def second():
    return render_template("2.html")

@app.route("/2", methods = ["POST", "GET"])
def third():
    return render_template("3.html")

@app.route("/3", methods = ["POST", "GET"])
def fourth():
    return render_template("4.html")
@app.route("/4", methods = ["POST", "GET"])
def fifth():
    return render_template("5.html")

@app.route("/5", methods = ["POST", "GET"])
def sixth():
    return render_template("6.html")
@app.route("/6", methods = ["POST", "GET"])
def seventh():
    return render_template("7.html")
@app.route("/7", methods = ["POST", "GET"])
def eigth():
    return render_template("8.html")
@app.route("/8", methods = ["POST", "GET"])
def ninth():
    return render_template("9.html")
@app.route("/9", methods = ["POST", "GET"])
def tenth():
    return render_template("10.html")
@app.route("/10", methods = ["POST", "GET"])
def eleventh():
    return render_template("11.html")

if __name__ == "__main__":
  app.debug = True
  app.run()