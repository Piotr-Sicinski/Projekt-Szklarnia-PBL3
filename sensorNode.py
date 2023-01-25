from sensorRead import *


def load_config():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return data


def main():
    config_data = load_config()
    c = BluetoothClient(config_data["mac_address"], None)

    while (True):
        s = generatePayload(config_data["id"])
        string = str(s)
        print(string)
        c.send(string)
        sleep(15)


if __name__ == "__main__":
    main()
