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

    # Start thread to handle preUpdate functions
    preUpdateTimer = QTimer()
    preUpdateTimer.timeout.connect(lambda:
                                   preUpdate(canServer, traceWindow, graphicsWindow, cmrWindow, [ich]))
    preUpdateTimer.start(20)

    # Offset postUpdateTimer by PRE_UPDATE_MAXIMUM_TIME
    time.sleep(PRE_UPDATE_MAXIMUM_TIME)

    # Start thread to handle postUpdate functions
    postUpdateTimer = QTimer()
    postUpdateTimer.timeout.connect(lambda:
                                    postUpdate(canServer, traceWindow, graphicsWindow, cmrWindow, [ich]))
    postUpdateTimer.start(20)

    # Show the window
    mainWindow.show()

    # Run the event loop
    app.instance().exec_()


def preUpdate(canServer, traceWindow, graphicsWindow, cmrWindow, mockedNodes):
    """
    function to call preUpdate functions for all windows. 
    """
    startTime = time.time()

    canServer.preUpdate()
    # traceWindow.preUpdate()
    # graphicsWindow.preUpdate()
    cmrWindow.preUpdate()

    for node in mockedNodes:
        # node.preUpdate()
        pass

    executionTime = time.time() - startTime
    if executionTime > PRE_UPDATE_MAXIMUM_TIME:
        print("WARNING: Execution time: {:.6f} seconds".format(
            time.time() - startTime))


def postUpdate(canServer, traceWindow, graphicsWindow, cmrWindow, mockedNodes):
    """
    function to call postUpdate functions for all windows. 
    """
    startTime = time.time()

    canServer.postUpdate()
    # traceWindow.postUpdate()
    # graphicsWindow.postUpdate()
    cmrWindow.postUpdate()

    for node in mockedNodes:
        # node.postUpdate()
        pass

    executionTime = time.time() - startTime
    if executionTime > POST_UPDATE_MAXIMUM_TIME:
        print("WARNING: Execution time: {:.6f} seconds".format(
            time.time() - startTime))


if __name__ == "__main__":
    main()
