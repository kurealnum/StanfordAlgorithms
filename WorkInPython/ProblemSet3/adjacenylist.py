import random

graph = {"A": ["B","C","D"],
         "B": ["A","C","D"],
         "C": ["A","B"],
         "D": ["A","B"]}


#this is the worst possible algorithm you could ever have for a graph, it's just for practice though!
def slow_find(graph, start, end):
    iter = start
    while True:
        if start == end:
            print("We're already here")
            break

        if end in graph[iter]:
            count += 1
            print(f"This took {count} steps")
            break

        else:
            count += 1
            iter = graph[iter][0]

#adding to node1, removing node2
def merge_node(graph, node1, node2):
    #create the new list
    graph[node1] = list(set(graph[node1] + graph[node2]))
    
    #removing "duplicates"
    if node1 in graph[node1]:
        graph[node1].remove(node1)

    if node2 in graph[node2]:
        graph[node1].remove(node2)

    #removing extra nodes
    graph.pop(node2)

    #remove all instances of node2 in each subarray in the graph
    for node, neighs in graph.items():
        if node2 in graph[node]:
            graph[node].remove(node2)


while len(graph) > 2:
    #keys of the graph hashmap
    graph_vertices = list(graph.keys())
    #random graph index with the graph vertices
    random_graph_index = graph_vertices[random.randint(0,len(graph)-1)]

    length_of_node1 = len(graph[random_graph_index])
    random_graph_edge = random.randint(0,length_of_node1-1) #i say "edge" lightly because its not technically an edge

    #node 1 and 2 correspond to node1 and node2 in merge_node()
    node1 = random_graph_index
    node2 = graph[random_graph_index][random_graph_edge]

    #merging process
    merge_node(graph, node1, node2)

print(graph)
        