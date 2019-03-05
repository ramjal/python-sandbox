
class Vertix:
    def __init__(self, name):
        self.discovered = False
        self.name = name
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    def __init__(self, vertices, edgeList):
        self.vertices = {}
        for n in vertices:
            vertix = Vertix(n) #name            
            for edge in edgeList:
                if edge[0] == vertix.name:
                    vertix.add_neighbor(edge[1])
            self.vertices[n] = vertix

    def print_graph(self):
        for vertix in self.vertices.values():
            print(vertix.name, '->', vertix.neighbors)
    
    def reset(self):
        for vertix in self.vertices.values():
            vertix.discovered = False


    def dfsRecursive(self, name):
        vertex = self.vertices[name]
        if not vertex.discovered:
            vertex.discovered = True
            print(vertex.name)       
            for vName in vertex.neighbors:
                self.dfsRecursive(vName)

    def dfsStack(self, name):
        stack = []
        vertex = self.vertices[name]
        stack.append(vertex)
        while stack:
            vertex = stack.pop()
            if not vertex.discovered:
                vertex.discovered = True
                print(vertex.name)
                for vName in vertex.neighbors:
                    stack.append(self.vertices[vName])


vertices = [0, 1, 2, 3, 4, 5, 6]
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
g = Graph(vertices, edgeList)
g.print_graph()

print("--------- Recursive -----------")
g.dfsRecursive(0)

g.reset()
print("--------- Stack -----------")
g.dfsStack(0)


