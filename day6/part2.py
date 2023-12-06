import math

T = 60947882
D = 475213810151650
halfT = T/2
sq = math.sqrt(T**2-4*D)/2

lower = math.floor(halfT - sq)
upper = math.floor(halfT + sq)
range = upper - lower
print(range)