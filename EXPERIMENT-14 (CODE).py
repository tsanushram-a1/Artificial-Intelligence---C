def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, (int, float)):
        return node

    if maximizing:
        best = float("-inf")
        for child in node:
            best = max(best, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    best = float("inf")
    for child in node:
        best = min(best, alpha_beta(child, depth - 1, alpha, beta, True))
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

score = alpha_beta(tree, 3, float("-inf"), float("inf"), True)
print("Best score:", score)
