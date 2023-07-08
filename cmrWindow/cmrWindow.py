from constants.constants import *

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
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

        # Always start with 1 VariableItem
        self.layout.addWidget(VariableItem())

        # Setup AddVariableItemButton
        self.addVariableItemButton = AddVariableItem()
        self.layout.addWidget(self.addVariableItemButton)
        self.layout.setAlignment(
            self.addVariableItemButton, Qt.AlignmentFlag.AlignHCenter)

    def addVariableItem(self):
        """
        Add a new VariableItem to layout
        """
        self.layout.insertWidget(self.layout.count() - 1, VariableItem())


class AddVariableItem(QPushButton):
    """
    Class representing a button to create new VariableItems
    """

    def __init__(self):
        super().__init__()

        self.setText("Add")
        self.setFixedSize(80, 40)
        self.setIcon(
            qta.icon('fa5.plus-square', color=COLORS[COLOR_SCHEME]['GREEN']))
        self.setIconSize(QSize(30, 30))
        self.clicked.connect(self.addClicked)

    def addClicked(self):
        """
        Call function in parent to add new VariableItem widget
        """
        self.parentWidget().addVariableItem()


class VariableItem(QWidget):
    """
    Class representing a variable item
    """

    def __init__(self):
        super().__init__()

        # Set layout
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.setLayout(self.layout)

        # Add remove button
        self.removeButton = QPushButton(" ")
        self.removeButton.setMinimumSize(15, 30)
        self.removeButton.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.removeButton.setStyleSheet(
            f"QPushButton {{ background-color: {COLORS[COLOR_SCHEME]['RED']};"
            f"border: 1px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR']};"
            f"border-top-left-radius: 5px;"
            f"border-top-right-radius: 0px;"
            f"border-bottom-left-radius: 5px;"
            f"border-bottom-right-radius: 0px; }}"

            f"QPushButton:hover {{ border: 2px solid {COLORS[COLOR_SCHEME]['MAROON']}; }}"
        )
        self.removeButton.clicked.connect(self.deleteSelf)
        self.layout.addWidget(self.removeButton, 0, 0, 1, 1)

        # Add frame to hold everything but the remove button
        self.frame = QFrame()
        self.frameLayout = QGridLayout()
        self.setStyleSheet(
            f"background-color: {COLORS[COLOR_SCHEME]['SECONDARY_COLOR']};"
            f"border: 1px solid {COLORS[COLOR_SCHEME]['THIRD_COLOR']};"
            f"border-top-right-radius: 5px;"
            f"border-bottom-right-radius: 5px;"
        )
        self.frameLayout.setSpacing(0)
        self.frame.setLayout(self.frameLayout)
        self.layout.addWidget(self.frame, 0, 1, 1, 2)
        self.layout.setColumnStretch(1, 2)

        # Add text field
        self.inputTextField = QLineEdit()
        self.inputTextField.setPlaceholderText("Enter variable name...")
        self.inputTextField.setMinimumSize(30, 30)
        self.inputTextField.setStyleSheet(
            f"QLineEdit {{ margin: 0px 10px 0px 0px; }}"
            f"QLineEdit {{ padding: 0px 5px 0px 5px; }}"
            f"QLineEdit {{ border: 1px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR']}; }}"
            f"QLineEdit {{ border-radius: 5px; }}"
            f"QLineEdit:hover {{ border: 2px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED']}; }}"
            f"QLineEdit:focus {{ border: 2px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR_FOCUSED']}; }}"
        )
        self.frameLayout.addWidget(
            self.inputTextField, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.frameLayout.setColumnStretch(0, 1)

        # Add send button
        self.sendButton = QPushButton("Send")
        self.sendButton.setIcon(
            qta.icon('fa5.paper-plane', color=COLORS[COLOR_SCHEME]['GREEN']))
        self.sendButton.setMinimumSize(30, 30)
        self.sendButton.setStyleSheet(
            f"QPushButton {{ margin: 0px 10px 0px 0px; }}"
            f"QPushButton {{ padding: 0px 5px 0px 5px; }}"
            f"QPushButton {{ border: 1px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR']}; }}"
            f"QPushButton {{ border-radius: 5px; }}"
            f"QPushButton:hover {{ border: 2px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED']}; }}"
            f"QPushButton:pressed {{ border: 2px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR_FOCUSED']}; }}"
        )
        self.frameLayout.addWidget(
            self.sendButton, 0, 1, Qt.AlignmentFlag.AlignTop)

        # Add result text field to a scrollable area
        self.resultScrollArea = QScrollArea()
        self.resultScrollArea.setWidgetResizable(True)
        self.resultScrollArea.setMaximumHeight(300)
        self.resultScrollArea.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        self.resultScrollArea.setStyleSheet(
            f"QScrollArea {{ padding: 5px 5px 5px 5px; }}"
            f"QScrollArea {{ border: 1px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR']}; }}"
            f"QScrollArea {{ border-radius: 5px; }}"
            f"QScrollArea:hover {{ border: 2px solid {COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED']}; }}"
        )
        self.resultTextField = QLabel()
        self.resultTextField.setStyleSheet(
            f"QLabel {{ border: 0px; }}"
        )
        self.resultTextField.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.resultScrollArea.setWidget(self.resultTextField)
        self.frameLayout.addWidget(self.resultScrollArea, 0, 3)
        self.frameLayout.setColumnStretch(3, 3)

    def deleteSelf(self):
        """
        Delete self
        """
        parentWidget = self.parentWidget()

        # Delete self
        parentWidget.layout.removeWidget(self)
        self.deleteLater()
