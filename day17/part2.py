from queue import PriorityQueue

floormap = []
for line in open('input.txt').read().splitlines():
    floormap.append([int(x) for x in list(line)])

maxx = len(floormap[0]) - 1
maxy = len(floormap) - 1

q = PriorityQueue()
q.put((0, 0, 0, "R", 0))
q.put((0, 0, 0, "D", 0))
visited = set()

while not q.empty():

    heat_loss, y, x, direction, direction_steps = q.get()
    # print(heat_loss, y, x, direction, direction_steps)

    if (y, x, direction, direction_steps) in visited:
        continue

    if direction_steps >= 4:
        visited.add((y, x, direction, direction_steps))

    if x == maxx and y == maxy and direction_steps >= 4:
        print(f"min loss now: {heat_loss}")
        break

    if direction_steps < 4:
        if direction == "R" and 0 <= x + 1 <= maxx and 0 <= y <= maxy:
            q.put((heat_loss + floormap[y][x + 1], y, x + 1, "R", direction_steps + 1))

        if direction == "D" and 0 <= x <= maxx and 0 <= y + 1 <= maxy:
            q.put((heat_loss + floormap[y + 1][x], y + 1, x, "D", direction_steps + 1))

        if direction == "U" and 0 <= x <= maxx and 0 <= y - 1 <= maxy:
            q.put((heat_loss + floormap[y - 1][x], y - 1, x, "U", direction_steps + 1))

        if direction == "L" and 0 <= x - 1 <= maxx and 0 <= y <= maxy:
            q.put((heat_loss + floormap[y][x - 1], y, x - 1, "L", direction_steps + 1))
    else:
        if direction != "L" and (direction != "R" or direction_steps < 10) and 0 <= x + 1 <= maxx and 0 <= y <= maxy:
            q.put((heat_loss + floormap[y][x + 1], y, x + 1, "R", direction_steps + 1 if direction == "R" else 1))

        if direction != "U" and (direction != "D" or direction_steps < 10) and 0 <= x <= maxx and 0 <= y + 1 <= maxy:
            q.put((heat_loss + floormap[y + 1][x], y + 1, x, "D", direction_steps + 1 if direction == "D" else 1))

        if direction != "D" and (direction != "U" or direction_steps < 10) and 0 <= x <= maxx and 0 <= y - 1 <= maxy:
            q.put((heat_loss + floormap[y - 1][x], y - 1, x, "U", direction_steps + 1 if direction == "U" else 1))

        if direction != "R" and (direction != "L" or direction_steps < 10) and 0 <= x - 1 <= maxx and 0 <= y <= maxy:
            q.put((heat_loss + floormap[y][x - 1], y, x - 1, "L", direction_steps + 1 if direction == "L" else 1))
