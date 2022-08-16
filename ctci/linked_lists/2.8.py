from template import List_node
from template import print_linked_list
from template import generate_linked_list

def detect_loop(list1):
    slow = fast = list1
    while slow.next and fast.next.next:
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
    

x = List_node(1,List_node(2,List_node(3,List_node(4))))
x.next.next.next.next = x.next

print(detect_loop(x))
#print_linked_list(x)

