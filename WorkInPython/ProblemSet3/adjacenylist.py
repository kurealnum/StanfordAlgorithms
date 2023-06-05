graph = {"A": ["B","C","D"],
         "B": ["A","C"],
         "C": ["A","B"],
         "D": ["A"]}

count = 0
start = "E"
end = "A"
iter = start

graph["E"] = ["B","C"]

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