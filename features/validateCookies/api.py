from dataBase import api as dataBaseAPI


def isValidCookies(cookies) -> bool:
    cookieDict = dict(cookies)

    visitorNames = dataBaseAPI.fetchData()["visitors"]
    try:
        # if name not in database or not found
        if visitorNames.count(cookieDict["visitorName"]) == 0:
            return False
    except KeyError:
        return False

    return True
