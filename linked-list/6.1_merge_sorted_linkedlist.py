class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def add_next_node(self, inter):
        self.next = ListNode(inter)
    
    def get_next_node(self):
        return self.next
    


L1 = ListNode(2)



dummy_head = tail = ListNode()

print(dummy_head.data)
print(tail.data)

print(L1.get_next_node())