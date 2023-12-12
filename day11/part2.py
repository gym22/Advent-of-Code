import math

universe = []
cols = None
galaxies = []
expansion = 1000 # with 1000x expansion, numbers are large enough to just add zeroes
expansion2 = 1000000

with open("input.txt") as file:
    for line in file:
        row = [1 if p == "#" else 0 for p in list(line.strip())]
        if cols is not None:
            cols = map(lambda x, y: x + y, cols, row)
        else:
            cols = row.copy()

        universe.append(row)
        if sum(row) == 0:
            print("expand row... ")
            for n in range(1,expansion):
                universe.append(row.copy())

# expand columns
n = 0
for i, col in enumerate(list(cols)):
    if col == 0:
        print("expand col ", i, i+n)
        for c in range(1,expansion):
            n += 1
            for row in universe:
                row.insert(i + n, 0)


def find_galaxies():
    n = 0
    for y, row in enumerate(universe):
        for x, pixel in enumerate(row):
            if pixel == 1:
                n += 1
                galaxies.append({"id": n, "y": y, "x" : x})

def draw_line(y1, x1, y2, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    if x1 == x2:
        return y2 - y1
    if y1 == y2:
        return x2 - x1

    dx = x2 - x1
    dy = y2 - y1

    if dx > dy:
        return draw_low_slopex(y1, x1, y2, x2)
    else:
        return draw_low_slopey(y1, x1, y2, x2)


def draw_low_slopex(y1, x1, y2, x2):
    steps = 0
    prevy = y1
    dx = x2 - x1
    dy = y2 - y1

    for x in range(x1, x2):
        y = y1 + math.floor(dy * (x - x1) / dx)

        steps += 1
        if y > prevy:
            steps += 1
        prevy = y
    return steps + 1


def draw_low_slopey(y1, x1, y2, x2):
    steps = 0
    prevx = x1
    dx = x2 - x1
    dy = y2 - y1

    for y in range(y1, y2):
        x = x1 + math.floor(dx * (y - y1) / dy)
        steps += 1
        if x > prevx:
            steps += 1
        prevx = x
    return steps + 1

find_galaxies()

# sample tests
# print(draw_line(6, 1, 11, 5))
# print(draw_line(0, 4, 10, 9))
# print(draw_line(2, 0, 7, 12))
# print(draw_line(11, 0, 11, 5))

pairs = 0
total_steps = 0
while len(galaxies) > 0:
    g1 = galaxies.pop(0)
    for g2 in galaxies:
        steps = draw_line(g1["y"], g1["x"], g2["y"], g2["x"])
        # with 1000x expansion, numbers are large enough to just add zeroes
        total_steps += steps//expansion*expansion2 + steps%expansion
        pairs += 1


print("pairs", pairs, "steps", total_steps)
