#need this for kargers, but there are other ways to do it I think 
import random
from copy import deepcopy

#open file
fp = open("C:\Code\StanfordAlgorithms\WorkInPython\ProblemSet3\kargerMinCut.txt", 'r')
data = fp.readlines()

#variables
graph = {}
E = 0

#read file
for row in data:
    row = row.strip()
    row = row.split()
    row = [int(x) for x in row]

    vertex_edges = row[1:]
    graph[row[0]] = vertex_edges
    E += len(vertex_edges)

#get supervertices (supernodes)
supervertices = {}
for key in graph:
    supervertices[key] = [key]

#len of graph is # of vertices left 
V = len(graph)


#main algo
def kargers_algorithm(graph, supervertices, E):
    min_cut = 0
    while len(graph) > 2:
        #random vertices
        vertice1, vertice2 = select_random_edge(graph,E)

        #updating edge count
        E -= len(graph[vertice1])
        E -= len(graph[vertice2])

        #merge the edges
        graph[vertice1].extend(graph[vertice2])

        #update references 
        for vertex in graph[vertice2]:
            graph[vertex].remove(vertice2)
            graph[vertex].append(vertice1)

        #remove self loops
        graph[vertice1] = [x for x in graph[vertice1] if x != vertice1]

        #update edge count again
        E += len(graph[vertice1])
        graph.pop(vertice2)

        #update the "cut grouping" in the graph
        supervertices[vertice1].extend(supervertices.pop(vertice2))

    #calc the mincut
    for edges in graph.values():
        min_cut = len(edges)

    return min_cut, supervertices


#really weird way of getting random vertices, but it works for some reason
def select_random_edge(graph, E):
    rand_edge = random.randint(0, E-1)

    for vertex, vertex_edges in graph.items():
        if len(vertex_edges) < rand_edge:
            rand_edge -= len(vertex_edges)

        else:
            from_vertex = vertex
            to_vertex = vertex_edges[rand_edge-1]
            return from_vertex, to_vertex
        

def main(graph):
    #karger is random, so we repeat for a high likelihood!!
    iterations = 10
    first_copy = deepcopy(graph)
    output = kargers_algorithm(first_copy, supervertices, E)
    min_cut = output[0]
    super_vertices = output[1]

    for i in range(iterations):
        copy = deepcopy(first_copy)
        output = kargers_algorithm(copy, supervertices, E)
        if output[0] < min_cut:
            min_cut = output[0]
            super_vertices = output[1]

    return min_cut

print(main(graph))


