import math

inputs = [[60,475],[94,2138],[78,1015],[82,1650]]
outputs = []
for T,D in inputs:
    range = round(math.sqrt(T ** 2 - 4 * D))
    outputs.append(range)
    print(range)

print(math.prod(outputs))