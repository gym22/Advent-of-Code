readings = []
alldiffs = []
with open("input.txt") as file:
    for line in file:
        readings.append([int(x) for x in line.strip().split(" ")])

for line in readings:
    differences = [line]
    newdiffs = line
#    print("line", line)
    while newdiffs.count(0) != len(newdiffs):
        newdiffs = [newdiffs[x+1] - newdiffs[x] for x in range(0,len(newdiffs)-1)]
#        print(newdiffs)
        differences.insert(0, newdiffs)

    thisdiff = 0
    for diff in differences:
        thisdiff += diff[-1]
#        print(thisdiff)
    alldiffs.append(thisdiff)

print(sum(alldiffs), alldiffs)