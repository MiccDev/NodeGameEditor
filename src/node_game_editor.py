from PyQt5.QtWidgets import *

from graphics_scene import UDQGraphicsScene

class NodeGameEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        self.graphics_scene = UDQGraphicsScene()

        self.view = QGraphicsView(self)
        self.view.setScene(self.graphics_scene)
        self.layout.addWidget(self.view)

        self.show()