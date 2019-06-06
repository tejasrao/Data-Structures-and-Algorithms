class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def LCA(node, a, b):
    if node is None:
        return None

    if node.value == a or node.value == b:
        return node

    leftLCA = LCA(node.left, a, b)
    rightLCA = LCA(node.right, a, b)

    if leftLCA and rightLCA:
        return node

    if leftLCA:
        return leftLCA
    else:
        return rightLCA

def check(n, a):
    if n is None:
        return False
    if n.value == a or check(n.left, a) or check(n.right, a):
        return True
    return False

def findLCA(n, a, b):
    node = LCA(n, a, b)
    if check(n, a) and check(n, b):
        return node.value
    else:
        return -1

def main():
    n = Node(12)
    n.left = Node(1)
    n.right = Node(2)
    n.left.left = Node(3)
    n.right.left = Node(4)
    n.right.right = Node(5)

    print(findLCA(n, 1, 3))

if __name__ == '__main__':
    main()
