
"""Query Parameters"""
from maths.mathematics import summation, subtraction, multiplication
from flask import Flask, render_template, request  # <-- 'request' zaroori hai
app = Flask(__name__)
@app.route("/")
def hello_world():
    """This is the home route that renders the index.html template."""
    return render_template("index.html")

@app.route("/sum")
def add():
    """This route returns the sum of two numbers from query parameters."""
    # Browser se 'num1' aur 'num2' ki value pakadna
    n1 = float(request.args.get('num1'))
    n2 = float(request.args.get('num2'))

    result = summation(n1, n2)
    return f"The sum of {n1} and {n2} is: {result}"

# Isi tarah subtract aur multiply mein bhi badlav karein

@app.route("/subtract")
def sub():
    """This route returns the difference of two numbers from query parameters."""
    # Browser se 'num1' aur 'num2' ki value pakadna
    n1 = float(request.args.get('num1'))
    n2 = float(request.args.get('num2'))

    result = subtraction(n1, n2)
    return f"The difference of {n1} and {n2} is: {result}"

@app.route("/multiply")
def mult():
    """This route returns the product of two numbers from query parameters."""
    # Browser se 'num1' aur 'num2' ki value pakadna
    n1 = float(request.args.get('num1'))
    n2 = float(request.args.get('num2'))

    result = multiplication(n1, n2)
    return f"The product of {n1} and {n2} is: {result}"
if __name__ == "__main__":
    app.run(debug=True)
