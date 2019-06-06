class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BT:
    def __init__(self):
        self.root = None

    def __setRoot(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self.__setRoot(value)
        else:
            self.__insertNode(self.root, value)

    def __insertNode(self, node, value):
        if value <= node.value:
            if node.left:
                self.__insertNode(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self.__insertNode(node.right, value)
            else:
                node.right = Node(value)
                
class BST:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.__push(root)

    def hasNext(self):
        if len(self.stack) > 0:
            return True
        return False

    def next(self):
        tmpNode = self.stack.pop()
        if tmpNode.right:
            self.__push(tmpNode.right)
        return tmpNode.value

    def __push(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
def main():
    # Binary Tree
    bt = BT()
    bt.insert(2)
    bt.insert(6)
    bt.insert(1)
    bt.insert(2)
    bt.insert(5)
    bt.insert(7)
    bst = BST(bt.root)
    while bst.hasNext():
        print(bst.next())

if __name__ == '__main__':
    main()
