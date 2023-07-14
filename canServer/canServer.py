# Library includes
import can
from PyQt6.QtCore import *

# File includes
from utilities.utilities import *
from constants.constants import *


class CanServer(object):
    """
    Can server
    """

    def __init__(self):
        self.bus = can.interface.Bus(interface='vector',
                                     channel=0,
                                     bitrate=500000)
        self.notifier = can.Notifier(bus=self.bus, listeners=[])

    def registerListener(self, listener):
        self.notifier.add_listener(listener=listener)

    def sendMessage(self, messageId, command, index, subindex, data=None):
        messageData = []

        # Add command specifier to message
        messageData.append(command)

        # Add index to message
        packU16LittleEndian(index, messageData)

        # Add subindex to message
        messageData.append(subindex)

        # Check if there is any data to add to the message
        if not data == None:
            packU32LittleEndian(data, messageData)

        # Create message and send
        message = can.Message(arbitration_id=messageId,
                              data=messageData, is_extended_id=False)
        self.bus.send(msg=message)


class CanListener(can.BufferedReader):
    """
    Can listener
    """

    def __init__(self):
        super().__init__()

        self.registeredMessages = []

    def registerReceive(self, messageId):
        """
        Register a message id to listen for
        """
        self.registeredMessages.append(messageId)

    def on_message_received(self, msg):
        """
        Overload of can.BufferedReader.on_message_received()
        """
        if (msg.arbitration_id in self.registeredMessages):
            return super().on_message_received(msg)

    def get_message(self):
        """
        Overload of can.BufferedReader.get_message()
        """
        return super().get_message(timeout=0)
