import re

pipemap = []
y = 0
x = 0

directions = {
    "SOUTH": {
        "|": "SOUTH",
        "L": "EAST",
        "J": "WEST",
    },
    "NORTH": {
        "|": "NORTH",
        "F": "EAST",
        "7": "WEST",
    },
    "WEST": {
        "-": "WEST",
        "F": "SOUTH",
        "L": "NORTH",
    },
    "EAST": {
        "-": "EAST",
        "7": "SOUTH",
        "J": "NORTH",
    }
}

movements = {
    "NORTH": {"y": -1, "x": 0},
    "SOUTH": {"y": 1, "x": 0},
    "EAST": {"y": 0, "x": 1},
    "WEST": {"y": 0, "x": -1}
}

with open("input.txt") as file:
    for i, line in enumerate(file):
        sstr = re.search(r"S", line)
        if sstr is not None:
            y = i
            x = sstr.start()
        pipemap.append([p for p in list(line.strip())])


def find_starting_direction(posy, posx):
    heading = "UNKNOWN"
    if pipemap[posy - 1][posx] in ["|", "7", "F"]:
        posy = posy - 1
        heading = "NORTH"
    elif pipemap[posy + 1][posx] in ["|", "J", "L"]:
        posy = posy + 1
        heading = "SOUTH"
    elif pipemap[posy][posx - 1] in ["-", "F", "L"]:
        posx = posx - 1
        heading = "WEST"
    elif pipemap[posy][posx + 1] in ["|", "J", "7"]:
        posx = posx + 1
        heading = "EAST"
    else:
        print("map error", posx, posy)
    return posy, posx, heading


def create_double_map():
    for line in pipemap:
        doubleline = []
        for tile in line:
            doubleline.append(tile)
            doubleline.append(" ")
        doublemap.append(doubleline)
        doubleline = []
        for tile in line:
            doubleline.append(" ")
            doubleline.append(" ")
        doublemap.append(doubleline)


def mark_direction_on_map(posy, posx, heading):
    if heading == "NORTH":
        doublemap[posy * 2 + 1][posx * 2] = "↑"
    if heading == "SOUTH":
        doublemap[posy * 2 - 1][posx * 2] = "↓"
    if heading == "EAST":
        doublemap[posy * 2][posx * 2 - 1] = "→"
    if heading == "WEST":
        doublemap[posy * 2][posx * 2 + 1] = "←"


def find_next_step(posy, posx, heading):
    nextheading = directions[heading][pipemap[posy][posx]]
    nextx = posx + movements[nextheading]["x"]
    nexty = posy + movements[nextheading]["y"]

    # mark visited locations for visualisation
    if heading != nextheading:  # corner for better visibility
        doublemap[posy * 2][posx * 2] = "K"
    else:
        doublemap[posy * 2][posx * 2] = "#"

    mark_direction_on_map(posy, posx, heading)
    return nexty, nextx, nextheading


pipemap[y][x] = "#"

doublemap = []
create_double_map()
y, x, direction = find_starting_direction(y, x)

print("starting", y, x, direction)

steps = 1
while pipemap[y][x] != "#":
    y, x, direction = find_next_step(y, x, direction)
    steps += 1
#    print(y, x, direction, pipemap[y][x])

# connect last step
mark_direction_on_map(y, x, direction)

print(steps / 2)
# for line in doublemap:
#     print(''.join(line))

inside_tiles = 0
for y, line in enumerate(doublemap):
    if y % 2 == 1:
        continue
    inside = False
    for x, tile in enumerate(line[:-1]):
        if x % 2 == 1:
            continue
        lowertile = doublemap[y + 1][x]
        if tile == "#" or tile == "K":
            if lowertile == "↑" or lowertile == "↓":
                inside = not inside
        elif inside:
            doublemap[y][x] = "I"
            inside_tiles += 1
        else:
            doublemap[y][x] = "O"

for line in doublemap:
    print(''.join(line))

print(inside_tiles)
