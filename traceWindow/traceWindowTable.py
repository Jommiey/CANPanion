from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import binascii


class TraceWindowTable(QTableView):
    def __init__(self):
        super().__init__()

        self.headers = ['time', 'sender', 'data']
        self.active = True

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.setupModel()
        self.setupTable()
        self.setupHeader()

    def appendRow(self, time, sender, data):
        """
        Append a row to the table
        """
        rowItems = []
        self.rowItemsPaused = []

        rowItems.append(self.createItem("{:.5f}".format(time), "Roboto Mono"))
        rowItems.append(self.createItem(hex(sender)[2:], "Roboto Mono"))
        rowItems.append(self.createItem(binascii.hexlify(
            data, sep=' ', bytes_per_sep=1).decode('utf-8'), "Roboto Mono"))

        # Append rows
        self.model.appendRow(rowItems)
        self.scrollToBottom()

    def createItem(self, string, font):
        """
        Function to create an item to append to a row
        """
        item = QStandardItem(string)

        font = QFont(font)
        font.setPointSize(12)

        item.setFont(font)
        return item

    def setupTable(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setShowGrid(False)
        self.setEditTriggers(QTableView.NoEditTriggers)

        # Setup vertical header
        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(5)

    def resetTable(self):
        self.model.removeRows(0, self.model.rowCount())

    def setupModel(self):
        # Setup the model to handle pausing of trace
        self.pausedModel = QStandardItemModel()

        # Setup the active model
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.headers)

    def setupHeader(self):
        self.horizontalHeaderView = HeaderView(
            Qt.Horizontal, self.headers, self)
        self.setHorizontalHeader(self.horizontalHeaderView)


class HeaderView(QHeaderView):
    def __init__(self, orientation, headers, table):
        super().__init__(orientation)

        # Setup menu for header
        self.headerMenu = HeaderMenu(headers, table)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.headerMenu.showMenu)

        # Setup behaviour for sections
        self.setStretchLastSection(True)
        self.setSectionsMovable(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QHeaderView.InternalMove)

        # Style header
        self.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet(
            """
            ::section {
                background-color: #353e4d;
                color: #f2f2f2;
                font-weight: bold;
            }
            """
        )


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
