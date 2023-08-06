from gui.graphics_node import UDQGraphicsNode
from gui.node_content_widget import QUDNodeContentWidget

class Node:
    def __init__(self, scene, title="Undefined Node", colour="#ff313131", inputs=[], outputs=[]):
        self.scene = scene

        self.title = title
        self.colour = colour

        self.content = QUDNodeContentWidget()
        self.graphics_node = UDQGraphicsNode(self)

        self.scene.add_node(self)

        self.inputs = inputs
        self.outputs = outputs