with open("input.txt") as file:
    fields = [[list(y) for y in x.split("\n")] for x in file.read().split("\n\n")]


def find_reflections(field):
    for i in range(0, len(field) - 1):
        if field[i] == field[i + 1]:
            s = True
            for r in range(1, min(i, len(field) - i) + 1):
                if i - r >= 0 and i + 1 + r < len(field) and field[i - r] != field[i + 1 + r]:
                    s = False
            if s:
                return i + 1
    return 0

sum = 0
for field in fields:
    sum += 100 * find_reflections(field)

    field = list(zip(*field))
    sum += find_reflections(field)

print(sum)
