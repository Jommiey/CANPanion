import can
import threading
from PyQt6.QtCore import pyqtSignal, QObject


class CanServer(QObject):
    canMessageReceived = pyqtSignal(can.message.Message)

    def __init__(self, channel, interface, bitrate):
        super().__init__()

        self.bus = can.interface.Bus(
            channel=channel, interface=interface, bitrate=bitrate)

    def readVariableValueOnce(self, variableName):
        print("Reading:", variableName)
        message = can.Message(arbitration_id=0x50E, data=[
                              0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.bus.send(message)
        self.bus.recv(timeout=20)

    def readVariableValuePeriodically(self, variableName, period):
        print("Reading", variableName, "every", float(period) / 1000, "s")
        message = can.Message(arbitration_id=0x50E, data=[
                              0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.bus.send_periodic(message, float(period) / 1000)

    def emitLatestCanMessage(self, message):
        self.canMessageReceived.emit(message)

    def startListening(self):
        thread = threading.Thread(target=self.canListen)
        thread.daemon = True
        thread.start()

    def canListen(self):
        while True:
            receivedMessage = self.bus.recv()
            if receivedMessage:
                self.emitLatestCanMessage(receivedMessage)
