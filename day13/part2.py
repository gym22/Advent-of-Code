with open("input.txt") as file:
    fields = [[list(y) for y in x.split("\n")] for x in file.read().split("\n\n")]

horizontals = []
verticals = []


def find_horizontals(field, original_h):
    for i in range(0, len(field) - 1):
        if i != original_h and field[i] == field[i + 1]:
            s = True
            for r in range(1, min(i, len(field) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field) and field[i - r] != field[i + 1 + r]:
                    s = False
            if s:
                return i + 1
    return 0


def compare_vertical(field, c1, c2):
    for line in field:
        if line[c1] != line[c2]:
            return False
    return True


def find_verticals(field, original_v):
    for i in range(0, len(field[0]) - 1):
        if i != original_v and compare_vertical(field, i, i + 1):
            s = True
            for r in range(1, min(i, len(field[0]) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field[0]) and not compare_vertical(field, i - r, i + 1 + r):
                    s = False
            if s:
                return i + 1
    return 0


def flip(f):
    if f == "#":
        f = "."
    else:
        f = "#"
    return f


for field in fields:
    h = 0
    v = 0
    original_h = find_horizontals(field, -1) - 1
    original_v = find_verticals(field, -1) - 1

    for i in range(0, len(field)):
        if h or v:
            break
        for r in range(0, len(field[0])):
            if h or v:
                break

            field[i][r] = flip(field[i][r])
            h = find_horizontals(field, original_h)
            if h:
                horizontals.append(h)
            v = find_verticals(field, original_v)
            if v:
                verticals.append(v)
            field[i][r] = flip(field[i][r])

print(sum(horizontals) * 100 + sum(verticals))
