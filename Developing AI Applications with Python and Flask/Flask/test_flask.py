"""
This is MyFirstApplication
"""
from flask import Flask
my_app = Flask("MyFirstApplication")

@my_app.route("/")
def hello_world():
    """Returns a greeting message."""
    return "Hello World!"

if __name__ == "__main__":
    my_app.run(debug=True)
