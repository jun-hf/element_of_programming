from dataclasses import dataclass


"""

kth last element:

k = 2
          |
1 -> 2 -> 4 -> 6 -> 9 -> 18


"""
class LinkNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def remove_kth_element(L, k):
    dummy_head = LinkNode(0, L)

    first_node = dummy_head.next

    for _ in range(k):
        first_node = first_node.next
    
    second_node = dummy_head

    while first_node:
        first_node, second_node = first_node.next, second_node
    
    second_node.next = second_node.next.next

    return dummy_head.next


