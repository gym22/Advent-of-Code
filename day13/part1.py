with open("input.txt") as file:
    fields = [[y for y in x.split("\n")] for x in file.read().split("\n\n")]

horizontals = []
verticals = []


def find_horizontals(field):
    for i in range(0, len(field) - 1):
        if field[i] == field[i + 1]:
            s = True
            for r in range(1, min(i, len(field) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field) and field[i - r] != field[i + 1 + r]:
                    s = False
            if s:
                horizontals.append(i + 1)


def compare_vertical(field, c1, c2):
    for line in field:
        if line[c1] != line[c2]:
            return False
    return True


def find_verticals(field):
    for i in range(0, len(field[0]) - 1):
        if compare_vertical(field, i, i + 1):
            s = True
            for r in range(1, min(i, len(field[0]) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field[0]) and not compare_vertical(field, i - r, i + 1 + r):
                    s = False
            if s:
                verticals.append(i + 1)


for field in fields:
    find_horizontals(field)
    find_verticals(field)

print(sum(horizontals) * 100 + sum(verticals))
