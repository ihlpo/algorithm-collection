class Graph:
    def __init__(self):
        self.nodes = None

class Node:
    def __init__(self, value, adjacent):
        self.value = value
        self.adjacent = adjacent
        self.visited = False


def route_exists(start, end):
    queue = []
    queue.append(start)
    while queue:
        dequeue_node = queue.pop(0)
        if dequeue_node is end:
            return True
        dequeue_node.visited = True
        for node in dequeue_node.adjacent:
            if node.visited == False:
                queue.append(node)
    return False


def route_exists_dfs(start, end):
    def dfs(node, end):
        if node is end:
            return True
        node.visited = True
        for node in node.adjacent:
            if node.visited == False:
                if dfs(node, end):
                    return True
    if not start or not end:
        return False
    return True if dfs(start, end) else False

x = Graph()
a = Node(0,[])
b = Node(1, [])
c = Node(2,[])
d = Node(3, [])
e = Node(4,[])
f = Node(5,[]) 

a.adjacent = [b,e,f]
b.adjacent = [d,e]
c.adjacent = [b]
d.adjacent = [c,e]
e.adjacent = []
f.adjacent = []

print(route_exists_dfs(a, e))
