import json
import time

from flask import Flask, request
from flask.helpers import abort, flash, make_response, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from werkzeug.wrappers.response import Response

app = Flask(__name__)

messages = []

clients = []


@app.route("/")
def index():
    if request.cookies.get("username") is not None:
        return redirect(url_for("homeFunc"))

    return redirect(url_for("loginFunc"))


@app.route("/events")
def events():
    def stream():
        q = []
        clients.append(q)

        try:
            while True:
                if q:
                    print(f"{q[0]} is sent")
                    yield f"data: {q.pop(0)}\n\n"
                time.sleep(0.1)
        finally:
            clients.remove(q)

    return Response(stream(), mimetype="text/event-stream")


@app.route("/history")
def historyGet():
    def giveMessages():
        return json.dumps(messages)

    return giveMessages()


def sendMessage(msg):
    for q in clients:
        print(f"Sending {msg}")
        q.append(msg)


@app.route("/login", methods=["GET", "POST"])
def loginFunc():
    if request.method == "POST":
        name = request.form.get("username") or "NAN"
        resp = make_response(redirect(url_for("index")))
        resp.set_cookie("username", name)
        return resp

    return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def homeFunc():
    if request.cookies.get("username") is None:
        abort(401)
    page = ""

    with open("templates/home.html", "r") as f:
        page = f.read()

    page = page.replace("USERNAME", str(request.cookies.get("username")))
    return page


@app.route("/submit", methods=["POST"])
def submit():
    message = f"{request.cookies.get('username')}: {request.form.get('message')}"
    sendMessage(message)
    messages.append(message)

    return "", 204


def convertMessagesIntoHtml():
    result = ""
    temp = ""

    with open("templates/messageTemp.html", "r") as f:
        temp = f.read()

    for i in messages:
        result += temp.format(i)

    return result
