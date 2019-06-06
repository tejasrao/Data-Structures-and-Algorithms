class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# sorted SLL
class SLL:
    def __init__(self):
        self.head = None

    def sortedInsert(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        elif self.head.val >= val:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next and current.next.val < val:
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def printList(self):
        temp = self.head
        while temp.next:
            print(temp.val, end='->')
            temp = temp.next
        print(temp.val)
        
class MergeSLL:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    def merge(self, a, b):
        while True:
            if a is None:
                self.tail.next = b
                break
            if b is None:
                self.tail.next = a
                break
            if a.val <= b.val:
                self.tail.next = a
                a = a.next
            else:
                self.tail.next = b
                b = b.next
            self.tail = self.tail.next
        self.head = self.head.next
        return self.head

    def printList(self):
        temp = self.head
        while temp.next:
            print(temp.val, end='->')
            temp = temp.next
        print(temp.val)
            
def main():
    s1 = SLL()
    s1.sortedInsert(12)
    s1.sortedInsert(10)
    s1.sortedInsert(20)
    s1.printList()

    s2 = SLL()
    s2.sortedInsert(14)
    s2.sortedInsert(8)
    s2.sortedInsert(15) 
    s2.printList()
    
    s3 = MergeSLL()
    s3.merge(s1.head, s2.head)
    s3.printList()
    
    
if __name__ == '__main__':
    main()
