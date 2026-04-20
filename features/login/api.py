from . import service


def validateVisitorName(visitorName) -> dict:
    visitorNameTaken = service.visitorNameInDataBase(visitorName=visitorName)

    if visitorNameTaken:
        return {"status": "error", "msg": "Visitor name already taken"}

    return {"status": "ok", "msg": "Visitor name not taken"}


def saveVisitorName(visitorName):
    return service.saveVisitorName(visitorName=visitorName)
