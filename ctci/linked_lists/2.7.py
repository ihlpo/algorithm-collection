from template import List_node
from template import print_linked_list
from template import generate_linked_list

def intersection(list1, list2):
    '''To check whether the given linked lists have an interect, we can first check if they have to same last node.
    If they do, we can go back from the beginning and traverse until we find the first same node. we will need to
    account for when the lists have different lengths. we can do this be having counters during the first traversal
    then we can move the pointer of the larger list forward by the difference of length
    O(n+m) time to traverse both list. O(1) space as we as we are only using pointers'''

    head1 = list1
    head2 = list2
    count1 = 1
    count2 = 1
    while head1 and head1.next:
        head1 = head1.next
        count1 += 1

    while head2 and head2.next:
        head2 = head2.next
        count2 += 1

    if head1 is head2:
        head1 = list1
        head2 = list2
        difference = abs(count1 - count2)
        if count1 > count2:
            for i in range(difference):
                head1 = head1.next
        elif count2 > count1:
            for i in range(difference):
                head2 = head2.next
        
        while head1 and head2:
            if head1 is head2:
                return head1.data
            head1 = head1.next
            head2 = head2.next
                
    return False



x = List_node(1,List_node(2,List_node(3,List_node(4))))
y = List_node(9, List_node(8, x.next))


print_linked_list(x)
print_linked_list(y)
print(intersection(x, y))
