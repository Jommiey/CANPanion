# Library includes
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import qtawesome as qta
import can

# File includes
from constants.constants import *
from cmrWindow.cmrWindowStyles import *
from canServer.canServer import *
from utilities.utilities import *


class CmrWindow(QWidget):
    """
    Container for the CMR window
    """

    def __init__(self, canServer):
        super().__init__()

        self.canServer = canServer

        # Set layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setContentsMargins(15, 30, 15, 15)
        self.setLayout(self.layout)

        # Setup AddVariableItemButton
        self.addVariableItemButton = AddVariableItemButton()
        self.layout.addWidget(self.addVariableItemButton)
        self.layout.setAlignment(
            self.addVariableItemButton, Qt.AlignmentFlag.AlignHCenter)

    def addVariableItem(self):
        """
        Add a new VariableItem to layout
        """
        self.layout.insertWidget(
            self.layout.count() - 1, VariableItem(self.canServer, self.layout.count() - 1))

    def preUpdate(self):
        for variableItemIndex in range(0, self.layout.count() - 1):
            try:
                self.layout.itemAt(variableItemIndex).widget().preUpdate()
            except AttributeError:
                print("Failed to call preUpdate for:",  # variableItemIndex)
                      str(self.layout.itemAt(variableItemIndex)))

    def postUpdate(self):
        for variableItemIndex in range(0, self.layout.count() - 1):
            try:
                self.layout.itemAt(variableItemIndex).widget().postUpdate()
            except AttributeError:
                print("Failed to call postUpdate for:",
                      str(self.layout.itemAt(variableItemIndex)))


class AddVariableItemButton(QPushButton):
    """
    Class representing a button to create new VariableItems
    """

    def __init__(self):
        super().__init__()

        self.setText("Add row")
        self.setFixedSize(120, 40)
        self.setIcon(
            qta.icon('fa5.plus-square', color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR']))
        self.setIconSize(QSize(30, 30))
        self.setStyleSheet(style_addRowButton)
        self.clicked.connect(self.addClicked)

    def addClicked(self):
        """
        Call function in parent to add new VariableItem widget
        """
        self.parentWidget().addVariableItem()

    def preUpdate(self):
        pass

    def postUpdate(self):
        pass


class VariableItem(QWidget):
    """
    Class representing a variable item
    """

    def __init__(self, canServer, layoutCount):
        super().__init__()

        self.expectingResponse = False

        # Setup listener
        self.listener = CanListener()
        self.listener.registerReceive(ICH_TO_CMR_SDO)
        self.canServer = canServer
        self.canServer.registerListener(self.listener)

        # Set layout
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.setLayout(self.layout)

        # Add remove button
        self.removeButton = QPushButton()
        self.removeButton.setIcon(
            qta.icon('fa5.trash-alt', color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR']))
        self.removeButton.setIconSize(QSize(20, 20))
        self.removeButton.setMinimumSize(15, 15)
        self.removeButton.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.removeButton.setStyleSheet(style_removeButton)
        self.removeButton.clicked.connect(self.removeButtonClicked)
        self.removeButton.released.connect(self.removeButtonReleased)
        self.layout.addWidget(self.removeButton, 0, 0, 1, 1)

        # Add frame to hold everything but the remove button
        self.frame = QFrame()
        self.frameLayout = QGridLayout()
        self.setStyleSheet(style_frame)
        self.frameLayout.setSpacing(0)
        self.frame.setLayout(self.frameLayout)
        self.layout.addWidget(self.frame, 0, 1, 1, 2)
        self.layout.setColumnStretch(1, 2)

        # Add text field
        self.inputTextField = QLineEdit()
        self.inputTextField.setPlaceholderText(str(layoutCount))
        # self.inputTextField.setPlaceholderText("Enter variable name...")
        self.inputTextField.setFixedSize(200, 45)
        self.inputTextField.setStyleSheet(style_variableNameTextField)
        self.frameLayout.addWidget(
            self.inputTextField, 0, 0, Qt.AlignmentFlag.AlignTop)

        # Add send button
        self.sendButton = QPushButton()
        self.sendButton.clicked.connect(self.sendButtonClicked)
        self.sendButton.released.connect(self.sendButtonReleased)
        self.sendButton.setIcon(
            qta.icon('fa5.paper-plane', color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR']))
        self.sendButton.setFixedSize(40, 45)
        self.sendButton.setStyleSheet(style_sendButton)
        self.frameLayout.addWidget(
            self.sendButton, 0, 1, Qt.AlignmentFlag.AlignTop)

        # Add timer text field
        self.timerTextField = QLineEdit()
        self.timerTextField.setText("20")
        self.timerTextField.setFixedSize(80, 45)
        self.timerTextField.setStyleSheet(style_timerTextField)

        self.frameLayout.addWidget(
            self.timerTextField, 0, 2, Qt.AlignmentFlag.AlignTop)

        # Add button to send message on a timer
        self.sendPeriodicButton = QPushButton()
        self.sendPeriodicButton.setIcon(
            qta.icon('fa5.hourglass',
                     color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'])
        )
        self.sendPeriodicButton.setCheckable(True)
        self.sendPeriodicButton.setFixedSize(40, 45)
        self.sendPeriodicButton.setStyleSheet(style_sendPeriodicButtonInactive)
        self.sendPeriodicButton.clicked.connect(self.sendPeriodicButtonClicked)
        self.frameLayout.addWidget(
            self.sendPeriodicButton, 0, 3, Qt.AlignmentFlag.AlignTop)

        # Add result text field to a scrollable area
        self.resultScrollArea = QScrollArea()
        self.resultScrollArea.setWidgetResizable(True)
        self.resultScrollArea.setMaximumHeight(200)
        self.resultScrollArea.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        self.resultScrollArea.setStyleSheet(style_scrollAreaInactive)

        self.resultTextField = QLabel()
        self.resultTextField.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.resultTextField.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.resultTextField.setStyleSheet(style_resultTextField)

        self.resultScrollArea.setWidget(self.resultTextField)
        self.frameLayout.addWidget(self.resultScrollArea, 0, 4)
        self.frameLayout.setColumnStretch(4, 3)

    def _setResultTextField(self, data):
        self.resultScrollArea.setStyleSheet(style_scrollAreaValid)

        if data[0] == CANOPEN_READ_1_BYTE:
            self.resultTextField.setText(str(data[4]))
        elif data[0] == CANOPEN_READ_2_BYTE:
            self.resultTextField.setText(str(unpackU16LittleEndian(4, data)))
        elif data[0] == CANOPEN_READ_4_BYTE:
            self.resultTextField.setText(str(unpackU32LittleEndian(4, data)))
        else:
            self.resultScrollArea.setStyleSheet(style_scrollAreaInvalid)
            self.resultTextField.setText("Read request aborted")

    def sendButtonClicked(self):
        """
        Send button clicked.
        """
        if not self.sendPeriodicButton.isChecked():
            # Only send messages if periodic is unchecked
            self.canServer.sendMessage(
                CMR_TO_ICH_SDO, CANOPEN_READ, 0x20f0, 0x01, 0x54)
            self.expectingResponse = True

    def sendButtonReleased(self):
        """
        Send button lost focus.
        """
        self.sendButton.clearFocus()

    def sendPeriodicButtonClicked(self):
        if self.sendPeriodicButton.isChecked():
            # Start animating timer icon
            self.sendPeriodicButton.setIcon(
                qta.icon('fa5.hourglass',
                         color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'], animation=qta.Spin(self.sendPeriodicButton))
            )

            # Disable text field
            self.timerTextField.setReadOnly(True)
        else:
            self.sendPeriodicButton.setIcon(
                qta.icon('fa5.hourglass',
                         color=COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'])
            )
            # Disable text field
            self.timerTextField.setReadOnly(False)

    def removeButtonClicked(self):
        """
        Remove button clicked. Delete self.
        """
        parentWidget = self.parentWidget()

        # Delete self
        self.listener.stop()
        parentWidget.layout.removeWidget(self)
        self.deleteLater()

    def removeButtonReleased(self):
        """
        Remove button lost focus.
        """

        self.removeButton.clearFocus()

    def preUpdate(self):
        """
        preUpdate function to receive messages
        """

        if self.expectingResponse:
            # print(self.listener.get_message())
            self._setResultTextField(self.listener.get_message().data)

        self.expectingResponse = False

    def postUpdate(self):
        """
        postUpdate function to send messages
        """

        # Check if periodic send is active, if so send message
        if self.sendPeriodicButton.isChecked():
            self.canServer.sendMessage(
                CMR_TO_ICH_SDO, CANOPEN_READ, 0x20f0, 0x02, 0x54)
            self.expectingResponse = True
