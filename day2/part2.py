def is_game_possible(input_line):
    a = input_line.split(": ")
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
    return cubes["red"] * cubes["green"] * cubes["blue"]


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        num = is_game_possible(line.strip())
        print(num)
        total_sum += num

print(f"Total Sum: {total_sum}")
