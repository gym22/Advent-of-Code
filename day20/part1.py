def parse():
    for line in open('input.txt'):
        id, next = line.strip().split(" -> ")
        nextlist = next.split(', ')
        if id[0] == '%':
            state = 'off'
        else:
            state = {}
        modules[id[1:]] = {"type": id[0], "state": state, "nextmodules": nextlist}


def find_references():
    cons = [x for x in modules if modules[x]["type"] == "&"]
    for con in cons:
        references = [x for x in modules if modules[x]["nextmodules"].count(con) > 0]
        modules[con]["state"] = {x: "low" for x in references}


def push():
    lows = 0
    highs = 0
    q = [('roadcaster', "low", "button")]
    while q:
        # print(list(reversed(q[0])))
        moduleid, pulse, lastmodule = q.pop(0)
        if pulse == "low":
            lows += 1
        else:
            highs += 1

        if moduleid not in modules:
            continue

        module = modules[moduleid]

        if module["type"] == "b":
            newpulse = "low"

        if module["type"] == "%":
            if pulse == "high":
                continue
            newpulse = "high" if module["state"] == "off" else "low"
            module["state"] = "on" if module["state"] == "off" else "off"

        if module["type"] == "&":
            module["state"][lastmodule] = pulse
            newpulse = "low" if list(module["state"].values()).count("low") == 0 else "high"

        for nextid in module["nextmodules"]:
            q.append((nextid, newpulse, moduleid))

    return lows, highs


modules = {}
parse()
find_references()

ls = 0
hs = 0

for _ in range(1000):
    l, h = push()
    ls += l
    hs += h

print(ls, hs, ls*hs)
