import sys
from PyQt5.QtWidgets import *

from node_game_editor import NodeGameEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NodeGameEditor()

    sys.exit(app.exec_())