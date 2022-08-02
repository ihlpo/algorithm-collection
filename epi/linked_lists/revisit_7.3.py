def is_cyclic(list):
    fast = slow = list

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            pass
        
    return None