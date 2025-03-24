import QueueExe
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    # Set data
    def setData(self,data):
        self.data = data
    # get Data
    def getData(self):
        return self.data
    # get Left node
    def getLeftNode(self):
        return self.left
    # get right node
    def getRightNode(self):
        return self.right


def preOrderRecursive(root, result):
    if not root:
        return
    result.append(root.data)
    preOrderRecursive(root.getLeft(),result)
    preOrderRecursive(root.getRight(),result)

def inOrderIterative(root, result):
    if not root:
        return
    stack = []
    node = root
    while stack or root:
        if node:
            stack.append(node)
            node = node.getRight()
        else:
            node = stack.pop()
            result.append(node.getData())
            node = node.getRight()

def postRecursive(root,result):
    if not root:
        return
    postRecursive(root.getLeft(),result)
    postRecursive(root.getLeft(),result)
    result.append(root.getData())

def sizeOfRecursiveArray(root):
    if not root:
        return 0
    return  sizeOfRecursiveArray(root.getLeft())+sizeOfRecursiveArray(root.getRight())+1

def NumerOfLevelsInBtUsingLevelOrder(root):
    if root is None:
        return 0
    q = QueueExe()
    q.enQueur(root)
    node = None
    count = 0
    while not q.isEmpty():
        node = q.deQueue()
        if node.left is None and node.right is None:
            count+=1
        else:
            if node.left is not None:
                q.enQueur(node.left)
            if node.right is not None:
                q.enQueur(node.right)
    return count
def numberOfHalfNodesInBtUsingLevelOrder(root):
    if root is None:
        return 0
    q = QueueExe()
    q.enQueur(root)
    node = None
    count = 0
    while not q.isEmpty():
        node = q.deQueue()
        if (node.left is None and node.right is not None) or (node.left is  not None and node.right is None):
            count += 1
        else:
            if node.left is not None:
                q.enQueur(node.left)
            if node.right is not None:
                q.enQueur(node.right)
    return count

def zigzagTraversal(root):
    result = []
    currentLevel = []
    if root is not  None:
        currentLevel.append(root)
    leftToRight = True
    while len(currentLevel) > 0:
        levelResult = []
        nextLevel = []
        while len(currentLevel) > 0:
            node = currentLevel.pop()
            levelResult.append(node)


# def areStructurallySame(root1,root2):
#     if (not root1.left )

class GenericTreeNode:
    def __init__(self,data = None,next = None):
        self.data = data
        self.firstChild = None
        self.nextSibinling = None


class GenericTree:
    def __init__(self,parent,value = None):
        self.parent = parent
        self.value = value
        self.childList = []
        if parent is None:
            self.birthOrder = 0
        else:
            self.birthOrder = len(self.childList)
            