class Tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
y = Tree_node(10, Tree_node(5), Tree_node(30))
y.left.left = Tree_node(5)
y.right.right = Tree_node(40)
y.right.right.right = Tree_node(50)
y.right.right.right.right = Tree_node(60)

def is_bst_array(tree):
    """The brute force method is first use an inorder traversal to get all the values in sorted order.
    This assume the tree DOES NOT have duplicates because when we traverse the array, we cannot be
    sure that the duplicate is a left child and not a right child.
    once the values have been collected, we traverse the values to check if n is smaller than n+1.
    O(n) time complexity as we need to traverse all nodes. O(n) space for extra values in a list."""
    def helper(tree, array):
        if not tree:
            return
        helper(tree.left, array)
        array.append(tree.value)
        helper(tree.right, array)

        return array
    values = helper(tree, [])
    for i in range(1, len(values)):
        if values[i] < values[i-1]:
            return False
    return True

def is_bst_min_max_range(tree):
    """Using thr BST relationship left child <= n < right child, we can pass in a range within our recursive
    function to check whether it satisfies the BST condition.
    O(n) time complexity as we need to traverse the entire tree. O(log n) space for the recursive stack
    for up to the depth of the tree since its a binary tree"""
    def helper(tree, mini, maxi):
        if not tree:
            return True
        #tree.value cannot be smaller or equal to mini to be a valid right child
        #tree.value cannot be larger than maxi to be a valid left child
        if tree.value <= mini or tree.value > maxi: 
            return False

        return helper(tree.left, mini, tree.value) and helper(tree.right, tree.value, maxi)
    #The initial range must be infinity on both ends

    return helper(tree,float("-inf"), float('inf'))    

print(is_bst_min_max_range(y))