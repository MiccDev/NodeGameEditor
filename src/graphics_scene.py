from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
Create a user-defined (UD) QGraphicsScene
rather than overriding it.
"""
class UDQGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.background_colour = QColor("#393939")
        self.foreground_colour = QColor("#2f2f2f")

        self.pen = QPen(self.foreground_colour)
        self.pen.setWidth(1)

        self.scene_width = 64000
        self.scene_height = 64000
        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)

        self.setBackgroundBrush(self.background_colour)

    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:
        super().drawBackground(painter, rect)