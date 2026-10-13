
from itertools import permutations

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
min_cost = float('inf')
best_route = None

for route in permutations(cities):
    path = (0,) + route + (0,)
    cost = 0

    for i in range(len(path) - 1):
        cost += distance[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_route = path

print("Shortest Route:", best_route)
print("Minimum Distance:", min_cost)
