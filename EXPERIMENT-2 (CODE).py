def solve_queens(n=8):
    """Return all solutions as lists of column positions, one per row."""
    solutions = []
    placement = []

    def backtrack(row, columns, diag_down, diag_up):
        if row == n:
            solutions.append(placement.copy())
            return

        for col in range(n):
            down = row - col
            up = row + col
            if col in columns or down in diag_down or up in diag_up:
                continue

            placement.append(col)
            backtrack(
                row + 1,
                columns | {col},
                diag_down | {down},
                diag_up | {up},
            )
            placement.pop()

    backtrack(0, set(), set(), set())
    return solutions


def print_board(solution):
    n = len(solution)
    for col in solution:
        print(". " * col + "Q " + ". " * (n - col - 1))
    print()


if __name__ == "__main__":
    solutions = solve_queens()
    print(f"Found {len(solutions)} solutions. Showing the first:\n")
    print_board(solutions[0])
