from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class TraceWindowFilter(QWidget):
    """
    Container for the filter window
    """

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        frame = QFrame()
        frame.setLineWidth(0)
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setStretch(0, 1)
        self.setLayout(layout)
