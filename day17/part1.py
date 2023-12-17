floormap = []
for line in open('input.txt').read().splitlines():
    floormap.append([int(x) for x in list(line)])

maxx = len(floormap[0]) - 1
maxy = len(floormap) - 1

q = [(0, 0, 0, "", 0)]
visited = set()


while len(q) > 0:

    ind = q.index(min(q))
#    print(q[ind])
    heat_loss, y, x, direction, direction_steps = q.pop(ind)

    if (y, x, direction, direction_steps) in visited:
        continue

    visited.add((y, x, direction, direction_steps))

    if x == maxx and y == maxy:
        print(f"min loss now: {heat_loss}")
        break

    if direction != "L" and (direction != "R" or direction_steps < 3) and 0 <= x + 1 <= maxx and 0 <= y <= maxy:
        q.append((heat_loss + floormap[y][x + 1], y, x + 1, "R", direction_steps + 1 if direction == "R" else 1))

    if direction != "U" and (direction != "D" or direction_steps < 3) and 0 <= x <= maxx and 0 <= y + 1 <= maxy:
        q.append((heat_loss + floormap[y + 1][x], y + 1, x, "D", direction_steps + 1 if direction == "D" else 1))

    if direction != "D" and (direction != "U" or direction_steps < 3) and 0 <= x <= maxx and 0 <= y - 1 <= maxy:
        q.append((heat_loss + floormap[y - 1][x], y - 1, x, "U", direction_steps + 1 if direction == "U" else 1))

    if direction != "R" and (direction != "L" or direction_steps < 3) and 0 <= x - 1 <= maxx and 0 <= y <= maxy:
        q.append((heat_loss + floormap[y][x - 1], y, x - 1, "L", direction_steps + 1 if direction == "L" else 1))
