def acohash(s):
    current_value = 0
    for c in s:
        current_value = (ord(c) + current_value) * 17 % 256
    return current_value


steps = open('input.txt').read().strip().split(',')
boxes = {x: {} for x in range(256)}

for step in steps:
    if "=" in step:
        label, focal_length = step.split('=')
        boxid = acohash(label)
        boxes[boxid][label] = int(focal_length)
    else:
        label = step[:-1]
        boxid = acohash(label)
        boxes[boxid].pop(label, None)

focusing_power = 0
for boxid in boxes:
    for slot, lensid in enumerate(boxes[boxid], 1):
        focusing_power += (boxid + 1) * slot * boxes[boxid][lensid]

print(focusing_power)
