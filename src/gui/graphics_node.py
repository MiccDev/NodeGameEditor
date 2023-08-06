from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UDQGraphicsNode(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.content = self.node.content

        self.title_color = Qt.white
        self.title_font = QFont("Ubuntu", 10)

        self.width = 180
        self.height = 240
        self.edge_size = 10
        self.title_height = 24
        self.padding = 5.0

        self.title_brush = QBrush(QColor(self.node.colour))
        self.background_brush = QBrush(QColor("#e3212121"))

        self.pen = QPen(QColor("#7f000000"))
        self.pen_selected = QPen(QColor("#ffffa637"))

        self.create_title()
        self.title = self.node.title

        self.create_sockets()

        self.create_content()

        self.create_ui()

    def create_title(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self.title_color)
        self.title_item.setFont(self.title_font)
        self.title_item.setPos(self.padding, 0)
        self.title_item.setTextWidth(
            self.width -
            2 * self.padding
        )

    def create_content(self):
        self.graphics_content = QGraphicsProxyWidget(self)
        self.content.setGeometry(self.edge_size, self.title_height + self.edge_size, self.width - 2 * self.edge_size, self.height - 2 * self.edge_size - self.title_height)
        self.graphics_content.setWidget(self.content)

    def create_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self) -> QRectF:
        return QRectF(
            0, 0,
            2 * self.edge_size + self.width,
            2 * self.edge_size + self.height
        ).normalized()

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget=None) -> None:
        # Title

        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.title_height, self.edge_size, self.edge_size)
        path_title.addRect(0, self.title_height - self.edge_size, self.edge_size, self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size, self.edge_size)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.title_brush)
        painter.drawPath(path_title.simplified())

        # Content

        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(0, self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.title_height, self.edge_size, self.edge_size)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.background_brush)
        painter.drawPath(path_content.simplified())

        # Outline

        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)

        painter.setPen(self.pen if not self.isSelected() else self.pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    @property
    def title(self): return self.text_title
    @title.setter
    def title(self, value):
        self.text_title = value
        self.title_item.setPlainText(self.text_title)
