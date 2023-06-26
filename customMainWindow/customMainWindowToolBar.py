from PyQt6.QtWidgets import QToolBar, QGraphicsItem
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize, Qt
import qtawesome as qta
from PyQt6.QtCore import pyqtSignal


class ToolBar(QToolBar):
    traceActiveStatus = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.setIconSize(QSize(32, 32))
        self.setStyleSheet("background-color: #353e4d;")
        self.setMovable(False)

        # Add start button
        self.startButton = QAction(self)
        self.startButtonIcon = qta.icon('fa5s.power-off', color='#3CB043')
        self.startButton.setIcon(self.startButtonIcon)
        self.startButton.triggered.connect(self.startButtonClicked)
        self.startButtonActive = False
        self.addAction(self.startButton)

        self.addSeparator()

    def startButtonClicked(self):
        # Invert active status
        self.startButtonActive = not self.startButtonActive

        # Set start button depending on status
        if self.startButtonActive:
            self.startButtonIcon = qta.icon(
                'fa5s.circle', color='#f44336')
        else:
            self.startButtonIcon = qta.icon(
                'fa5s.power-off', color='#589d5d')
        self.startButton.setIcon(self.startButtonIcon)

        # Emit status of start button to listeners
        self.traceActiveStatus.emit(self.startButtonActive)
