"""
Given a linked list and the start and end position of a part of the linked list, reverse the part of the two position. The 
first node is consider 1.

1 -> 4 -> 8 -> 9

(2, 3)

1 -> 8 -> 4 -> 9

"""
class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def reverse_sublist(l, start, end):

    dummy_head = sublist_head = ListNode(0, l)

    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    for _ in range(end - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next
