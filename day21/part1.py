garden = []
nextsteps = set()

for row, line in enumerate(open('input.txt')):
    if "S" in line:
        nextsteps.add((line.index("S"), row))
    garden.append(line)

maxx = len(garden[0]) - 1
maxy = len(garden[1]) - 1

for step in range(65):
    steps = nextsteps.copy()
    nextsteps = set()
    for x, y in steps:
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nextx = x + dx
            nexty = y + dy
            if nexty < 0 or nextx < 0 or nextx > maxx or nexty > maxy or garden[nexty][nextx] == "#":
                continue
            nextsteps.add((nextx, nexty))

print(len(steps))
