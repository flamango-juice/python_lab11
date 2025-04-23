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

    def get_str(self, indent = 0):
        result = ""
        if indent == 0:
            result += "mindmap" + "  root"
            result += " " * indent + str(self) + os.linesep
            indent += 2
        else:
            result += " " * indent + str(self) + os.linesep

        for child in self.children:
            result += child.get_str(indent + 2)

        return result

    def display(self, indent=0):
        if indent == 0:
            print("mindmap" + os.linesep + "  root",end="")
        to_print = ("    " * indent) + str(self)
        print(to_print)
        for child in self.children:
            child.display(indent + 2)

    def __str__(self):
        return self.get_shape_representation().format(self.name)

def main():
    from mindmap_leaf import MindMapLeaf
    root = MindMapComposite("The Battle at Wolf 359", "circle")

    characters = MindMapComposite("Characters", "oval")
    characters.add(MindMapLeaf("Jean-Luc Picard / Locutus", "plain"))
    characters.add(MindMapLeaf("William Riker", "plain"))
    characters.add(MindMapLeaf("Data", "plain"))
    characters.add(MindMapLeaf("Worf", "plain"))
    characters.add(MindMapLeaf("Borg Queen (implied presence)", "plain"))
    root.add(characters)
    to_p = root.get_str()
    root.display()
    print(to_p)


if __name__ == "__main__":
    main()