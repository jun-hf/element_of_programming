def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    
    fast = slow = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None
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

def overlapping_lists(l0, l1):
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root1 and root1:
        return overlapping_no_cycle_lists(l0, l1)
    elif (root0 and not root1) or (not root0 and root1):
        return None

    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break
    
    return root1 if temp is root0 else None


