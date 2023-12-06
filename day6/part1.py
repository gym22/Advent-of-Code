import math

inputs = [[60,475],[94,2138],[78,1015],[82,1650]]
outputs = []
for T,D in inputs:
    halfT = T/2
    sq = math.sqrt(T**2-4*D)/2

    lower = math.floor(halfT - sq)
    upper = math.floor(halfT + sq)
    range = upper - lower
    outputs.append(range)
    print(range)

print(math.prod(outputs))