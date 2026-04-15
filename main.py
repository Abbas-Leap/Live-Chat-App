import json

from flask import Flask, request
from flask.helpers import make_response, url_for
from flask.json import jsonify
from flask.templating import render_template
from werkzeug.utils import redirect

from features.login import api as loginAPI
from features.validateCookies import api as validateCookiesAPI

app = Flask(__name__)


@app.route("/")
def index():
    if not validateCookiesAPI.validateCookies(cookies=request.cookies.items()):
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


@app.route("/home")
def homePageFunc():
    return "Home"
