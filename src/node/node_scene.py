from gui.graphics_scene import UDQGraphicsScene

class Scene:
    def __init__(self):
        self.nodes = []
        self.edges = []

        self.scene_width = 64000
        self.scene_height = 64000

        self.create_ui()

    def create_ui(self):
        self.graphics_scene = UDQGraphicsScene(self)
        self.graphics_scene.set_graphics_scene(self.scene_width, self.scene_height)

    def add_node(self, node):
        self.nodes.append(node)
        self.graphics_scene.addItem(node.graphics_node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_node(self, node):
        self.nodes.remove(node)

    def remove_edge(self, edge):
        self.edges.remove(edge)