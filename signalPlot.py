import pyqtgraph as pg
from PyQt6.QtWidgets import QVBoxLayout, QWidget
import numpy as np
import random


class SignalPlot(QWidget):
    def __init__(self, background):
        super().__init__()

        self.x = list(range(10))
        self.y = [random.randint(1, 20) for _ in range(10)]
        self.background = background

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.plotWidget = pg.PlotWidget(background=self.background)
        self.plotWidget.showGrid(x=True, y=True)
        self.plotWidget.setXRange(0, 20, padding=0)
        self.plotWidget.setYRange(0, 20, padding=0)

        self.plots = {}

        self.layout.addWidget(self.plotWidget)

    def startPlotting(self, frequency):
        timer = pg.QtCore.QTimer(self)
        timer.timeout.connect(self.updatePlots)
        timer.start(frequency)

    def updatePlots(self):
        for plot in self.plots:
            if self.plots[plot]:
                self.x.append(self.x[-1] + 1)
                self.y.append(random.randint(1, 20))
                self.plots[plot].setData(self.x, self.y)

                # Handle scrolling
                currentRange = self.plotWidget.viewRange()[0]
                if currentRange[1] >= self.x[-1]:
                    continue
                scrollRange = (
                    currentRange[0] + (self.x[1] - self.x[0]), currentRange[1] + (self.x[1] - self.x[0]))
                self.plotWidget.setXRange(
                    *scrollRange, padding=0)

    def addPlot(self, plotName, plotLineColor):
        self.plots[plotName] = self.plotWidget.plot(self.x, self.y, pen=pg.mkPen(color=plotLineColor,
                                                                                 width=2))
