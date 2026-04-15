from dataBase import api as dataBaseAPI


def validateCookies(cookies) -> bool:
    cookieDict = dict(cookies)

    visitorNames = dataBaseAPI.fetchData()["visitors"]

    try:
        if visitorNames.count(cookieDict["visitorName"]) == 0:
            return False
    except KeyError:
        return False

    return True
