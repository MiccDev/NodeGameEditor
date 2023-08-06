from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QUDNodeContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.create_ui()

    def create_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.widget_label = QLabel("Title")
        self.layout.addWidget(self.widget_label)
        self.layout.addWidget(QTextEdit('foo bar'))