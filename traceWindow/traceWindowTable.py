from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import binascii


class TraceWindowTable(QTableView):
    def __init__(self):
        super().__init__()

        self.headers = ['time', 'sender', 'data']
        self.paused = False

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.setupModel()
        self.setupTable()
        self.setupHeader()

    def setPaused(self, paused):
        self.paused = paused

        if paused:
            self.model.pause()
        elif not paused:
            self.model.resume()

    def appendRow(self, time, sender, data):
        """
        Append a row to the table
        """
        rowItems = []

        # Append rows to model
        rowItems.append(self.createItem("{:.5f}".format(time), "Roboto Mono"))
        rowItems.append(self.createItem(hex(sender)[2:], "Roboto Mono"))
        rowItems.append(self.createItem(binascii.hexlify(
            data, sep=' ', bytes_per_sep=1).decode('utf-8'), "Roboto Mono"))
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
        self.model.removeRows(row=0, count=self.model.rowCount())

    def setupModel(self):
        # Setup the model
        self.model = PausingStandardItemModel()
        self.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.headers)

    def setupHeader(self):
        self.horizontalHeaderView = HeaderView(
            Qt.Horizontal, self.headers, self)
        self.setHorizontalHeader(self.horizontalHeaderView)


class PausingStandardItemModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.isPaused = False
        self.loop = QEventLoop()
        self.pendingItems = []

    def pause(self):
        self.isPaused = True

    def resume(self):
        self.isPaused = False
        for items in self.pendingItems:
            self.appendRow(items)
        self.pendingItems = []
        self.loop.quit()

    def itemChanged(self, item):
        if not self.isPaused:
            super().itemChanged(item)
        else:
            self.pendingItems.append([item])
            QTimer.singleShot(0, self.loop.quit)
            if not self.loop.isRunning():
                self.loop.exec_()

    def removeRows(self, row, count):
        if not self.isPaused:
            super().removeRows(row, count)
        else:
            for i in range(row, row + count):
                self.pendingItems.append(self.takeRow(i))
            QTimer.singleShot(0, self.loop.quit)
            if not self.loop.isRunning():
                self.loop.exec_()

    def appendRow(self, items):
        if not self.isPaused:
            super().appendRow(items)
        else:
            self.pendingItems.append(items)
            QTimer.singleShot(0, self.loop.quit)
            if not self.loop.isRunning():
                self.loop.exec_()


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
