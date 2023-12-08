import re

with open("input.txt") as file:
    rawinstructions, rawmaps = file.read().split('\n\n')

    instructions = list(rawinstructions)
    maps = {x[0]: {"L": x[1], "R": x[2]} for x in re.findall('(\\w{3}) = \\((\\w{3}). (\\w{3})', rawmaps)}

# print(maps)
location = "AAA"
finallocation = "ZZZ"
steps = 0

while location != finallocation:
    instruction = instructions.pop(0)
    instructions.append(instruction)

    location = maps[location][instruction]
#    print(location, instruction)
    steps += 1

print(steps)
