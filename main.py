from traceWindow.traceWindow import *
from customMainWindow.customMainWindow import *
from customMainWindow.customMainWindowToolBar import *
from cmrWindow.cmrWindow import *

from PyQt6.QtWidgets import QApplication
from testSuite.mockNode import MockNode


def main():
    # Create the application
    app = QApplication([])

    # Set font for application
    font = QFontDatabase.systemFont(QFontDatabase.GeneralFont)
    font.setFamily("Verdana")
    font.setPointSize(12)
    app.setFont(font)

    # Setup can server
    canServer = CanServer()

    # Mock ICH in debug mode
    if DEBUG:
        ich = MockNode(0x0E)
        ich.start()

    # Setup trace window
    traceWindow = TraceWindow(canServer)

    # Create graphics window
    graphicsWindow = GraphicsWindow(canServer)

    # Create CMR window
    cmrWindow = CmrWindow(canServer)

    # Create main window
    mainWindow = CustomMainWindow(traceWindow, graphicsWindow, cmrWindow)

    # Show the window
    mainWindow.show()

    # Run the event loop
    app.instance().exec_()


if __name__ == "__main__":
    main()
