from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from canServer.canServer import *
from traceWindow.traceWindowToolBar import *
from traceWindow.traceWindowTable import *
from traceWindow.traceWindowFilter import *
from traceWindow.traceWindowSplitter import *
import time


class TraceWindow(QWidget):
    """
    Container for the trace window
    """

    def __init__(self, canServer):
        super().__init__()

        # Setup variables
        self.traceActive = False
        self.traceStartTime = time.time()

        # Setup toolbar
        self.toolbar = TraceWindowToolBar()

        # Setup spitter view
        self.splitterView = TraceWindowSplitter(Qt.Horizontal)

        # Setup filter view
        self.filterView = TraceWindowFilter()
        self.splitterView.addWidget(self.filterView)

        # setup trace table view
        self.traceTable = TraceWindowTable()
        self.splitterView.addWidget(self.traceTable)

        # Setup grid layout
        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)

        self.layout.addWidget(self.toolbar, 0, 0, 1, 2)
        self.layout.addWidget(self.splitterView, 1, 0, 1, 2)

        self.layout.setRowStretch(1, 4)
        self.layout.setColumnStretch(1, 4)
        self.layout.setColumnStretch(0, 1)

        self.setLayout(self.layout)

        canServer.canMessageReceived.connect(self.addToTraceList)
        self.toolbar.pauseButtonPressed.connect(self.pauseTrace)

    def pauseTrace(self, paused):
        self.traceTable.setPaused(paused)

    def addToTraceList(self, canMessage):
        if (self.traceActive):
            # Add item to list
            self.traceTable.appendRow(
                time.time() - self.traceStartTime, canMessage.arbitration_id, canMessage.data)

    def setTraceActive(self, status):
        if status:
            # Store start time and clear old entries of the table
            self.traceStartTime = time.time()
            self.pauseTrace(False)
            self.traceTable.resetTable()
            self.toolbar.pauseButton.setDisabled(False)
        else:
            # Disable toolbar pausebutton
            self.pauseTrace(True)
            self.toolbar.pauseButton.setDisabled(True)

        self.toolbar.pauseButton.setChecked(not status)
        self.traceActive = status
