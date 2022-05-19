"""

"""


def overlapping_no_cycle_lists(l0, l1):
    def length(L):
        lenght = 0
        while L:
            lenght += 1
            L= L.next
        return lenght
    
    l0_len, l1_len = length(l0), length(l1)

    if l0_len > l1_len:
        l0, l1 = l1, l0
    
    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next
    
    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    
    return l0