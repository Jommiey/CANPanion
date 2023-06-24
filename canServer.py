import can
import threading
from PyQt6.QtCore import pyqtSignal, QObject


class CanServer(QObject):
    canMessageReceived = pyqtSignal(can.message.Message)

    def __init__(self, channel, interface):
        super().__init__()

        self.channel = channel
        self.interface = interface

    def emitLatestCanMessage(self, message):
        self.canMessageReceived.emit(message)

    def startListening(self):
        bus = can.interface.Bus(channel=self.channel,
                                interface=self.interface, start=0)
        thread = threading.Thread(target=self.canListen, args=(bus, ))
        thread.daemon = True
        thread.start()

    def canListen(self, bus):
        while True:
            receivedMessage = bus.recv()
            if receivedMessage:
                self.emitLatestCanMessage(receivedMessage)
