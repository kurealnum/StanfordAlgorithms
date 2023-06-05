graph = {"1": ["2","3","4"],
         "2": ["1","3"],
         "3": ["1","2"],
         "4": ["1"]}

count = 0
start = "4"
end = "3"
iter = start

ran_vert_one = "3"
ran_vert_two = graph[ran_vert_one][0]

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