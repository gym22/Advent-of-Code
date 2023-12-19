import re


def parse():
    w, p = open('input.txt').read().split("\n\n")
    for wf in w.split('\n'):
        wfid, instr = wf.split("{")
        wfs[wfid] = instr[:-1].split(",")

    for pa in p.split('\n'):
        part = [int(re.sub(r".=", "", x)) for x in pa[1:-1].split(',')]
        parts.append({"x": part[0], "m": part[1], "a": part[2], "s": part[3]})


wfs = {}
parts = []
parse()

totals = []
for part in parts:
    wf = 'in'
    while wf not in "AR":
        for rule in wfs[wf]:
            if "<" not in rule and ">" not in rule:
                wf = rule
                break

            rtype, rating, nextwf = re.split('[:><]', rule)
            rating = int(rating)
            if ">" in rule:
                if part[rtype] > rating:
                    wf = nextwf
                    break
            if "<" in rule:
                if part[rtype] < rating:
                    wf = nextwf
                    break
    if wf == "A":
        totals.append(sum([part[rtype] for rtype in list("xmas")]))

print(sum(totals))
