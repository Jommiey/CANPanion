from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import qtawesome as qta


class TraceWindowToolBar(QFrame):
    def __init__(self):
        super().__init__()

        # Style layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.setStyleSheet(
            """
            background-color: #353e4d;
            QFrame {
                border: 0px;
            }
            """)
        self.setFrameShape(QFrame.StyledPanel)

        # Create pause button
        self.pauseButton = QPushButton()
        self.pauseButton.setDisabled(True)
        self.pauseButton.setCheckable(True)
        self.pauseButton.setChecked(True)
        self.pauseButton.setFixedSize(24, 24)
        self.pauseButton.setIcon(qta.icon('fa5s.pause', color='#F05454'))
        self.layout.addWidget(self.pauseButton)

        # Create spacer item
        self.layout.addItem(QSpacerItem(
            100, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
