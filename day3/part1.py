import re


def has_symbol(fragment):
    if re.search(r'[^\d.]', fragment) is not None:
        return True
    return False


with open("input.txt") as file:
    lines = [line.strip() for line in file]

all_part_numbers = []
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
        print(p_num, start, end)
        fragment = ""
        if line_no > 0:
            fragment = lines[line_no - 1][start:end]
        fragment += lines[line_no][start:end]
        if line_no < number_of_lines - 1:
            fragment += lines[line_no + 1][start:end]
        print(line_no, p_num, has_symbol(fragment), fragment)
        if has_symbol(fragment):
            all_part_numbers.append(int(p_num))

print(sum(all_part_numbers))
