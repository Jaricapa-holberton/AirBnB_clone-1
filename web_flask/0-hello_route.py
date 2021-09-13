#!/usr/bin/python3
"""
First Flask web application, this app is
listening on 0.0.0.0, port 5000
"""
from flask import Flask
# instance the class flask
app = Flask(__name__)


# assing to Flask what URL trigger our function
@app.route('/', strict_slashes=False)
# create app for run
def hello():
    """Display “Hello HBNB!”"""
    return 'Hello HBNB!'


# app_run modify where execute the app
if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000")
