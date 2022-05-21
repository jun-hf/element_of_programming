
class LinkedList:
    class Node:
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = self.Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def printLinkedList(self):
        current = self.head
        while current:
            print (current.data)
            current = current.next


LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(6)
LL1.insert(8)


LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)

LL1.printLinkedList()

class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def merge(L1, L2):
    head = tail = LinkedNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail, L1 = L1, L1.next
        else:
            tail, L2 = L2, L2.next
        
        tail = tail.next
    
    tail.next = L1 or L2

    return head.next


