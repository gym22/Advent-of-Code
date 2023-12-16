rocks = []

with open("input.txt") as file:
    for line in file:
        rocks.append(list(line))

weight = len(rocks)


def calculate_weights():
    open_positions = [0]*len(rocks[0])
    total_load = 0
    for r, row in enumerate(rocks):
        for i, place in enumerate(row):
            if place == "O":
                total_load += weight - open_positions[i]
                open_positions[i] += 1
            if place == "#":
                open_positions[i] = r + 1
    return total_load


print(calculate_weights())
