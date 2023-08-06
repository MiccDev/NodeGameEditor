from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
Create a user-defined (UD) QGraphicsView
rather than overriding it.
"""
class UDQGraphicsView(QGraphicsView):
    def __init__(self, scene: QGraphicsScene, parent=None):
        super().__init__(parent)

        self.graphics_scene = scene

        self.zoom_factor = 1.25
        self.zoom = 5
        self.zoom_step = 1
        self.zoom_range = [0, 15]

        self.moving = False
        self.move_start = [0, 0]

        self.create_ui()
        self.setScene(self.graphics_scene)

    def create_ui(self):
        self.setRenderHints(QPainter.Antialiasing | 
                            QPainter.HighQualityAntialiasing | 
                            QPainter.TextAntialiasing | 
                            QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MiddleButton:
            self.moving = True
            self.move_start = [event.x(), event.y()]
            self.setCursor(Qt.ClosedHandCursor)
        return super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MiddleButton:
            self.moving = False
            self.setCursor(Qt.ArrowCursor)
        return super().mouseReleaseEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.moving:
            mouse_x, mouse_y = event.x(), event.y()
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - (mouse_x - self.move_start[0])
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - (mouse_y - self.move_start[1])
            )

            self.move_start = [mouse_x, mouse_y]
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoom_out_factor = 1 / self.zoom_factor

        if event.angleDelta().y() > 0:
            zoom_factor = self.zoom_factor
            self.zoom += self.zoom_step
        else:
            zoom_factor = zoom_out_factor
            self.zoom -= self.zoom_step

        clamped = False
        if self.zoom < self.zoom_range[0]: self.zoom, clamped = self.zoom_range[0], True
        if self.zoom > self.zoom_range[1]: self.zoom, clamped = self.zoom_range[1], True

        if not clamped:
            self.scale(zoom_factor, zoom_factor)