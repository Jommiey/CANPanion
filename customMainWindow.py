from traceWindow import *
from graphicsWindow import *
from signalPlot import *
from canServer import *
from toolbar import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTabWidget
import configparser


class CustomMainWindow(QMainWindow):
    def __init__(self, traceWindow, graphicsWindow):
        super().__init__()

        # Read config
        configParser = configparser.ConfigParser()
        configParser.read('./colorscheme.ini')

        # Customize main window
        self.setWindowTitle("CANPanion")
        self.setMinimumSize(1920, 1080)
        self.setStyleSheet("background-color: #DDDDDD;")

        # Add toolbar
        self.toolBar = ToolBar()
        self.addToolBar(self.toolBar)
        self.toolBar.traceActiveStatus.connect(traceWindow.setTraceActive)

        # Create tab widget to hold other windows/layouts
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)
        tabs.setStyleSheet("QTabBar::tab {"
                           "background: #353e4d;"
                           "color: white;"
                           "}"
                           "QTabBar::tab:selected {"
                           "background: #222831;"
                           "}")

        # Create the trace window
        tabs.addTab(traceWindow, "Trace")

        # Create the graphics window
        tabs.addTab(graphicsWindow, "Graphics")

        self.setCentralWidget(tabs)
