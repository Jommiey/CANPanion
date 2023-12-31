from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class GraphicsWindow(QWidget):
    def __init__(self, canServer):
        super().__init__()

        self.signals = ['ActualSpeed', 'WantedSpeed']

        # Set layout
        self.layout = QGridLayout()
        self.layout.addLayout(SignalsLayout(self.signals), 0, 1,
                              alignment=Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)


class SignalsLayout(QVBoxLayout):
    def __init__(self, signals):
        super().__init__()

        # Add all signals to the signal window
        for i in signals:
            self.addWidget(QCheckBox(i))
