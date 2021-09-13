#!/usr/bin/python3
"""
First Flask web application, this app is
listening on 0.0.0.0, port 5000
"""
from flask import Flask
# instance the class flask
app = Flask(__name__)


# assing to Flask what URL trigger our function
# route for '/'
@app.route('/', strict_slashes=False)
def hello():
    """Display “Hello HBNB!”"""
    return 'Hello HBNB!'


# route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return 'HBNB'


# route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """Display “C ” followed by <text> variable"""
    # save the string from the url and replace "_" for " "
    C_string = "C {}".format(text.replace("_", " "))
    return C_string


# app_run modify where execute the app
if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000")
