from flask import Flask, render_template, request, jsonify
import json
import requests
from pprint import pprint
from functools import wraps
from flask import  Response
from cassandra.cluster import Cluster



def check_auth(username, password):
    return username == 'cloudcomputing' and password == 'ecs781'

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

#cluster = Cluster(['cassandra'])
cluster = Cluster(['35.226.36.91'],port=9042)
session = cluster.connect()


app = Flask(__name__)

@app.route("/")
@requires_auth
def index():
    return render_template("index.html")

currency_url_template = 'https://free.currencyconverterapi.com/api/v6/convert?apiKey={key}&q={cur}&compact=ultra&date={start}&endDate={end}'


@app.route('/currencystat', methods=['GET' , 'POST'])
def currencychart():
    my_api_key = request.args.get('key','9a7996420eaad29d1592')
    my_currency = request.form.get("currency")
    my_startdate = request.form.get("start_date")
    my_enddate = request.form.get("end_date")

    rows = session.execute( """select results_id from result.stats where results_currencyname= '{}' ALLOW FILTERING""".format(my_currency))

    for result in rows:
        resultid = result.results_id

    currency_url = currency_url_template.format(key= my_api_key, cur=resultid, start=my_startdate, end=my_enddate)

    resp= requests.get(currency_url)
    if resp.ok:
            showcurrency = resp.json()
    else:
            print(resp.reason)


    return jsonify(showcurrency)


if __name__ == "__main__":
    app.run(debug = True,port=8080)
