#!/usr/bin/python3
"""
Start a Flask web application
- listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

# Close session
@app.teardown_appcontext
def teardown(exc):
    """Close SQLAlchemy session."""
    storage.close()

# URL for query list from cities
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display an HTML page
    - H1: “States”
    - UL: list of all State sorted by name (A->Z)
    - LI: <state.id>: <B><state.name></B>
        - UL: list of City
        - LI: <city.id>: <B><city.name></B>
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


# run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
