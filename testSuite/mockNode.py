import can
import threading
import time
import random
from PyQt6.QtCore import QObject


class MockNode(QObject):
    def __init__(self, nodeId, channel, interface, bitrate):
        super().__init__()

        self.nodeId = nodeId

        # Start sending messages
        self.bus = can.interface.Bus(
            channel=channel, interface=interface, bitrate=bitrate)
        thread = threading.Thread(target=self.canSendMsg, args=(self.bus, ))
        thread.daemon = True
        thread.start()

    def canSendMsg(self, bus):
        while True:
            msgData = [random.randint(0, 255)
                       for _ in range(8)]
            msg = can.Message(arbitration_id=self.nodeId, data=msgData)
            bus.send(msg)
            time.sleep(.02)

    def canReceiveMsg(self, bus):
        pass
