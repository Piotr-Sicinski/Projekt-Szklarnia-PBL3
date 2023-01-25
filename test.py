#from common import *
import json


def load_config():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return data


print((load_config())["id"])

#print(datetime(2022, 7, 1))
# print(datetime.now())
