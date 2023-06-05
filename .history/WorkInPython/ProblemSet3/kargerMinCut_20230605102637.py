#need this for kargers, but there are other ways to do it
import random

fp = open("C:\Code\StanfordAlgorithms\WorkInPython\ProblemSet3\kargerMinCut.txt", 'r')
data = fp.readlines()
graph = {}

for row in data:
    row = row.strip()
    row = row.split()
    
    graph[row[0]] = row[1:]

#len of graph is # of vertices left 
V = len(graph)
E = V * (V-1)/2



'''while len(graph) > 2:
    first_vertice = random.randint(1,len(graph))
    second_vertice = random.randint(1,len(graph))'''

def select_random_edge(E, graph):
    rand_edge = random.randint(0, E-1)
    print(rand_edge)
    for vertex, vertex_edges in graph.items():
        if len(vertex_edges) < rand_edge:
            rand_edge -= len(vertex_edges)
        else:
            from_vertex = vertex
            to_vertex = vertex_edges[rand_edge-1]
            return from_vertex, to_vertex
     
print(select_random_edge(E, graph), "asasad")
