import can
import threading
import random
from PyQt6.QtCore import QObject


class MockNode(QObject):
    def __init__(self, nodeId):
        super().__init__()

        # Set up object dictionary
        self.objectDictionary = {
            '0x20f0': self._memoryAccessRead,
        }

        self.nodeId = nodeId
        self.bus = can.interface.Bus(
            channel='test', interface='virtual', bitrate=500000)
        self.bus.set_filters([{"can_id": self.nodeId, "can_mask": 0x7F}])

    def start(self):
        self.thread = threading.Thread(target=self._listen)
        self.thread.start()

    def processReceivedMessage(self, message):
        index = hex(message.data[2] << 8 | message.data[1])
        subindex = hex(message.data[3])
        self.objectDictionary[index](subindex)

    def _sendMessageResponse(self, data):
        message = can.Message(arbitration_id=0x48E, data=data)
        self.bus.send(message)

    def _listen(self):
        while True:
            message = self.bus.recv()
            self.processReceivedMessage(message)

    def _memoryAccessRead(self, subindex):
        data = [0x60, 0xF0, 0x20, int(subindex, 16), 0x00, 0x00, 0x00, 0x00]

        if subindex == '0x1':
            data[4] = random.randint(0, 254)
        else:
            data[0] = 0x80

        self._sendMessageResponse(data)
