from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.graphics_view import UDQGraphicsView
from node.node_scene import Scene
from node.pin import Pin
from node.node import Node

class NodeGameEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stylesheet_path = "./src/styles/node-style.qss"
        self.load_stylesheet(self.stylesheet_path)
        self.create_ui()

    def create_ui(self):
        """
        Sets up all the gui realted stuff
        """

        self.setWindowTitle("Node Game Editor")
        self.setGeometry(200, 200, 1920 // 2, 1080 // 2)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = Scene()
        # self.graphics_scene = self.scene.graphics_scene

        node = Node(self.scene, "Cool Node", "#ff0000", inputs=[Pin(), Pin(), Pin()], outputs=[Pin(), Pin()])

        self.view = UDQGraphicsView(self.scene.graphics_scene, self)
        self.layout.addWidget(self.view)

        # self.debug()
        self.show()

    def debug(self):
        green_brush = QBrush(Qt.green)
        outline_pen = QPen(Qt.black)
        outline_pen.setWidth(2)
        
        rect = self.graphics_scene.addRect(-100, -100, 80, 100, outline_pen, green_brush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

    def load_stylesheet(self, filename):
        stylesheet_file = QFile(filename)
        stylesheet_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = stylesheet_file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding="utf-8"))