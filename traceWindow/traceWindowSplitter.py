from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QSplitterHandle


class TraceWindowSplitter(QSplitter):
    """
    Custom QSplitter class
    """

    def __init__(self, orientation):
        super().__init__()

        self.setStyleSheet(
            """
            QSplitter::handle {
                background-color: black;
            }
            QSplitter::handle:horizontal {
                width: 10px;
            }
            """
        )

    def createHandle(self):
        return TraceWindowSplitterHandle(self.orientation(), self)


class TraceWindowSplitterHandle(QSplitterHandle):
    """
    Custom QSplitterHandle class
    """

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)

        self.collapsed = False
        self.setMouseTracking(True)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Set width of first widget to 0
            self.parent().setSizes([0, self.parent().sizes()[1]])

        super().mousePressEvent(event)
