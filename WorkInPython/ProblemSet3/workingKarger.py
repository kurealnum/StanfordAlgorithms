from random import choice
from copy import deepcopy

def contract(graph):
    u = choice(list(graph.keys()))
    v = choice(graph[u])
    new_key = u+"-"+v 
    graph[new_key] = graph[u] + graph[v]
    del graph[u]
    del graph[v]
    for key in graph.keys():
        copy = graph[key][:]
        if new_key == key:
            for item in copy:
                if item == u or item == v:
                    graph[key].remove(item)
        else:
            for item in copy:
                if item == u or item == v:
                    graph[key].remove(item)
                    graph[key].append(new_key)
                    
    
def min_cut(graph):
    n = len(graph)
    minimum = n*(n-1)//2
    for i in range(1):
        copy =  deepcopy(graph)
        while len(copy) > 2:
            contract(copy)
            minimum = min(minimum , len(list(copy.values())[0]))
    return minimum
        

graph = {}
with open("C:\Code\StanfordAlgorithms\WorkInPython\ProblemSet3\kargerMinCut.txt", 'r') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
f.close()

print(min_cut(graph))