
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 2, 'B': 1, 'C': 1, 'D': 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                new_f = new_cost + h[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_cost, neighbor,
                     path + [neighbor])
                )

astar('A', 'D')
