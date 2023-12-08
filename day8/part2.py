import re
import math


def find_loop_length(loc):
    location = loc
    steps = 0
    while location not in endlocations:
        instruction = instructions.pop(0)
        instructions.append(instruction)

        location = maps[location][instruction]

        steps += 1
    return steps


with open("input.txt") as file:
    rawinstructions, rawmaps = file.read().split('\n\n')

    instructions = list(rawinstructions)
    maps = {x[0]: {"L": x[1], "R": x[2]} for x in re.findall('(\\w{3}) = \\((\\w{3}). (\\w{3})', rawmaps)}

# print(maps)
locations = [x for x in list(maps) if x[2] == "A"]
endlocations = [x for x in list(maps) if x[2] == "Z"]

loops = [find_loop_length(location) for location in locations]
print(loops)
print(math.lcm(*loops))
