#!/usr/bin/python3
"""Create a flask application."""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Return a view if only arg in URL is an integer."""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_odd_or_even(n):
    """Render a template that shows whether the number is odd or even."""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
