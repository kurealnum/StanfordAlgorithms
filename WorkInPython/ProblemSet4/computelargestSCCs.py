#Kosaraju's algorithms
#do not print the graph, its 5 million lines in a .txt so...
from collections import defaultdict
graph = {}


#reading the file
with open('test.txt', "r") as f:
    data = f.readlines()
    for row in data:
        row = row.strip()
        row = row.split()
        row = [int(x) for x in row]

        vertex_outs = row[1:]
        graph[row[0]] = vertex_outs + graph.get(row[0], [])


def reverse_graph(graph, graphrev):
    #should just be O(m+n)
    for key in graph:
        for i in range(len(graph[key])):
            #the new key to put in the reversed graph
            new_key = graph[key][i]
            graphrev[new_key] = graphrev.get(new_key, []) + [key]


def dfs_traversal(graph, s, visited):
    #add the current vertex to the visited list
    visited.append(s)
    print(s, end="") 

    #go thru every vertex
    for outgoing in graph[s]:
        if outgoing not in visited:
            dfs_traversal(graph, outgoing, visited)


def fillOrder(v, visited, stack):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            fillOrder(i, visited, stack)

    stack = stack.append(v)
    

def main(graph):
    vertices = list(graph.keys())

    #mark everything as not visited (First DFS)
    visited = [False]*len(vertices)
    stack = []

    #fill the stack with finishing times
    for i in range(5):
        if visited[i] == False:
            fillOrder(i, visited, stack)

    #reverse the graph
    graphrev = {}
    reverse_graph(graph, graphrev)

    #mark everything as not visited (second DFS)
    visited = [False]*len(vertices)
    while stack:
        i = stack.pop()
        if visited[i] == False:
            dfs_traversal(graphrev, i, visited)
            print("")


main(graph)