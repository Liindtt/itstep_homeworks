class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def pre_order(self, start, trace):
        # "Root -> Left -> Right"
        if start:
            trace = trace + str(start.value) + "__"
            trace = self.pre_order(start.left, trace)
            trace = self.pre_order(start.right, trace)
        return trace

    def post_order(self, start, trace):
        # "Left -> Right -> Root"
        if start is not None:
            trace = self.post_order(start.left, trace)
            trace = self.post_order(start.right, trace)
            trace = trace + str(start.value) + "__"
        return trace

    def in_order(self, start, trace):
        # "Left -> Root -> Right"
        if start is not None:
            trace = self.in_order(start.left, trace)
            trace = trace + str(start.value) + "__"
            trace = self.in_order(start.right, trace)
        return trace

    def find_parent_by_value(self, node, value):
        if node.value == value:
            return node
        elif node.left:
            node = self.find_parent_by_value(node.left, value)
        elif node.right:
            node = self.find_parent_by_value(node.right, value)
        return node


root = Node("A")
tree = Tree(root)
tree.root.left = Node("B")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.left.left.left = Node("H")
tree.root.left.left.right = Node("I")

tree.root.right = Node("C")
tree.root.right.left = Node("F")
tree.root.right.right = Node("G")
tree.root.right.right.left = Node("J")


print("Pre-Order: ", tree.pre_order(start=tree.root, trace=""))
print("In-Order: ", tree.in_order(start=tree.root, trace=""))
print("Post-Order: ", tree.post_order(start=tree.root, trace=""))
print("Find parent: ", tree.find_parent_by_value(node=tree.root, value="F"))
