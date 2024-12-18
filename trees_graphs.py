#Binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)
root=Node(1)
one=Node(2)
two=Node(3)
three=Node(4)
four=Node(5)
root.left=one
root.right=two
root.left.left=three
root.left.right=four
print(pre_order(root))
print(in_order(root))
print(post_order(root))
'-------------------------------------------------------------------------------------------'
#Binary search tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(r, key):
    if r is None:
        return Node(key) 
    elif r.data < key:
        r.right = insert(r.right, key)
    else:
        r.left = insert(r.left, key)
    return r
def in_order(r):
    if r:
        print(r.data)
        in_order(r.left)
        in_order(r.right)
def search(r,key):
    if r is None or r.data == key:
        return node
    elif r.data < key:
        return insert(r.right,key)
    else:
        return insert(r.left,key)
    
r=Node(10)
r=insert(r,14)
r=insert(r,30)
r=insert(r,1)
r=insert(r,6)
r=insert(r,55)
r=insert(r,4)
r=insert(r,20)
r=insert(r,10)
print(in_order(r))
print("found" if search(r,55) else "not found")
'-----------------------------------------------------------------------------------------------'
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
'------------------------------------------------------------------------------------------------'