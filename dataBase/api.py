import json
from pathlib import Path

basePath = Path(__file__).resolve().parent
filePath = basePath / "data.json"

filePath.write_text(json.dumps({"visitors": [], "messages": []}))


def readFile():
    content = filePath.read_text()

    return content


def saveFile(content):
    formattedContent = json.dumps(content)

    filePath.write_text(formattedContent)


def fetchData() -> dict:
    return json.loads(readFile())


def saveVisitorName(visitorName):
    content = json.loads(readFile())

    content["visitors"].append(visitorName)

    saveFile(content)


def removeVisitorName(visitorName):
    content = json.loads(readFile())

    content["visitors"].remove(visitorName)

    saveFile(content=content)


def saveMessage(message):
    content = json.loads(readFile())

    content["messages"].append(message)

    saveFile(content=content)
