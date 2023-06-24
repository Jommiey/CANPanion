from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QAbstractItemView, QMenu, QHeaderView
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

        self.setupHeaderMenu()
        self.setupModel()
        self.setupTable()
        self.setupStyle()

    def appendRow(self, time, sender, data):
        rowItems = []

        rowItems.append(QStandardItem("{:.5f}".format(time)))
        rowItems.append(QStandardItem(hex(sender)[2:]))
        rowItems.append(QStandardItem(str(sender)))
        rowItems.append(QStandardItem(
            binascii.hexlify(data, sep=' ', bytes_per_sep=1).decode('utf-8')))

        self.model.appendRow(rowItems)
        self.scrollToBottom()

    def setupStyle(self):
        # Setup header style
        self.horizontalHeader().setStyleSheet(
            """
            QHeaderView::section {
                text-align: left;
            }
            """
        )
        pass

    def setupTable(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setShowGrid(False)
        self.setEditTriggers(QTableView.NoEditTriggers)

        # Setup horizontal header
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionsMovable(True)
        self.horizontalHeader().setDragEnabled(True)
        self.horizontalHeader().setDragDropMode(QHeaderView.InternalMove)

        # Setup vertical header
        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(5)  # Can I make this smaller?

    def resetTable(self):
        self.model.removeRows(0, self.model.rowCount())

    def setupModel(self):
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.headers)

    def setupHeaderMenu(self):
        self.headerMenu = HeaderMenu(self.headers, self)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(
            self.headerMenu.showMenu)


class HeaderMenu(QMenu):
    def __init__(self, headers, table):
        super().__init__()

        self.headers = headers
        self.table = table

        for header in self.headers:
            action = QAction(header, self)
            action.setCheckable(True)
            action.setChecked(True)
            action.triggered.connect(
                lambda checked, h=header: self.toggleHeader(h, checked))
            self.addAction(action)

    def toggleHeader(self, header, checked):
        self.table.setColumnHidden(self.headers.index(header), not checked)

    def showMenu(self, position):
        self.exec_(self.table.viewport().mapToGlobal(position))
