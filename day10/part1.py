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


def find_next_step(posy, posx, heading):
    nextheading = directions[heading][pipemap[posy][posx]]
    nextx = posx + movements[nextheading]["x"]
    nexty = posy + movements[nextheading]["y"]
    pipemap[posy][posx] = "#"
    return nexty, nextx, nextheading


print(y, x)

y, x, direction = find_starting_direction(y, x)

# print("starting", y, x, direction)

steps = 1
while pipemap[y][x] != "S":
    y, x, direction = find_next_step(y, x, direction)
    steps += 1
#    print(y,x, direction, pipemap[y][x])

for line in pipemap:
    print(''.join(line))

print(steps/2)