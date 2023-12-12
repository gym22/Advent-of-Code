universe = []
cols = None
galaxies = []
expansion = 1000  # with 1000x expansion, numbers are large enough to just add zeroes
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
            for n in range(1, expansion):
                universe.append(row.copy())

# expand columns
n = 0
for i, col in enumerate(list(cols)):
    if col == 0:
        print("expand col ", i, i + n)
        for c in range(1, expansion):
            n += 1
            for row in universe:
                row.insert(i + n, 0)


def find_galaxies():
    n = 0
    for y, row in enumerate(universe):
        for x, pixel in enumerate(row):
            if pixel == 1:
                n += 1
                galaxies.append({"id": n, "y": y, "x": x})


def draw_line(y1, x1, y2, x2):
    if x1 > x2:
        x1, x2 = x2, x1

    dx = x2 - x1
    dy = y2 - y1

    return dx + dy


find_galaxies()

pairs = 0
total_steps = 0
while len(galaxies) > 0:
    g1 = galaxies.pop(0)
    for g2 in galaxies:
        steps = draw_line(g1["y"], g1["x"], g2["y"], g2["x"])
        # with 1000x expansion, numbers are large enough to just add zeroes
        total_steps += steps // expansion * expansion2 + steps % expansion
        pairs += 1

print("pairs", pairs, "steps", total_steps)
