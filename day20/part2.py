import math


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


def find_interesting_modules():
    cons = [x for x in modules if modules[x]["type"] == "&"]
    for con in cons:
        all_inputs_are_flips = True
        for ref in modules[con]["state"]:
            if modules[ref]['type'] == "&":
                all_inputs_are_flips = False
        if all_inputs_are_flips:
            interesting_modules.append(con)


def push(n):
    q = [('roadcaster', "low", "button")]
    while q:
        moduleid, pulse, lastmodule = q.pop(0)

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
            if (moduleid not in cycles and newpulse == "low" and moduleid in interesting_modules):
                print(f"{moduleid} cycle length", n)
                cycles[moduleid] = n

        for nextid in module["nextmodules"]:
            q.append((nextid, newpulse, moduleid))


interesting_modules = []
modules = {}
parse()
find_references()
find_interesting_modules()
cycles = {}

n = 1
while len(cycles) < 4:
    push(n)
    n += 1

print(math.lcm(*cycles.values()))
