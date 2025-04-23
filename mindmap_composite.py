import os
class MindMapComposite:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def remove(self, child):
        self.children.remove(child)

    def add(self,child):
        self.children.append(child)

    def get_shape_representation(self):
        shapes = {
            "square": "[{}]",
            "rounded square": "({})",
            "circle": "(({}))",
            "bang": ")){}((",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}" # Crazy escape to the party bracket usage
        }
        return shapes.get(self.shape,"{}")

    def display(self, indent=0):
        if indent == 0:
            print("mindmap" + os.linesep + "root",end="")
        to_print = ("    " * indent) + str(self)
        print(to_print)
        for child in self.children:
            child.display(indent + 2)

    def __str__(self):
        return self.get_shape_representation().format(self.name)