'''BFS And DFS are common graph search algorithms. DFS are mainly used when wanting to search to entire
graph, while BFS is used when wanting to find the shortest path. DFS is implemented with recursion. 
BFS is implemented by using a queue and not recursively'''

class Graph:
    def __init__(self):
        self.nodes = None

class Node:
    def __init__(self, value, adjacent):
        self.value = value
        self.adjacent = adjacent
        self.visited = False

def dfs(node):
    if not node:
        return
    node.visited = True
    print(node.value)
    for node in node.adjacent:
        if node.visited == False:
            dfs(node)

def bfs(node):
    queue = []
    node.visited = True
    queue.append(node)
    while queue:
        dequeued_node = queue.pop(0)
        print(dequeued_node.value)
        for node in dequeued_node.adjacent:
            if not node.visited:
                node.visited = True
                queue.append(node)
        
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

bfs(a)