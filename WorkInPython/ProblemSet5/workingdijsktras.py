import heapq

graph = {}

with open("dijkstraData.txt", "r") as f:
    data = f.readlines()
    for row in data:
        row = row.strip()
        row = row.split()

        key = row[0]
        adjs = []
        for vertex in row[1:]:
            split_vertex = (vertex.split(","))
            split_vertex = [int(i) for i in split_vertex]
            adjs.append(split_vertex)

        graph[int(key)] = adjs

# iPair ==> Integer Pair
iPair = tuple
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]
 
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
 
    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
 
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
 
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
 
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
 
        # Print shortest distances stored in dist[]
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
 
# Driver's code
if __name__ == "__main__":
    # create the graph given in above figure
    V = 201
    g = Graph(V)
 
    # making above shown graph
    g.addEdge(0, 1, 0)
    g.addEdge(0, 7, 8)
    
    #key: [adj veretex, length from key]
    for k,v in graph.items():
        for values in v:
            g.addEdge(k, values[0], values[1])
 
    g.shortestPath(0)