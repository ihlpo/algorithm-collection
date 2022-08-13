from template import List_node
from template import print_linked_list
from template import generate_linked_list

def delete_node(node):
    '''O(1) time, O(1) space'''

    node.data = node.next.data
    node.next = node.next.next
