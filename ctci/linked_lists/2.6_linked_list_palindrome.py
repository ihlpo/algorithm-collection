from template import List_node
from template import print_linked_list
from template import generate_linked_list

def panlindrome(list1):
    '''O(n) time to traverse the list twice. O(n) space to store values in a stack'''
    def push_to_stack(head, stack):
        if not head:
            return
        stack.append(head.data)
        push_to_stack(head.next, stack)
        return stack
    

    stack = push_to_stack(x,[])
    
    while list1:
        if list1.data != stack.pop():
            return False
        list1 = list1.next
    return True

x = generate_linked_list([1,2,3,2,1])
print(panlindrome(x))
