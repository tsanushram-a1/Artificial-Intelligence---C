regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def solve(region):
    if region == len(regions):
        return True

    current = regions[region]

    for color in colors:
        if all(result.get(n) != color
               for n in neighbors[current]):
            result[current] = color

            if solve(region + 1):
                return True

            del result[current]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution found")
