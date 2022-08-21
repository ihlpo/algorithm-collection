from template import List_node
from template import print_linked_list
from template import generate_linked_list

def detect_loop(list1):
    '''Have a slow and faster pointer. when the pointers collide, they will be k steps away from
    the start of the loop. At the same time the head of the linked list will also be k steps away
    from the start of the loop. When there is a collision we can move a pointer to the head and leave
    the collided pointer in place. Then move them at the same pace. When they collide, that node will
    the start of the cycle.
    O(n) time for traversing the linked list. O(1) constant space as we are only using references.'''
    slow = fast = list1

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = list1
            while slow and fast:
                if slow is fast:
                    return slow.data
                slow = slow.next
                fast = fast.next
    return False

x = generate_linked_list([1,2,3,4,5])
print_linked_list(x)
print(detect_loop(x))


