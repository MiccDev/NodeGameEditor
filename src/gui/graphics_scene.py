import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
Create a user-defined (UD) QGraphicsScene
rather than overriding it.
"""
class UDQGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene

        self.grid_size = 20

        self.background_colour = QColor("#393939")
        self.foreground_colour = QColor("#2f2f2f")

        self.pen = QPen(self.foreground_colour)
        self.pen.setWidth(1)
        
        self.setBackgroundBrush(self.background_colour)

    def set_graphics_scene(self, width, height):
        self.setSceneRect(-width // 2, -height // 2, width, height)

    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        screen_left = left - (left % self.grid_size)
        screen_top = top - (top % self.grid_size)

        lines = []
        for x in range(screen_left, right, self.grid_size):
            lines.append(QLine(x, top, x, bottom))

        for y in range(screen_top, bottom, self.grid_size):
            lines.append(QLine(left, y, right, y))

        painter.setPen(self.pen)
        painter.drawLines(lines)