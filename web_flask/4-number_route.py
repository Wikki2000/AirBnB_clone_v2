#!/usr/bin/python3
"""Create a flask application."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Define the home view."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define hbnb view."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_message(text):
    """Define view function for dynamic routes."""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_message(text="is cool"):
    """Define view function for dynamic routes."""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Define dynamic routes for integer."""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
