
vertices = [0, 1, 2, 3, 4, 5, 6]
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]


neighborList = [[] for v in vertices]
for edge in edgeList:
    neighborList[edge[0]].append(edge[1])

visited = []
stack = [0]
while stack:
    vertex = stack.pop()   
    for neighbor in neighborList[vertex]:
        if neighbor not in visited:
            stack.append(neighbor)
    visited.append(vertex)

print(visited)