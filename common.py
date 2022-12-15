from abc import ABC, abstractmethod
from time import sleep
from datetime import datetime, timedelta
import random
import pymongo
import json


class Receiver(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError(
            'users must define __init__ to use this base class')

    @abstractmethod
    def receive() -> dict:
        pass


class Writer(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError(
            'users must define __init__ to use this base class')

    @abstractmethod
    def write(data: dict):
        pass


class BTReceiver(Receiver):
    def __init__(self) -> None:
        # tutaj cały init BT, adresy itp
        pass

    def receive() -> dict:
        """
        ma zwracać jsona w postaci dicta. Oczekujemy takich dwóch typów.
        {
            "sensorId": 0,
            "timestamp": "2022-12-14 23:47:40.531669",
            "temperature": 24,
            "humidity": 17
        }
        Albo
        {
            "sensorId": 0,
            "timestamp": "2022-12-14 23:47:45.534343",
            "moisture": 47
        }

        Proponuje, abyś użył funkcji generateFakePayload do testów i spróbował przepychać takie stringi bądź pliki nwm.
        writer = TerminalWriter() tak ustawiasz do testów
        pip install pymongo - aby Ci się nie sypał cały skrypt.
        """
        pass


class TestReceiver(Receiver):
    def __init__(self) -> None:
        pass

    def receive(self) -> dict:
        sleep(5)
        payload = generateFakePayload(2)
        return payload


class TerminalWriter(Writer):
    def __init__(self) -> None:
        pass

    def write(self, data):
        # pprint(data)
        print(json.dumps(data, indent=4))


class DBWriter(Writer):
    def __init__(self, dbName="projekt_szklarnie", dbColection="test") -> None:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient[dbName]
        self.mycol = mydb[dbColection]

    def write(self, data: dict):
        x = self.mycol.insert_one(data)
        print(x)


def generateFakePayload(noSensorNodes: int, measType="random") -> dict:
    """Generates fake payload for testing purpose

    Args:
        noSensorNodes (int): number of nodes to be simulated
        measType (str, optional): type of massages that are simulated "air", "soil". Defaults to "random".

    Returns:
        dict: Generated messang
    """

    measTypeDef = ["air", "soil"]

    if measType == "random":
        measType = random.choice(measTypeDef)

    payload = {
        "sensorId": random.randint(0, noSensorNodes-1),
        "timestamp": str(datetime.now())
    }

    if measType == "air":
        payload["temperature"] = random.randint(15, 25)
        payload["humidity"] = random.randint(0, 100)
    else:
        payload["moisture"] = random.randint(30, 90)

    return payload
