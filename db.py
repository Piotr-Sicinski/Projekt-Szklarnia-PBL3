from common import *


def findLastMeas(collection):
    queryAir = {"humidity": {"$exists": True}}
    querySoil = {"moisture": {"$exists": True}}
    print(collection.find(queryAir).sort("timestamp", -1)[1])
    # i jak tutaj wydobyć konkretną temp?
    #print(collection.find(queryAir).sort("timestamp", -1)[1]["temperature"])
    print(collection.find(querySoil).sort("timestamp", -1)[1])


def findMeasDay(collection, noDays=1):
    boundaryTime = str(datetime.now() - timedelta(days=noDays))
    query = {"timestamp": {"$gt": boundaryTime}}
    for meas in collection.find(query).sort("timestamp", -1):
        print(meas)


def main():
    dbName = "projekt_szklarnie"
    dbColection = "test"

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbName]
    mycol = mydb[dbColection]

    #findLastMeas(mycol)
    findMeasDay(mycol)


if __name__ == "__main__":
    main()
