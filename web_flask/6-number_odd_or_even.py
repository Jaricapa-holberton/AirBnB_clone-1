#!/usr/bin/python3
"""
First Flask web application, this app is
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
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


# route for '/python'
@app.route("/python", strict_slashes=False)
# route for '/python/(<text>)', for default use "is cool"
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is_cool"):
    """Display “Python ” followed by <text> variable"""
    return "Python {}".format(text.replace("_", " "))


# route for '/number/<int:n>'
@app.route('/number/<int:n>')
def number_page(n):
    """ Redirection for /number/ page and return a number
        only if is integer.
    """
    return ('{} is a number'.format(n))


# route for '/number_template/<int:n>'
@app.route('/number_template/<int:n>')
def number_template(n):
    """ Redirection for /number_template page and return HTML with a number
        only if is integer.
    """
    return render_template('5-number.html', number=n)


# route for '/number_odd_or_even/<int:n>'
@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """ Redirection for /number_odd_even page and return HTML with a number
        only if is integer.
    """
    text = " is odd"
    if n % 2 == 0:
        text = " is even"
    return render_template('6-number_odd_or_even.html', string=str(n)+text)


# app_run modify where execute the app
if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000")
