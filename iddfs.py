from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):

        if src == target: return True
        if maxDepth <= 0: return False
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    def IDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

n = int(input("Number of edges: "))
idfs = Graph(n)

for i in range(n):
    print("\n")
    temp=list(map(int,input().strip().split()))
    idfs.addEdge(temp[0],temp[1])

src = int(input("Enter source: "))
dest = int(input("Enter destination: "))
num_i = int(input("Max depth allowed: "))

if idfs.IDFS(src, dest, num_i) :
    print ("Target found within depth")
else :
    print ("Target not found within depth")

print("\n Used Iterative deepening search algorithm")
