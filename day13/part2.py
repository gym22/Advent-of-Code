with open("input.txt") as file:
    fields = [[list(y) for y in x.split("\n")] for x in file.read().split("\n\n")]


def find_reflections(field, original_h):
    for i in range(0, len(field) - 1):
        if i != original_h and field[i] == field[i + 1]:
            s = True
            for r in range(1, min(i, len(field) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field) and field[i - r] != field[i + 1 + r]:
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

def smudge(field):
        h = 0
        original_h = find_reflections(field, -1) - 1

        for i in range(0, len(field)):
            if h:
                break
            for r in range(0, len(field[0])):
                if h:
                    break

                field[i][r] = flip(field[i][r])
                h = find_reflections(field, original_h)
                if h:
                    return h
                field[i][r] = flip(field[i][r])
        return h


sum = 0
for field in fields:
    sum += 100 * smudge(field)
    field = [list(x) for x in zip(*field)]
    sum += smudge(field)

print(sum)
