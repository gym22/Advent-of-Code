instructions = [x.split(" ") for x in open('input.txt').read().splitlines()]

movements = {
    "R": (0, 1,),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0)
}


def dig(maxy, test):
    x = 0
    y = 0
    area = 0
    for i in range(len(instructions)-1):
        inst = instructions[i]
        nextinst = instructions[i+1]
        previnst = instructions[i-1]

        dir, steps, color = inst
        nextdir, *_ = nextinst
        prevdir, *_ = previnst

        dy, dx = movements[dir]
        ndy, ndx = movements[nextdir]
        pdy, pdx = movements[prevdir]

        steps = int(steps)
        y += dy * steps
        x += dx * steps

        if not test and dx!=0: # trace outer edge
            if dx == 1:
                outeryedgelength = maxy - y + 1
            if dx == -1:
                outeryedgelength = maxy - y

            outerxedgelength = steps + 1
            if ndy == -dx:
                outerxedgelength -= 1
            if pdy == dx :
                outerxedgelength -= 1

            area += outeryedgelength*outerxedgelength*dx

        if test:
            maxy = max(y, maxy)
    return maxy if test else area


maxy = dig(0, True)
print(dig(maxy, False))
