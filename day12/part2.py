def test_line(springs, conditions, last_spring):
    # print(first_part, springs, conditions)

    key = (last_spring,springs, conditions)
    if key in cache:
        return cache[key]

    if len(conditions) == 0:
        if "#" not in springs:
            return 1
        else:
            return 0

    current_count = conditions[0]
    if len(springs) == 0:
        if current_count == 0 and len(conditions) == 1:
            return 1
        else:
            return 0

    current_spring = springs[0]
    next_springs = springs[1:]

    result = 0
    if current_spring == "?":
        result = test_line("." + next_springs, conditions, last_spring)
        if current_count > 0 or last_spring == "#":
            result += test_line("#" + next_springs, conditions, last_spring)

    if current_spring == '.':
        if current_count == 0:
            result = test_line(next_springs, conditions[1:], current_spring)
        elif not (last_spring == "#"):
            result = test_line(next_springs, conditions, current_spring)

    if current_spring == "#":
        if current_count > 0:
            result = test_line(next_springs, tuple([current_count - 1]) + conditions[1:], current_spring)

    cache[key] = result
    return result


total = 0
cache = {}
with open("input.txt") as file:
    for line in file:
        s, c = line.strip().split(" ")
        total += test_line("?".join(5 * [s]), tuple(map(int,c.split(',')*5)), " ")

print(total)
