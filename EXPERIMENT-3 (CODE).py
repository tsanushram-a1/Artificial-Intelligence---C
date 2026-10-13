from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        # Check whether target is reached
        if jug1 == target or jug2 == target:
            print("Solution found!")
            print("Jug 1:", jug1, "litres")
            print("Jug 2:", jug2, "litres")
            return

        # Possible operations
        states = [
            (capacity1, jug2),                         # Fill Jug 1
            (jug1, capacity2),                         # Fill Jug 2
            (0, jug2),                                 # Empty Jug 1
            (jug1, 0),                                 # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            # Pour Jug 2 -> Jug 1
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution exists.")


# Input
capacity1 = 4
capacity2 = 3
target = 2

water_jug_problem(capacity1, capacity2, target)
