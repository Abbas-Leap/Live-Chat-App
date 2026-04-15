from dataBase import api as dataBaseAPI


def visitorNameInDataBase(visitorName):
    visitorNames = dataBaseAPI.fetchData()["visitors"]

    if visitorNames.count(visitorName) == 0:
        return False

    return True


def saveVisitorName(visitorName):
    dataBaseAPI.saveVisitorName(visitorName=visitorName)
