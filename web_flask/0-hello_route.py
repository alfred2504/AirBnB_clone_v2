#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
=======
"""script that starts a Flask web application"""


>>>>>>> 90e1dd1802f0535acde0e7429d25ec206b1c955c
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
=======
def index():
>>>>>>> 90e1dd1802f0535acde0e7429d25ec206b1c955c
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(debug=True)
>>>>>>> 90e1dd1802f0535acde0e7429d25ec206b1c955c
