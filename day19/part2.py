import math
import re


def parse():
    w, _ = open('input.txt').read().split("\n\n")
    for wf in w.split('\n'):
        wfid, instr = wf.split("{")
        wfs[wfid] = instr[:-1].split(",")


wfs = {}
ranges = []
parse()

combinations = []
q = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]

while q:
    wf, ranges = q.pop()

    if wf == "A":
        combinations.append((wf, ranges))
        continue

    if wf == "R":
        continue

    for rule in wfs[wf]:
        if "<" not in rule and ">" not in rule:
            wf = rule
            q.append((wf, ranges))
            continue

        rtype, rating, nextwf = re.split('[:><]', rule)
        rating = int(rating)

        newranges = ranges.copy()
        if ">" in rule and ranges[rtype][1] > rating:
            newranges[rtype] = (max(ranges[rtype][0], rating + 1), ranges[rtype][1])
            ranges[rtype] = (ranges[rtype][0], max(ranges[rtype][0], rating))

        if "<" in rule and ranges[rtype][0] < rating:
            newranges[rtype] = (ranges[rtype][0], min(ranges[rtype][1], rating - 1))
            ranges[rtype] = (min(ranges[rtype][1], rating), ranges[rtype][1])

        q.append((nextwf, newranges))

tot = sum([math.prod([rting[1][x][1] - rting[1][x][0] + 1 for x in list("xmas")]) for rting in combinations])

print(tot)
