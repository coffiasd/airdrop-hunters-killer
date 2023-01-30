import time

def calculateLifeTime(startDate):
    EndTime = int(time.time())

    day = int((EndTime - startDate)/86400)
    if day >= 1:
        return day
    else:
        return 1
