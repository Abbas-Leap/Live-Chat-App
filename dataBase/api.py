import json
from pathlib import Path

basePath = Path(__file__).resolve().parent
filePath = basePath / "visitors.json"

filePath.write_text(json.dumps({"visitors": []}))


def readFile():
    content = filePath.read_text()

    return content


def saveFile(content):
    formattedContent = json.dumps({"visitors": content})

    filePath.write_text(formattedContent)


def fetchData() -> dict:
    return json.loads(readFile())


def saveVisitorName(visitorName):
    content = json.loads(readFile())["visitors"]

    content.append(visitorName)

    saveFile(content)


def removeVisitorName(visitorName):
    content = json.loads(readFile())["visitors"]

    content.remove(visitorName)

    saveFile(content)
