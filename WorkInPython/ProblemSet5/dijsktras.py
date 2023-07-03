#define an infinte variable
import math
inf = math.inf

#g = graph
#key: [adj veretex, length from key]
g = {}

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

        g[int(key)] = adjs


#variables
#distance values for each vertex, Q is a copy of g_distances
g_distances = {k:inf for k,v in g.items()}
Q = {k:inf for k,v in g.items()}

#S is the vertices we already visited
S = []

#set 1's distance to 0
g_distances[1] = 0


#main algo
while len(Q) > 0:
    #minimum
    u = min(Q, key=Q.get)
    Q.pop(u)

    #add u to S
    S.append(u)

    #for every vertex adjacent to u
    for v in g[u]:
        if v in S:
            continue

        #adjacent vertex
        adj_v = v[0]

        #if v's distance is greater than u's distance + the distance between u and v (relaxing)
        if g_distances[adj_v] > g_distances[u] + v[1]:
            g_distances[adj_v] = g_distances[u] + v[1]


#print the results
print(g_distances[7], g_distances[37], g_distances[59], g_distances[82], g_distances[99], g_distances[115], g_distances[133], g_distances[165], g_distances[188], g_distances[197])


    