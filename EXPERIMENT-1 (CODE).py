import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def manhattan(state):
    """Sum of each tile's Manhattan distance from its goal position."""
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = tile - 1
        row, col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(row - goal_row) + abs(col - goal_col)
    return distance

def neighbors(state):
    """Yield each state reachable by one legal move."""
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            next_state = list(state)
            next_state[blank], next_state[new_blank] = (
                next_state[new_blank], next_state[blank]
            )
            yield tuple(next_state)

def is_solvable(state):
    """For a 3x3 puzzle, the inversion count must be even."""
    tiles = [tile for tile in state if tile != 0]
    inversions = sum(
        tiles[i] > tiles[j]
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
    )
    return inversions % 2 == 0

def solve(start):
    if not is_solvable(start):
        return None

    # Heap entries: (estimated total cost, moves so far, state)
    frontier = [(manhattan(start), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, moves, current = heapq.heappop(frontier)

        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        # Ignore outdated heap entries.
        if moves != cost_so_far[current]:
            continue

        for nxt in neighbors(current):
            new_cost = moves + 1
            if new_cost < cost_so_far.get(nxt, float("inf")):
                cost_so_far[nxt] = new_cost
                came_from[nxt] = current
                heapq.heappush(
                    frontier,
                    (new_cost + manhattan(nxt), new_cost, nxt)
                )

    return None

def print_board(state):
    for row in range(3):
        print(" ".join(
            "_" if tile == 0 else str(tile)
            for tile in state[row * 3:(row + 1) * 3]
        ))
    print()

def main():
    try:
        start = tuple(map(int, input(
            "Enter 9 numbers (0 for blank), separated by spaces: "
        ).split()))

        if len(start) != 9 or set(start) != set(range(9)):
            raise ValueError

    except ValueError:
        print("Invalid input. Enter each number from 0 to 8 exactly once.")
        return

    path = solve(start)
    if path is None:
        print("This puzzle has no solution.")
        return

    print(f"Solved in {len(path) - 1} moves:")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        print_board(state)

if __name__ == "__main__":
    main()
