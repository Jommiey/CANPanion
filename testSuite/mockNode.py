# Library includes
import can
import threading
import random
from PyQt6.QtCore import QObject

# File includes
from canServer.canServer import *
from utilities.utilities import *
from constants.constants import *


class MockNode(QObject):
    def __init__(self, nodeId, canServer):
        super().__init__()

        self.nodeId = nodeId

        # Setup listener
        self.listener = CanListener()
        self.listener.registerReceive(CMR_TO_ICH_SDO)
        self.canServer = canServer
        self.canServer.registerListener(self.listener)

    def update(self):
        message = self.listener.get_message()
        if message:
            print("received", message)
