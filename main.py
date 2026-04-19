import json

from flask import Flask, Response, request
from flask.helpers import make_response, url_for
from flask.json import jsonify
from flask.templating import render_template
from werkzeug.utils import redirect

from dataBase import api as dataBaseAPI
from features.login import api as loginAPI
from features.validateCookies import api as validateCookiesAPI

app = Flask(__name__)

print(dataBaseAPI.fetchData())
print(dataBaseAPI.addMessage("Hello"))
print(dataBaseAPI.fetchData())


@app.route("/")
def index():
    if not validateCookiesAPI.isValidCookies(cookies=request.cookies.items()):
        resp = make_response(redirect(url_for("loginFunc")))

        for key, _ in request.cookies.items():
            resp.delete_cookie(key=key)

        return resp

    return redirect(url_for("homePageFunc"))


@app.route("/loginComm", methods=["POST"])
def loginCommFunc():
    loginData = request.get_json()

    validVisitorName = loginAPI.validateVisitorName(loginData["visitorName"])

    if validVisitorName["status"] == "error":
        return jsonify(validVisitorName)

    loginAPI.saveVisitorName(loginData["visitorName"])

    resp = make_response(
        jsonify({"status": "ok", "msg": "Successful", "url": url_for("homePageFunc")})
    )

    resp.set_cookie("visitorName", loginData["visitorName"])

    return resp


@app.route("/login", methods=["GET", "POST"])
def loginFunc():
    return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def homePageFunc():
    if not validateCookiesAPI.isValidCookies(cookies=request.cookies.items()):
        return redirect(url_for("index"))

    return render_template("homePage.html")


@app.route("/homeCommOneTime", methods=["POST"])
def homeCommOneTime():
    data = {}

    data["visitorName"] = request.cookies.get("visitorName")
    # Message history
    data["messages"] = dataBaseAPI.fetchData()["messages"]

    return jsonify(data)
