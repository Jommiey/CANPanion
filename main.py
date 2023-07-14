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

    ich = MockNode(0x0F, canServer)

    # Setup trace window
    traceWindow = TraceWindow(canServer)

    # Create graphics window
    graphicsWindow = GraphicsWindow(canServer)

    # Create CMR window
    cmrWindow = CmrWindow(canServer)

    # Create main window
    mainWindow = CustomMainWindow(traceWindow, graphicsWindow, cmrWindow)

    # Start thread to handle update functions
    timer = QTimer()
    timer.timeout.connect(lambda:
                          update(traceWindow, graphicsWindow, cmrWindow, [ich]))
    timer.start(20)

    # Show the window
    mainWindow.show()

    # Run the event loop
    app.instance().exec_()


def update(traceWindow, graphicsWindow, cmrWindow, mockedNodes):
    # traceWindow.update()
    graphicsWindow.update()
    cmrWindow.update()

    for node in mockedNodes:
        node.update()


if __name__ == "__main__":
    main()
