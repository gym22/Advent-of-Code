def is_game_possible(input_line, test_cubes):
    a = input_line.split(": ")
    b = a[0].split(" ")
    game_id = int(b[1])
    game = a[1]

    subgames = game.split("; ")

    cubes = {"red": 0, "green": 0, "blue": 0}

    for subgame in subgames:
        subgame_cubes = subgame.split(", ")
        for subgame_cube in subgame_cubes:
            c = subgame_cube.split(" ")
            cube_color = c[1]
            no_of_cubes = int(c[0])
            if cubes[cube_color] < no_of_cubes:
                cubes[cube_color] = no_of_cubes

    print(cubes)
    if cubes["red"] > test_cubes["red"] or cubes["green"] > test_cubes["green"] or cubes["blue"] > test_cubes["blue"]:
        return 0
    else:
        return game_id


total_sum = 0
with open('day2input1.txt', 'r') as file:
    for line in file:
        num = is_game_possible(line.strip(), {"red": 12, "green": 13, "blue": 14})
        print(num)
        total_sum += num

print(f"Total Sum: {total_sum}")

# 2476
