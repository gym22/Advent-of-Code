import re

digits = (
    ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("0", 0), ("one", 1),
    ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9))


def find_digit(input_line):
    first_digit = 0
    last_digit = 0
    first_pos = 999
    last_pos = -1
    for digit in digits:
        m = re.search(digit[0], input_line)
        if m is not None:
            pos = m.span()[0]
            if first_pos > pos:
                first_pos = pos
                first_digit = digit

        m = re.search(".*(" + digit[0] + ")", input_line)
        if m is not None:
            pos = m.span()[1]
            if pos > last_pos:
                last_pos = pos
                last_digit = digit

    return first_digit[1] * 10 + last_digit[1]


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        num = find_digit(line)
        print(num)
        total_sum += num

print(f"Total Sum: {total_sum}")
