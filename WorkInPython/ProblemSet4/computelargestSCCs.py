#do not print the graph, its 5 million lines in a .txt so...
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


def dfs(graph, s):
    # s is our starting vertex
    #list of visited vertexes
    visited = set()

    #start of the recursive call
    dfs_traversal(graph,s,visited)


def dfs_traversal(graph, s, visited):
    #add the current vertex to the visited list
    print(s)
    visited.add(s)

    #go thru every vertex
    for outgoing in graph[s]:
        if outgoing not in visited:
            dfs_traversal(graph, outgoing, visited)

    print(visited)


dfs(graph, 1)

print(graph)