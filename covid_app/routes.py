from flask import Flask, render_template
import requests

app = Flask(__name__)

COVID_API_URL = "https://api.covid19api.com"

ENDPOINTS = {
    "summary": "/summary",
}


@app.route("/covid/summary")
def get_all_countries():
    summary = requests.get(COVID_API_URL+ENDPOINTS["summary"]).json()
    return render_template("summary.html", summary=summary)


@app.route("/covid/<country_slug>")
def country_confirmed_cases(country_slug):
    path = f"/dayone/country/{country_slug}/status/confirmed"
    cases_day = requests.get(COVID_API_URL+path).json()
    return render_template("country_details_info.html", cases_day=cases_day)

