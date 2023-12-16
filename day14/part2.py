rocks = []

with open("input.txt") as file:
    for line in file:
        rocks.append(list(line.strip()))

weight = len(rocks)


def roll_rocks():
    open_positions = [0] * len(rocks[0])
    total_load = 0
    for r, row in enumerate(rocks):
        for i, place in enumerate(row):
            if place == "O":
                if open_positions[i] != r:
                    rocks[open_positions[i]][i] = "O"
                    rocks[r][i] = "."

                total_load += weight - open_positions[i]
                open_positions[i] += 1
            if place == "#":
                open_positions[i] = r + 1
    return total_load


def calculate_weight():
    total_load = 0
    for r, row in enumerate(rocks):
        for i, place in enumerate(row):
            if place == "O":
                total_load += weight - r
    return total_load


def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i + len(pattern)] == pattern:
            matches.append(i)
        if len(matches) > 1:
            break
    return matches


def add_cycles(addcycles):
    global rocks
    for c in range(0, addcycles):
        for i in range(0, 4):
            roll_rocks()
            rocks = [list(x) for x in zip(*rocks[::-1])]
        weights.append(calculate_weight())


weights = []

# arbitrary starting point
cycles = 16
test_length = 8
add_cycles(cycles)

while True:
    testpattern = weights[cycles - test_length:cycles]
    loops = subfinder(weights, testpattern)
    if len(loops) >= 2:
        loop_length = loops[1] - loops[0]
        loop_start = loops[0]
        break
    else:
        test_length *= 2

    if test_length > cycles // 4:
        add_cycles(cycles)
        cycles *= 2

    print(loops, test_length)

index_at_end = (1000000000 - loop_start) % loop_length
if index_at_end == 0:
    index_at_end = loop_length

print(f"loop lenth: {loop_length} loop_start: {loop_start} cycles: {cycles} test length: {test_length} final index: {index_at_end}")
print("weight at 1000000000", testpattern[index_at_end-1])
