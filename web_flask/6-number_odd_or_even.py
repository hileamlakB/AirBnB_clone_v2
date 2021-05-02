from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C " + escape(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    return "Python " + escape(text.replace('_', ' '))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_tmplate(n):
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_eveness(n):
    t = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, type=t)

app.run(host='0.0.0.0', port=5000)
