
# Vacuum Cleaner Problem

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

current = 'A'

while True:
    print("Current Room:", current)

    if rooms[current] == 'Dirty':
        print("Cleaning Room", current)
        rooms[current] = 'Clean'
    else:
        print("Room", current, "is already clean")

    if current == 'A':
        current = 'B'
    else:
        break

print("Final Room Status:", rooms)
