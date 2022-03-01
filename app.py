from decimal import Decimal

from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def my_form_post():
    c = CurrencyRates(force_decimal=True)
    dollars = request.form["dollars"]
    inr = round(c.convert('USD', 'INR', Decimal(dollars)), 2)

    return render_template("form.html",
                           usd=dollars,
                           inr=inr)


if __name__ == "__main__":
    app.run(debug=True)
