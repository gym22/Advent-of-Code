import re


def find_gears(fragment, fragment_line, fragment_start, gear_id):
    gear_iterator = re.finditer(r'\*', fragment)
    for gear in gear_iterator:
        all_gears.append({"line": fragment_line, "pos": gear.start()  + fragment_start, "gear": int(gear_id)})
        print({"line": fragment_line, "pos": gear.start() + fragment_start, "gear": int(gear_id)})


with open("day3input1.txt") as file:
    lines = [line.strip() for line in file]

all_gear_ratios = []
all_gears = []
number_of_lines = len(lines)
line_length = len(lines[0])

print(line_length, number_of_lines)

for line_no, line in enumerate(lines):
    part_number_iterator = re.finditer(r'\d+', line)
    for pn in part_number_iterator:
        start = pn.start() - 1
        end = pn.end() + 1
        if start == -1:
            start = 0
        if end >= line_length:
            end = line_length - 1
        p_num = pn.group()
        fragment = ""
        if line_no > 0:
            find_gears(lines[line_no - 1][start:end], line_no - 1, start, p_num)
        find_gears(lines[line_no][start:end], line_no, start, p_num)
        if line_no < number_of_lines - 1:
            find_gears(lines[line_no + 1][start:end], line_no + 1,  start, p_num)

print(all_gears)

for gear1 in all_gears:
    for gear2 in all_gears:
        if gear1['line'] == gear2['line'] and gear1['pos'] == gear2['pos'] and gear1['gear'] != gear2['gear']:
            print(gear1, gear2)
            all_gear_ratios.append(gear1['gear'] * gear2['gear'])

print(sum(all_gear_ratios)/2)

# 80703636
