from . import service


def isMessageValid(message: str) -> bool:
    if len(message.strip()) < 1 or len(message.strip()) > 100:
        return False

    return True


def formatMessage(message: str, visitorName: str) -> str:
    return f"{visitorName}: {message}"


def sendMessageToAllClients(message: str):
    service.sendMessageToAllClients(message=message)


def getGeneratorCopy():
    return service.stream()
