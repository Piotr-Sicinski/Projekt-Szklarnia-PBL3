from common import *


def findMeasDay(noDays=1):
    boundaryTime = str(datetime.now() - timedelta(days=noDays))
    print(datetime.now())
    print(boundaryTime)


findMeasDay()
