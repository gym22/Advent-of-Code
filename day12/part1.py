import re

springs = []
conditions = []
with open("input.txt") as file:
    for line in file:
        s, c = line.strip().split(" ")
        springs.append(list(s))
        conditions.append([x for x in c.split(',')])


def test_line(line, n, variations):
    if n == len(line):
        thisline = ''.join(line)
        match = re.search(pattern, thisline)
        if match is not None:
            return variations + 1
        return variations
    elif line[n] == '?':
        copy = line.copy()
        copy[n] = "#"
        result = test_line(copy, n + 1, variations)
        copy2 = line.copy()
        copy2[n] = "."
        result = test_line(copy2, n + 1, result)
        return result
    else:
        return test_line(line, n + 1, variations)


def create_pattern(cond):
    p = '^[.]*'
    for i, x in enumerate(cond):
        p += '[#]{' + x + '}[.]'
        if i == len(cond) - 1:
            p += '*'
        else:
            p += '+'

    p = p
    return re.compile(p + '$')


variations = []
for i, line in enumerate(springs):
    pattern = create_pattern(conditions[i])
    #    print(pattern)
    variations.append(test_line(line, 0, 0))

print(variations)
print(sum(variations))
