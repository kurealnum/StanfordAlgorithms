#need this for kargers, but there are other ways to do it
import random

fp = open("C:\Code\Python\StanfordAlgorithms\ProblemSet3\kargerMinCut.txt", 'r')
data = fp.readlines()
graph = {}

for row in data:
    row = row.strip()
    row = row.split()
    
    graph[row[0]] = row[1:]

#len of graph is # of vertices left 
V = len(graph)
E = V * (V-1)/2

while len(graph) > 2:
    i = random.randint(1,len(graph))
     
