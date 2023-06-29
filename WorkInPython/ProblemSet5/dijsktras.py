#define an infinte variable
import math
inf = math.inf

#g = graph
#key: [length from key, adj veretex]
g = {
    1: [[100, 3],[5, 2]],
    2: [[2, 3],[5, 1]],
    3: [[100, 1], [2, 2], [1, 4]],
    4: [[1, 3]]
}

#distance values for each vertex
g_distances = {
    1: inf,
    2: inf,
    3: inf,
    4: inf
}

#S is the vertices we already visited, Q is the vertices we have yet to visit
S = []
Q = {
    1: inf,
    2: inf,
    3: inf,
    4: inf
}

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
        #adjacent vertex
        adj_v = v[1]

        #if v's distance is greater than u's distance + the distance between u and v
        print(u, adj_v)
        if g_distances[adj_v] > g_distances[u] + v[0]:
            g_distances[adj_v] = g_distances[u] + v[0]

print(g_distances)

    