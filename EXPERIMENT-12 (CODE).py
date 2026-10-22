regions = ['A', 'B', 'C', 'D']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
result = {}

def solve(i):
    if i == len(regions):
        return True
    r = regions[i]
    for c in colors:
        if all(result.get(n) != c for n in neighbors[r]):
            result[r] = c
            if solve(i + 1):
                return True
            del result[r]
    return False

solve(0)
print(result)
