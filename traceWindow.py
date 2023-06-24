from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QAbstractItemView, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QAction
from canServer import *
from functools import partial
import binascii
import time


class TraceWindow(QWidget):
    def __init__(self, canServer):
        super().__init__()

        self.traceActive = False
        self.traceStartTime = time.time()

        self.traceTableModel = QStandardItemModel()
        self.traceTable = TraceWindowTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.traceTable)
        self.setLayout(self.layout)

        canServer.canMessageReceived.connect(self.addToTraceList)

    def addToTraceList(self, canMessage):
        if (self.traceActive):
            # Add item to list
            self.traceTable.appendRow(
                time.time() - self.traceStartTime, canMessage.arbitration_id, canMessage.data)

    def setTraceActive(self, status):
        if status:
            # Store start time and clear old entries of the table
            self.traceStartTime = time.time()
            self.traceTable.resetTable()

        self.traceActive = status


class TraceWindowTable(QTableView):
    def __init__(self):
        super().__init__()

        self.headers = ['time', 'sender (hex)', 'sender (dec)', 'data']

        self.setupModel()
        self.setupTable()
        self.setupHeaderMenu()

    def appendRow(self, time, sender, data):
        rowItems = []

        rowItems.append(QStandardItem("{:.5f}".format(time)))
        rowItems.append(QStandardItem(hex(sender)))
        rowItems.append(QStandardItem(str(sender)))
        rowItems.append(QStandardItem(
            binascii.hexlify(data).decode('utf-8')))

        self.model.appendRow(rowItems)
        self.scrollToBottom()

    def setupTable(self):
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setShowGrid(False)
        self.setEditTriggers(QTableView.NoEditTriggers)
        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(5)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(self.showMenuHeader)

    def resetTable(self):
        self.setupModel()

    def setupModel(self):
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.headers)

    def setupHeaderMenu(self):
        self.headerMenu = QMenu(self)

        for header in self.headers:
            action = QAction(header, self)
            action.setCheckable(True)

            # Handle checked status for headers active from start
            if header in self.headers:
                action.setChecked(True)

            action.triggered.connect(partial(self.setHeader, header))
            self.headerMenu.addAction(action)

    def showMenuHeader(self, position):
        self.headerMenu.exec_(self.mapToGlobal(position))

    def setHeader(self, header):
        # Check for the case where only one header item is active. Don't allow empty header.
        if len(self.headers) == 1:
            return

        if header in self.headers:
            # Remove header from active headers
            self.headers.remove(header)
        else:
            # Add header to active headers
            self.headers.append(header)

        # Redraw headers
        self.model.setHorizontalHeaderLabels(self.headers)

    def formatTime(self, timestamp):
        return timestamp

    def formatSender(self, sender):
        return sender

    def formatReceiver(self, receiver):
        return receiver

    def formatData(self, data):
        return data
