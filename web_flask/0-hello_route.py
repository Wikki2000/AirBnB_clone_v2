#!/usr/bin/python3
"""Home route."""
from flask import Flask

# Create and instance of flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Response with Hello HBNB! when querying the root."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
