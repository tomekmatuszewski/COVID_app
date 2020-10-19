from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder='static')

COVID_API_URL = "https://api.covid19api.com"

ENDPOINTS = {
    'summary': '/summary',
    'confirmed_cases': "/dayone/country/{}/status/confirmed",
    'deaths': "/dayone/country/{}/status/deaths",
    'recovered': "/dayone/country/{}/status/recovered",
}


@app.route("/covid/summary")
def get_all_countries():
    summary = requests.get(COVID_API_URL+ENDPOINTS['summary']).json()
    return render_template("summary.html", summary=summary, title="Countries")


@app.route("/covid/<country_slug>")
def country_day_one_cases(country_slug):
    cases_day = requests.get(COVID_API_URL + ENDPOINTS['confirmed_cases'].format(country_slug)).json()
    deaths = requests.get(COVID_API_URL + ENDPOINTS['deaths'].format(country_slug)).json()
    recovered = requests.get(COVID_API_URL + ENDPOINTS['recovered'].format(country_slug)).json()
    title = cases_day[0]['Country']
    country_code = cases_day[0]['CountryCode']
    return render_template("country_day_one_confirmed_cases.html", cases_day=cases_day,
                           title=title, code=country_code, deaths=deaths, recovered=recovered)


@app.route("/covid/country/<country_slug>/<start_date>/<end_date>")
def country_start_end_date_cases(country_slug, start_date, end_date):
    path = COVID_API_URL + f"/country/{country_slug}/status/confirmed?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z"
    cases = requests.get(path).json()
    return render_template("country_start_end_cases.html", cases=cases)

@app.template_filter()
def numberFormat(value):
    return format(int(value), ",d")

