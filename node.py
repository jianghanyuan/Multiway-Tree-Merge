class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
