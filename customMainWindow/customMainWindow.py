from graphicsWindow.graphicsWindow import *
from graphicsWindow.signalPlot import *
from canServer.canServer import *
from customMainWindow.customMainWindowToolBar import *
from constants.constants import *

from PyQt6.QtWidgets import QMainWindow, QTabWidget


class CustomMainWindow(QMainWindow):
    def __init__(self, traceWindow, graphicsWindow, cmrWindow):
        super().__init__()

        # Customize main window
        self.setWindowTitle("CANPanion")
        self.setMinimumWidth(1280)
        self.setStyleSheet(
            "background-color: " +
            COLORS[COLOR_SCHEME]["BACKGROUND_COLOR"] + ";" +
            "color: " + COLORS[COLOR_SCHEME]["TEXT_COLOR"] + ";"
        )

        # Add toolbar
        self.toolBar = ToolBar()
        self.addToolBar(self.toolBar)
        self.toolBar.traceActiveStatus.connect(traceWindow.setTraceActive)

        # Create tab widget to hold other windows/layouts
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)
        tabs.setStyleSheet("""
                           QTabWidget::pane {
                            border: 0;
                            margin: -10px;
                           }
                           QTabBar::tab {
                           background: #353e4d;
                           color: white;
                           }
                           QTabBar::tab:selected {
                           background: #222831;
                           }
                           """)

        # Create CMR window
        tabs.addTab(cmrWindow, "CMR")

        # Create the graphics window
        tabs.addTab(graphicsWindow, "Graphics")

        # Create the trace window
        # tabs.addTab(traceWindow, "Trace")

        self.setCentralWidget(tabs)
