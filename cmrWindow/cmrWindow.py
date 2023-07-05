from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from functools import partial
import qtawesome as qta


class CmrWindow(QWidget):
    """
    Container for the CMR window
    """

    def __init__(self):
        super().__init__()

        # Set layout
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

        # Add 1 variable item as default
        self.layout.addWidget(VariableItem())


class VariableItem(QWidget):
    """
    Class representing a variable item
    """

    def __init__(self):
        super().__init__()

        # Set layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Add remove button
        self.removeButton = QPushButton()
        self.removeButton.setIcon(
            qta.icon('ph.x-circle', color='#F05454'))
        self.layout.addWidget(self.removeButton)

        # Add text field
        self.textField = QLineEdit()
        self.textField.setPlaceholderText("Enter variable name...")
        self.layout.addWidget(self.textField)

        # Add send button
        self.sendButton = SendButton("Send")
        self.sendButton.setIcon(qta.icon('fa5.paper-plane', color='#3CB043'))
        self.sendButton.clicked.connect(self.onSendButtonClick)
        self.layout.addWidget(self.sendButton)

    def onSendButtonClick(self):
        print("Clicked")


class SendButton(QPushButton):
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setChecked(not self.isChecked)
        elif event.button() == Qt.MouseButton.RightButton:
            print("Right button")
