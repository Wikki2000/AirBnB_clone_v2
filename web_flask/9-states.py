#!/usr/bin/python3
"""Render a template with dynamic content."""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_down_storage(error):
    """close database connection."""
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states(id=None):
    """Render the templates with states"""
    if id:
        state = storage.get_by_id(State, id)
        print(state)
        return render_template("9-states.html", state=state)
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
