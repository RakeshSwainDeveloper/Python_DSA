class DynamicTree:
    class Node:
        def __init__(self,data):
            self.data = data
            self.children = []
            self.parent = None
        def  add_child(self,child):
            child.parent = self
            self.children.append(child)
        def __str__(self):
            return self.data
    def __init__(self):
        self.root = None
    def find_node(self,node,data):
        if node is None:
            return None
        if node.data == data:
            return node
        for child in node.children:
            found = self.find_node(child,data)
            if found:
                return found
        return None
    def add_node(self,parent_data=None,child_data = None):
        pass