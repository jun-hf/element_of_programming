class LinkedNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

l11 = LinkedNode(11, None)
l11_1 = LinkedNode(11, l11)
l7 = LinkedNode(7, l11_1)
l5 = LinkedNode(5, l7)
l3 = LinkedNode(3, l5)
l2 = LinkedNode(2, l3)
l2_1 = LinkedNode(2, l2)

def print_all(l):
    pointer = l
    while pointer:
        print(pointer.data)
        pointer = pointer.next

print_all(l2_1)

"""
2 - 2 - 3 - 5 - 7 - 11 - 11

for this solutions, I just need to 

go throuhgt the linked list, 
and have a variable to store the current data

dummy_head = LinkedNode(0, l)
pointer = l
data = l.data
new_list = l

while pointer:
    if data != pointer.data:
        new_list.next will = pointer
        data = pointer's data
    update pointer
    pointer = poiunter.next

return

"""

def remove_dup(l):
    dummy_head = LinkedNode(0, l)
    pointer = dummy_head.next
    data = pointer.data
    new_list = dummy_head.next

    while pointer:
        if data != pointer.data:
            new_list.next = pointer
            data = pointer.data
        pointer = pointer.next
    
    return dummy_head.next

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

remove_dup(l2_1)
print_all(l2_1)



        

