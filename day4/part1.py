with open("input.txt") as file:
    lines = [line.strip() for line in file]

all_points = []

for line in lines:
    numbers = line.split(":")[1]
    split_numbers = numbers.split(" |")
    winning_numbers_string = split_numbers[0]
    my_numbers_strnig = split_numbers[1]

    winning_numbers = {winning_numbers_string[start:start + 3] for start in range(0, len(winning_numbers_string), 3)}
    my_numbers = {my_numbers_strnig[start:start + 3] for start in range(0, len(my_numbers_strnig), 3)}
    wins = winning_numbers & my_numbers

    if len(wins) > 0:
        points = 2 ** (len(wins) - 1)
        all_points.append(points)

    print(wins, points)

print(sum(all_points))
