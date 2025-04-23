class MindMapLeaf:
    def __init__(self,name,shape):
        self.name = name
        self.shape = shape

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
        to_print = ("    " * indent) + str(self)
        print(to_print)

    def __str__(self):
        return self.get_shape_representation().format(self.name)


