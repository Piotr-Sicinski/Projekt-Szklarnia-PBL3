from abc import ABC, abstractmethod
from time import sleep
from datetime import datetime, timedelta
import random
import pymongo
import json
import pandas as pd
import numpy as np
from bluedot.btcomm import BluetoothServer, BluetoothClient
import ast

newDataArrived = False
receivedData = ''


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


def data_received(data):
    global receivedData
    global newDataArrived

    receivedData = data
    newDataArrived = True


class BTReceiver(Receiver):
    def __init__(self) -> None:
        self.s = BluetoothServer(data_received)

    def receive(self) -> dict:
        global receivedData
        global newDataArrived

        while newDataArrived is False:
            pass
        newDataArrived = False
        print(receivedData)

        return ast.literal_eval(receivedData)


class TestReceiver(Receiver):
    def __init__(self) -> None:
        pass

    def receive(self) -> dict:
        sleep(5)
        payload = generateFakePayload(2)
        return payload


class GenDataReceiver(Receiver):
    def __init__(self, time) -> None:
        generateFakePayloadTime.time = time
        pass

    def receive(self) -> dict:
        # sleep(5)
        payload = generateFakePayloadTime(2)
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


def generateFakePayloadTime(noSensorNodes: int, measType="random") -> dict:

    generateFakePayloadTime.time += timedelta(minutes=15)

    if generateFakePayloadTime.time > datetime(2022, 12, 18):
        raise Exception("Koniec generowania")

    measTypeDef = ["air", "soil"]

    if measType == "random":
        measType = random.choice(measTypeDef)

    payload = {
        "sensorId": random.randint(0, noSensorNodes-1),
        "timestamp": str(generateFakePayloadTime.time)
    }

    if measType == "air":
        payload["temperature"] = random.randint(15, 25)
        payload["humidity"] = random.randint(0, 100)
    else:
        payload["moisture"] = random.randint(30, 90)

    return payload
