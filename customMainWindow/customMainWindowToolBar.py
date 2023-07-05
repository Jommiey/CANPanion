from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import qtawesome as qta


class ToolBar(QToolBar):
    traceActiveStatus = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.setIconSize(QSize(32, 32))
        self.setStyleSheet(
            """
                background-color: #EEEEEE;
                border: 1px solid #CCCCCC;
            """)
        self.setMovable(False)

        # Add start button
        self.startButton = QAction(self)
        self.startButtonIcon = qta.icon('fa5s.power-off', color='#3CB043')
        self.startButton.setCheckable(True)
        self.startButton.setIcon(self.startButtonIcon)
        self.startButton.triggered.connect(self.startButtonClicked)
        self.startButtonActive = False
        self.addAction(self.startButton)

        self.addSeparator()

    def startButtonClicked(self):
        # Invert active status
        self.startButtonActive = self.startButton.isChecked()

        # Set start button depending on status
        if self.startButtonActive:
            self.startButtonIcon = qta.icon(
                'fa5s.circle', color='#F05454')
        else:
            self.startButtonIcon = qta.icon(
                'fa5s.power-off', color='#589d5d')
        self.startButton.setIcon(self.startButtonIcon)

        # Emit status of start button to listeners
        self.traceActiveStatus.emit(self.startButtonActive)
