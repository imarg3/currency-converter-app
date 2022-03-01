from flask import Flask, render_template, request
from decimal import Decimal
from forex_python.converter import CurrencyRates
import redis

app = Flask(__name__)
default_key = '1'
cache = redis.StrictRedis(host='back-api.default.svc.cluster.local', port=6379, db=0)
cache.set(default_key, "one")


@app.route("/currency-converter")
def form():
    return render_template("form.html")


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    key = default_key
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        cache.set(key, request.form['cache_value'])

    cache_value = None
    if cache.get(key):
        cache_value = cache.get(key).decode('utf-8')

    return render_template('index.html', key=key, cache_value=cache_value)


@app.route("/currency-converter", methods=["POST"])
def my_form_post():
    c = CurrencyRates(force_decimal=True)
    dollars = request.form["dollars"]
    inr = round(c.convert('USD', 'INR', Decimal(dollars)), 2)

    return render_template("form.html",
                           usd=dollars,
                           inr=inr)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
