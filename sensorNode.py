from common import *


def main():
    c = BluetoothClient("DC:A6:32:F1:D8:78", None)

    while (True):
        s = generateFakePayload(1)
        string = str(s)
        print(string)
        c.send(string)
        sleep(5)


if __name__ == "__main__":
    main()
