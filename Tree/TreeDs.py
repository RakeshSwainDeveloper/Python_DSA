class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return  self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node


    def leetcode_insert(self,val):
        if self.root is None:
            self.root = Node(val)
            return
        root_node = self.root
        while 1:
            if val < root_node.data:
                if root_node.left is not None:
                    root_node = root_node.left
                else:
                    root_node.left = Node(val)
                    break
            elif val > root_node.data:
                if root_node.right is not None:
                    root_node = root_node.right
                else:
                    root_node.right = Node(val)
                    break

    def traverse_Inorder(self,node):
        if node is not None:
            self.traverse_Inorder(node.left)
            print(node.data , end=' -> ')
            self.traverse_Inorder(node.right)

    def traverse_Preorder(self,node):
        if node is not None:
            print(node.data,end=' ')
            self.traverse_Preorder(node.left)
            self.traverse_Preorder(node.right)
    def traverse_postorder(self,node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data,end=' ')

    def mirrorOfBinaryTree(self,node):
        if node is not None:
            self.mirrorOfBinaryTree(node.left)
            self.mirrorOfBinaryTree(node.right)
            node.left,node.right = node.right,node.left

    def areMirror(self,root1,root2):
        if root1 is None and root2 is None:
            return 1
        if root1 is None or root2 is None:
            return 0
        if root1.data is not root2.data:
            return 0
        else:
            return self.areMirror(root1.left,root2.right) and (root1.right,root2.left)




# tree = Tree()
# root = tree.createNode(5)
# print(root.data)
# tree.insert(root,2)
# tree.insert(root,10)
# tree.insert(root,7)
# tree.insert(root,15)
# tree.insert(root,12)
# tree.insert(root,20)
# tree.insert(root,30)
# tree.insert(root,6)
# tree.insert(root,8)
#
# print('\nInoder traverse--------------')
# tree.traverse_Inorder(root)
# print('\nPreOrder traverse-----------------')
# tree.traverse_Preorder(root)
# print('\npostorder traverse------------')
# tree.traverse_postorder(root)

# inoreder -> Left - root - right
# preOrder -> root - left - right
# postOrder -> left - right - root
