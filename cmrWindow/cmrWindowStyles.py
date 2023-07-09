from constants.constants import *

style_sendTimerButtonInactive = """
QPushButton {
    background-color: %s;
    margin: 0px 10px 0px 0px;
    padding: 0px 5px 0px 5px;
    border: 1px solid %s;
    border-top-right-radius: 5px;
    border-top-left-radius: 0px;
    border-bottom-right-radius: 5px;
    border-bottom-left-radius: 0px;
}  

QPushButton:hover { 
    border: 2px solid %s;
}

QPushButton:pressed { 
    border: 2px solid %s; 
}
""" % (
    COLORS[COLOR_SCHEME]['GREEN'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['GREEN_HOVER'],
    COLORS[COLOR_SCHEME]['GREEN_FOCUSED']
)

style_sendTimerButtonActive = """
QPushButton {
    background-color: %s;
    margin: 0px 10px 0px 0px;
    padding: 0px 5px 0px 5px;
    border: 1px solid %s;
    border-top-right-radius: 5px;
    border-top-left-radius: 0px;
    border-bottom-right-radius: 5px;
    border-bottom-left-radius: 0px;
}  

QPushButton:hover { 
    border: 2px solid %s;
}

QPushButton:pressed { 
    border: 2px solid %s; 
}
""" % (
    COLORS[COLOR_SCHEME]['GREEN'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['GREEN_HOVER'],
    COLORS[COLOR_SCHEME]['GREEN_FOCUSED']
)

style_resultTextField = """
QLabel {
    background-color: %s;
    border: 0px solid;
    border-radius: 0px;
    padding: 5px;
}
""" % (
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR']
)

style_addRowButton = """
QPushButton {
    background-color: %s;
    color: %s;
    border: 1px solid %s;
    border-radius: 15px;
}

QPushButton:hover { 
    border: 2px solid %s;
}

QPushButton:pressed { 
    border: 2px solid %s;
}
""" % (
    COLORS[COLOR_SCHEME]['GREEN'],
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['GREEN_HOVER'],
    COLORS[COLOR_SCHEME]['GREEN_FOCUSED']
)

style_removeButton = """
QPushButton {
    background-color: %s;
    padding: -3px;
    border: 1px solid %s;
    border-top-left-radius: 5px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 0px;
}

QPushButton:hover {
    border: 2px solid %s;
}

QPushButton:focus {
    border: 2px solid %s;
}
""" % (
    COLORS[COLOR_SCHEME]['RED'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['RED_HOVER'],
    COLORS[COLOR_SCHEME]['RED_FOCUSED']
)

style_frame = """
QFrame {
    background-color: %s;
    border: 1px solid %s;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
}
""" % (
    COLORS[COLOR_SCHEME]['SECONDARY_COLOR'],
    COLORS[COLOR_SCHEME]['THIRD_COLOR']
)

style_variableNameTextField = """
QLineEdit {
    margin: 0px;
    padding: 0px 5px 0px 5px;
    border: 1px solid %s;
    border-right: 0px;
    border-top-left-radius: 5px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 0px;
}

QLineEdit:hover {
    border: 2px solid %s;
    border-right: 0px;
}

QLineEdit:focus {
    border: 2px solid %s;
    border-right: 0px;
}
""" % (
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR_FOCUSED']
)

style_sendButton = """
QPushButton {
    background-color: %s;
    margin: 0px 10px 0px 0px;
    padding: 0px 5px 0px 5px;
    border: 1px solid %s;
    border-top-left-radius: 0px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 5px;
}

QPushButton:hover {
    border: 2px solid %s;
}

QPushButton:focus {
    border: 2px solid %s;
}
""" % (
    COLORS[COLOR_SCHEME]['GREEN'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['GREEN_HOVER'],
    COLORS[COLOR_SCHEME]['GREEN_FOCUSED']
)

style_timerTextField = """
QLineEdit {
    margin: 0px;
    padding: 0px 5px 0px 5px;
    border: 1px solid %s;
    border-right: 0px;
    border-top-left-radius: 5px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 0px;
}

QLineEdit:hover {
    border: 2px solid %s;
    border-right: 0px;
}

QLineEdit:focus {
    border: 2px solid %s;
    border-right: 0px;
}
""" % (
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR_FOCUSED']
)

style_scrollAreaValid = """
QScrollArea {
    border: 2px solid %s;
    border-radius: 5px;
    padding: 1px;
}

QScrollArea:hover {
    border: 3px solid %s;
}

QScrollBar:vertical {
    width: 10px;
    background: %s;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: %s;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
    background: transparent;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    height: 0px;
    background: transparent;
}
""" % (
    COLORS[COLOR_SCHEME]['GREEN'],
    COLORS[COLOR_SCHEME]['GREEN_HOVER'],
    COLORS[COLOR_SCHEME]['THIRD_COLOR'],
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'],
)

style_scrollAreaInvalid = """
QScrollArea {
    border: 2px solid %s;
    border-radius: 5px;
    padding: 1px;
}

QScrollArea:hover {
    border: 3px solid %s;
}

QScrollBar:vertical {
    width: 10px;
    background: %s;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: %s;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
    background: transparent;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    height: 0px;
    background: transparent;
}
""" % (
    COLORS[COLOR_SCHEME]['RED'],
    COLORS[COLOR_SCHEME]['RED_HOVER'],
    COLORS[COLOR_SCHEME]['THIRD_COLOR'],
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'],
)

style_scrollAreaInactive = """
QScrollArea {
    border: 1px solid %s;
    border-radius: 5px;
    padding: 1px;
}

QScrollArea:hover {
    border: 2px solid %s;
}

QScrollBar:vertical {
    width: 10px;
    background: %s;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: %s;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
    background: transparent;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    height: 0px;
    background: transparent;
}
""" % (
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['BORDER_COLOR_HOVERED'],
    COLORS[COLOR_SCHEME]['THIRD_COLOR'],
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR'],
)

style_cmrWindowFrame = """
QFrame {
    background-color: %s;
    border: 1px solid red;
}
""" % (
    COLORS[COLOR_SCHEME]['THIRD_COLOR']
)
