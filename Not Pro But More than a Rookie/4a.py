class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insertNode(self.root, val)

    def __insertNode(self, node, val):
        if val <= node.val:
            if node.left:
                self.__insertNode(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.__insertNode(node.right, val)
            else:
                node.right = Node(val)

    # solution - inorder and reverse inorder (controlled)
    def findPair(self, k):
        s1, s2 = [], [] # array/stack to store nodes <- length == log(Height of tree), log(nodes, 2)
        done1, done2 = False, False # flags to indicate traversal for next iter
        val1, val2 = 0, 0 # store pair values
        cur1, cur2 = self.root, self.root # inorder and reverse inoder nodes

        while True:
            while not done1:
                if cur1:
                    s1.append(cur1)
                    cur1 = cur1.left
                else:
                    if not len(s1):
                        done1 = True
                    else:
                        cur1 = s1.pop()
                        val1 = cur1.val
                        cur1 = cur1.right
                        done1 = True

            while not done2:
                if cur2:
                    s2.append(cur2)
                    cur2 = cur2.right
                else:
                    if not len(s2):
                        done2 = True
                    else:
                        cur2 = s2.pop()
                        val2 = cur2.val
                        cur2 = cur2.left
                        done2 = True

            pairSum = val1 + val2

            if val1 != val2 and pairSum == k:
                return True
            elif pairSum > k:
                done2 = False
            elif pairSum < k:
                done1 = False

            # if no pair found
            # after completing both inorder and reverse inorder traversals
            if val1 >= val2:
                return False

        
def main():
    bst = BST()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(8)
    bst.insert(12)
    bst.insert(16)
    bst.insert(25)
    if bst.findPair(25):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
