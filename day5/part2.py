import re


def load_seeds():
    seedline = file.readline()
    seediterator = re.finditer(r"(\d+) (\d+)", seedline)
    seeds = []
    for s in seediterator:
        seeds.append({"start": int(int(s.group(1))), "end": int(int(s.group(2))) + int(int(s.group(1))) - 1})
    _ = file.readline()
    return seeds


def load_maps():
    maps = {}
    currentmap = ""
    for line in file:
        mapline = line.strip()

        if re.search(r":", mapline) is not None:
            currentmap = mapline.split(":")[0]
            maps[currentmap] = []
        elif mapline != "":
            maps[currentmap].append(
                {'dst': int(mapline.split(" ")[0]), 'start': int(mapline.split(" ")[1]),
                 'end': (int(mapline.split(" ")[2]) + int(mapline.split(" ")[1])) - 1})
    return maps


with open("input.txt") as file:
    seeds = load_seeds()
    maps = load_maps()


for mapentry in maps:
    dst = []
    while len(seeds) > 0:
        seed = seeds.pop()
        seedstart = seed["start"]
        seedend = seed["end"]
#        print("seed", seed)

        found = False
        for mapvalues in maps[mapentry]:
#            print(mapentry, mapvalues)
            rangestart = mapvalues["start"]
            rangeend = mapvalues["end"]

            if rangestart <= seedend and rangeend >= seedstart:
                nextstart = mapvalues["dst"] + seedstart - rangestart
                nextend = nextstart + seed["end"] - seed["start"]
                if seedstart < rangestart:  # shorten start and split
                    seeds.append({"start": seedstart, "end": rangestart - 1})
                    nextstart += rangestart - seedstart

                if seedend > rangeend:  # shorten end and split
                    seeds.append({"start": rangeend + 1, "end": seedend})
                    nextend -= seedend - rangeend
                dst.append({"start": nextstart, "end": nextend})
                found = True
                break
        if not found:
            dst.append({"start": seed["start"], "end": seed["end"]})
    print(mapentry, len(dst))
#        print(nextstart, seeds, dst)
    seeds = dst


# print(seeds)
# print(maps)

print(min([x['start'] for x in seeds]))
