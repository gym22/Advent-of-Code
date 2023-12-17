floormap = open('input.txt').read().split(('\n'))
floor_width = len(floormap[0])
floor_height = len(floormap)

movements = {
    "U": (-1, 0, "U"),
    "D": (1, 0, "D"),
    "R": (0, 1, "R"),
    "L": (0, -1, "L")
}

directions = {
    "R": {
        ".": movements["R"],
        "-": movements["R"],
        "/": movements["U"],
        "\\": movements["D"],
        "|": "SPLIT"
    },
    "L": {
        ".": movements["L"],
        "-": movements["L"],
        "/": movements["D"],
        "\\": movements["U"],
        "|": "SPLIT"
    },
    "U": {
        ".": movements["U"],
        "-": "SPLIT",
        "/": movements["R"],
        "\\": movements["L"],
        "|": movements["U"]
    },
    "D": {
        ".": movements["D"],
        "-": "SPLIT",
        "/": movements["L"],
        "\\": movements["R"],
        "|": movements["D"]
    }
}


def beam(y, x, direction, visited):
    while True:
        if (y, x, direction) in visited:
            return
        if x < 0 or y < 0 or y >= floor_height or x >= floor_width:
            return

        visited.add((y, x, direction))
        tile = floormap[y][x]
        nextmove = directions[direction][tile]

        if nextmove == "SPLIT":
            if direction in "UD":
                beam(y, x + 1, "R", visited)
                beam(y, x - 1, "L", visited)
            else:
                beam(y - 1, x, "U", visited)
                beam(y + 1, x, "D", visited)
        else:
            y += nextmove[0]
            x += nextmove[1]
            direction = nextmove[2]


def get_energy(position):
    visited = set()
    beam(*position, visited)
    return len({(x[0], x[1]) for x in visited})


def get_edges():
    for yy in range(floor_height):
        yield yy, 0, "R"
        yield yy, floor_width - 1, "L"
    for xx in range(floor_width):
        yield 0, xx, "D"
        yield floor_height - 1, xx, "U"


print(max(map(get_energy, get_edges())))

