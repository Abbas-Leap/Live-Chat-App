import json
from pathlib import Path
from time import sleep

dataBaseState = {"reading": False, "writing": False}

basePath = Path(__file__).resolve().parent
filePath = basePath / "data.json"

filePath.write_text(json.dumps({"visitors": [], "messages": []}))
sleep(1)
keys: list = list(json.loads(filePath.read_text()).keys())
sleep(0.1)


def fetchData() -> dict:
    # Change state
    dataBaseState["reading"] = True
    while dataBaseState["writing"]:
        print("waiting for write")
        sleep(0.05)
    # Read
    data = filePath.read_text()
    # Reset
    dataBaseState["reading"] = False
    return json.loads(data)


def writeData(data: dict) -> dict:
    # Validate the data
    if list(data.keys()) != keys:
        return {"status": "declined", "msg": "keys donot match"}
    # Change state
    dataBaseState["writing"] = True
    while dataBaseState["reading"]:
        print("waiting for read")
        sleep(0.05)
    # Write
    filePath.write_text(json.dumps(data))
    # Reset state
    dataBaseState["writing"] = False
    return {"status": "ok", "msg": "successfully changed the data"}


def addVisitorName(visitorName: str) -> dict:
    data = fetchData()

    if visitorName in data["visitors"]:
        return {"status": "declined", "msg": "visitor name already taken"}

    data["visitors"].append(visitorName)

    return writeData(data=data)


def addMessage(message: str) -> dict:
    data = fetchData()

    data["messages"].append(message)

    return writeData(data)
