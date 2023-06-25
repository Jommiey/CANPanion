from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class TraceWindowToolBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

    def addButton(self, text, checkable, connectFunction=None):
        pushButton = QPushButton(text)
        pushButton.setCheckable(checkable)
        pushButton.setFixedSize(24, 24)

        if connectFunction:
            pushButton.clicked.connect(connectFunction)

        self.layout.addWidget(pushButton)

    def addSpacer(self, xSize, ySize):
        self.layout.addItem(QSpacerItem(
            xSize, ySize, QSizePolicy.Expanding, QSizePolicy.Minimum))
