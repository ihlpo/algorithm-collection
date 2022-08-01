class List_node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def search_list(list, key): # O(n) where n is the number of nodes.
        while list and list.data != key:
            list = list.next
        return list
    
    def insert_after(node, new_node): # O(1)
        #Insert new node after given node. a -> b to a -> c -> b
        new_node.next = node.next #First assign new node to node's original next node.
        node.next = new_node #Assign to new_node and nodes next node. 

    def delete_after(node): # O(1)
        # Delete the node after this one. Assume node is not a tail.  a -> b -> c to a -> c
        node.next = node.next.next #Assign node's next node to be original next node's next node.

def print_linked_list(list):
    list_array = []
    while list:
        list_array.append(list.data)
        list = list.next
    print(list_array)
    return None

def generate_linked_list(list):
    head = tail = List_node()

    for value in list:
        tail.next = (List_node(value))
        tail = tail.next
        
    return head
        
    