from traceWindow.traceWindow import *
from customMainWindow.customMainWindow import *
from customMainWindow.customMainWindowToolBar import *
from PyQt6.QtWidgets import QApplication
from testSuite.mockNode import MockNode


def main():
    # Create the application
    app = QApplication([])

    # Setup can server
    canServer = CanServer('test', 'virtual', 500000)
    canServer.startListening()

    # Mock nodes
    MockNode(0x4a, 'test', 'virtual', 500000)
    MockNode(0x08, 'test', 'virtual', 500000)

    # Setup trace window
    traceWindow = TraceWindow(canServer)

    # Create graphics window
    graphicsWindow = GraphicsWindow()

    # Create main window
    mainWindow = CustomMainWindow(traceWindow, graphicsWindow)

    # Show the window
    mainWindow.show()

    # Run the event loop
    app.instance().exec_()


if __name__ == "__main__":
    main()
