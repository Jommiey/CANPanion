from constants.constants import *

style_tabs = """
QTabWidget::pane {
    border: 0;
    margin: -10px;
}

QTabBar::tab {
    background-color: %s;
    color: white;
}

QTabBar::tab:selected {
    background-color: %s;
}
""" % (
    COLORS[COLOR_SCHEME]['BORDER_COLOR'],
    COLORS[COLOR_SCHEME]['BACKGROUND_COLOR']
)
