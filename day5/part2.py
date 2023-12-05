import re


def load_seeds():
    seedline = file.readline()
    seediterator = re.finditer(r"(\d+) (\d+)", seedline)
    seeds = []
    for s in seediterator:
        seeds.append({"id": int(int(s.group(1))), "range": int(int(s.group(2)))})
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
                dict(dst=int(mapline.split(" ")[0]), src=int(mapline.split(" ")[1]), lng=int(mapline.split(" ")[2])))
    return maps


with open("input.txt") as file:
    seeds = load_seeds()
    maps = load_maps()

for seed in seeds:
    for nextid in range(seed['id'], seed['id'] + seed['range']):
        seed['nextid'] = nextid
        for mapentry in maps:
            for mapvalues in maps[mapentry]:
                #print(mapvalues)
                if mapvalues["src"] <= seed["nextid"] < mapvalues["src"] + mapvalues["lng"]:
                    #print("using this map:", mapvalues, seed["nextid"] < mapvalues["src"] + mapvalues["lng"])
                    seed[mapentry] = mapvalues["dst"] + seed["nextid"] - mapvalues["src"]
                    seed["nextid"] = mapvalues["dst"] + seed["nextid"] - mapvalues["src"]
                    break
            if mapentry not in seed:
                    seed[mapentry] = seed["nextid"]
                    # seed["nextid"] stays the same
        #print(seed)
        if ("lowestid" not in seed or seed["nextid"] < seed["lowestid"]):
            seed["lowestid"] = seed["nextid"]

#print(seeds)
#print(maps)

print(min([x['lowestid'] for x in seeds]))
# 6227972
