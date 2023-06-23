#Kosaraju's algorithms
#do not print the graph, its 5 million lines in a .txt so...
from collections import defaultdict

#normal and reversed graph
graph = defaultdict(list)
grev = defaultdict(list)


#reading the file
with open('test.txt', "r") as f:
    data = f.readlines()
    for row in data:
        row = row.strip()
        row = row.split()
        row = [int(x) for x in row]

        vertex_outs = row[1:]
        graph[row[0]] = vertex_outs + graph.get(row[0], [])


#O(m + n) 
def reverse_graph(g, grev):
    for k in graph:
        for v in g[k]:
            grev[v].append(k)


def first_dfs(G, s, visited, stack):
    visited[s] = True

    for v in G[s]:
        if visited[v] is True:
            stack.append(v)
            return
        
        else:
            first_dfs(G, v, visited, stack)

    stack.append(s)


#main code

#reversing the graph (grev is the reversed graph)
reverse_graph(graph, grev)

#intial variables
vertices = list(graph.keys())
visited = [False] * (len(vertices) + 1)
stack = []

for i in range(1, len(vertices) + 1):
    if not visited[i]:
        first_dfs(graph, i, visited, stack)

print(stack)