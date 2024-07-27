#!/usr/bin/python3
"""renders a template with dynamic content."""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_down_storage(error):
    """Remove current session engine."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Renders all states from storage"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
