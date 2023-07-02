import can
import threading
from PyQt6.QtCore import pyqtSignal, QObject


class CanServer(QObject):
    canMessageReceived = pyqtSignal(can.message.Message)

    def __init__(self, channel, interface, bitrate):
        super().__init__()

        self.bus = can.interface.Bus(
            channel=channel, interface=interface, bitrate=bitrate)

    def emitLatestCanMessage(self, message):
        self.canMessageReceived.emit(message)

    def startListening(self):
        thread = threading.Thread(target=self.canListen, args=(self.bus, ))
        thread.daemon = True
        thread.start()

    def canListen(self, bus):
        while True:
            receivedMessage = bus.recv()
            if receivedMessage:
                self.emitLatestCanMessage(receivedMessage)
