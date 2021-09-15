from application import app
from flask import render_template, request, jsonify
import requests
from fake_useragent import UserAgent
import json

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    temp_user_agent = UserAgent()
    browser_header = {'User-Agent': temp_user_agent.random}
    URL = "https://api.covid19api.com/total/country/India"
    response = requests.get(URL, headers=browser_header)
    if response.ok:
        resp_json = response.json()
        resp_json = sorted(resp_json, key=lambda x:x['Date'],reverse=True)
        # case_data = json.dumps(resp_json,indent=1)
        # print(case_data)
    else:
        cases = "No Record Found"
        print("No cases found")
    return render_template("dashboard.html",cases=resp_json)


@app.route("/case_history", methods=["GET","POST"])
def case_history():
    confirmed = request.args.get("Confirmed")
    active = request.args.get("Active")
    recovered = request.args.get("Recovered")
    deaths = request.args.get("Deaths")
    cases={"Confirmed":confirmed,"Active":active, "Recovered":recovered,"Deaths":deaths}
    return render_template("chart.html",cases = cases)
