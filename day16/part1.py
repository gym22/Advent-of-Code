floormap = open('input.txt').read().split(('\n'))

visited = set()
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


def beam(y, x, direction):
    while True:
        if (y, x, direction) in visited:
            return
        if x < 0 or y < 0 or y >= len(floormap) or x >= len(floormap[0]):
            return

        visited.add((y, x, direction))
        tile = floormap[y][x]
        nextmove = directions[direction][tile]

        if nextmove == "SPLIT":
            if direction in "UD":
                beam(y, x + 1, "R")
                beam(y, x - 1, "L")
            else:
                beam(y - 1, x, "U")
                beam(y + 1, x, "D")
        else:
            y += nextmove[0]
            x += nextmove[1]
            direction = nextmove[2]

beam(0, 0, "R")
cleanvisited = {(x[0],x[1]) for x in visited}
print(len(cleanvisited))