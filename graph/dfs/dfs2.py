vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graph = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    stack = [start]
    neighborsList = [[] for vertex in vertexList]

    for edge in edgeList:
        neighborsList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in neighborsList[current]:
            if not neighbor in visitedList:
                stack.append(neighbor)                
        visitedList.append(current)
    #print(neigborsList)
    return visitedList

print(dfs(graph, 0))