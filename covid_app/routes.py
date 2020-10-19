from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder='static')

COVID_API_URL = "https://api.covid19api.com"


@app.route("/covid/summary")
def get_all_countries():
    path = "/summary"
    summary = requests.get(COVID_API_URL+path).json()
    return render_template("summary.html", summary=summary, title="Countries")


@app.route("/covid/<country_slug>")
def country_day_one_confirmed_cases(country_slug):
    path = f"/dayone/country/{country_slug}/status/confirmed"
    cases_day = requests.get(COVID_API_URL+path).json()
    return render_template("country_day_one_confirmed_cases.html", cases_day=cases_day)


@app.template_filter()
def numberFormat(value):
    return format(int(value), ",d")

