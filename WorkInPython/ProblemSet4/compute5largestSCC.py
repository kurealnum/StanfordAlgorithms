#Kosaraju's algorithms. m = # of edges, n = # of vertices
#do not print the graph, its 5 million lines in a .txt so...
import sys #import sys for recursion limit
from collections import defaultdict

#normal and reversed graph
vertices = set()
graph = defaultdict(list)
grev = defaultdict(list)


#reading the file
with open('SCC.txt', "r") as f:
    data = f.readlines()
    for row in data:
        row = row.strip()
        row = row.split()
        row = [int(x) for x in row]

        vertex_outs = row[1:]
        graph[row[0]] = vertex_outs + graph.get(row[0], [])

        #get ALL the vertices (i.e. don't miss vertices that aren't a dict key!)
        vertices.update(set(row))


#O(m + n) 
def reverse_graph(g, grev):
    for k in graph:
        for v in g[k]:
            grev[v].append(k)


#O(m + n)
def first_dfs(G, s, visited, stack):
    visited[s] = True

    for v in G[s]:
        if not visited[v]:
            first_dfs(G, v, visited, stack)

    stack.append(s)


#O(m + n): same as first_dfs, just uses SCC instead of stack. its the exact same thing otherwise
def second_dfs(G, s, visited, SCC):
    visited[s] = True

    for v in G[s]:
        if not visited[v]:
            first_dfs(G, v, visited, SCC)

    SCC.append(s)    


#--------------main code--------------

#setting recursion depth limit
sys.setrecursionlimit(10000)
print("Set recursion limit")

#reversing the graph (grev is the reversed graph)
reverse_graph(graph, grev)
print("Reversed the graph")

#intial variables
visited = [False] * (len(vertices) + 1)
stack = []

#creating the intitial stack. not 0 indexed, hence the weird range() 
for i in range(1, len(vertices) + 1):
    if not visited[i]:
        first_dfs(graph, i, visited, stack)

print("Passed first DFS")

#reset visited, add an array for all_sccs
visited = [False] * (len(vertices) + 1)
all_scc = []

#second set of DFS calls
while stack:
    #work down from the top of the stack
    i = stack.pop()

    if not visited[i]:
        SCC = []
        #fill SCC
        second_dfs(grev, i, visited, SCC)

        #if the length of ALL the SCCs is greater than 5
        if len(all_scc) >= 5: 
            for i in range(len(all_scc)):
                if len(all_scc[i]) < len(SCC):
                    #switch the smallest in the set of 5 with the current SCC
                    all_scc[i] = SCC

        else:
            all_scc.append(SCC)

biggest_SCC = []

print("Passed second DFS")

#getting the counts
for i in all_scc:
    biggest_SCC.append(len(i))

print(sorted(biggest_SCC, reverse=True))
