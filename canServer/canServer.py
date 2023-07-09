import can
import threading
from PyQt6.QtCore import *


class CanServer(QObject):
    def __init__(self):
        super().__init__()

        # Set up variable memory map
        self.memoryMap = {
            'test': 0x40567862
        }

        self.bus = can.interface.Bus(
            channel='test', interface='virtual', bitrate=500000)
        self.listeners = []
        self.transmitters = []

    def readVariableValue(self, variableName, callbackFunction, frequency):
        # Get memory address for variable
        if variableName not in self.memoryMap:
            return callbackFunction(can.Message(data=[0x80, 0xF0, 0x20, 0x01, 0x00, 0x00, 0x00, 0x00]))

        # Setup transmitter to send messages
        message = can.Message(arbitration_id=0x50E, data=[
                              0x40, 0xF0, 0x20, 0x01, 0x00, 0x00, 0x00, 0x00])
        self.bus.send(message)

        # Setup listener to listen to response
