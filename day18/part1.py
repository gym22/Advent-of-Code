instructions = open('input.txt').read().splitlines()

movements = {
    "R": (0, 1,),
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1)
}

maxx = 0
maxy = 0
miny = 9999
minx = 9999


def dig(y, x, test):
    global minx, maxx, miny, maxy
    for inst in instructions:
        dir, steps, color = inst.split(" ")
        steps = int(steps)
        #  print(dir, steps, color)
        if not test and dir in "UD":
             floormap[y][x] = dir
        for _ in range(steps):
            y += movements[dir][0]
            x += movements[dir][1]

            if x < 0 or y < 0:
                print("PANIK")
            if test:
                minx = min(x, minx)
                maxx = max(x, maxx)
                miny = min(y, miny)
                maxy = max(y, maxy)
            else:
                floormap[y][x] = dir


dig(0, 0, True)
print(miny, minx, maxy, maxx)

floorsizex = maxx - minx + 1
floorsizey = maxy - miny + 1

fl = "." * (floorsizex+2)
floormap = []
for _ in range(floorsizey+2):
    floormap.append(list(fl))

floormap[-miny+1][-minx+1] = "#"

dig(-miny+1, -minx+1, False)

print('\n'.join([''.join(x) for x in [y for y in floormap]]))
print('------------------------------')
for y in range(1,floorsizey+1):
    trench = 0
    for x in range(1,floorsizex+1):
        if floormap[y][x] in "U":
            trench =1
        elif floormap[y][x] in "D":
            trench =0
        elif trench > 0:
            floormap[y][x] = "#"

print('\n'.join([''.join(x) for x in [y for y in floormap]]))

print(sum([x.count('#') + x.count('L') + x.count("R") + x.count("D") + x.count("U") for x in floormap]))
