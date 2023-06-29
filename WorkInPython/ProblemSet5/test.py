import math
inf = math.inf

Q = {
    1: inf,
    2: inf,
    3: inf,
    4: inf
}

print(min(Q, key=Q.get))
Q.pop(1)

print(Q)