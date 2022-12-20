from common import *


class GatewayNode():
    """class for gateway node
    """

    def __init__(self, receiver: Receiver, writer: Writer):
        self.receiver = receiver
        self.writer = writer

    def receive(self) -> dict:
        lastMeas = self.receiver.receive()
        return lastMeas

    def write(self, data: dict):
        self.writer.write(data)

    def run(self):
        while (True):
            message = self.receive()
            self.write(message)


def main():
    # init bla bla bla
    global receivedData
    global newDataArrived

    receiver = BTReceiver()  # GenDataReceiver(datetime(2022, 9, 1))
    writer = TerminalWriter()  # DBWriter(dbColection="dataset2")
    gateway = GatewayNode(receiver, writer)
    gateway.run()


if __name__ == "__main__":
    main()
