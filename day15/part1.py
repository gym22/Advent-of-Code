def acohash(s):
    current_value = 0
    for c in s:
        current_value = (ord(c) + current_value) * 17 % 256
    return current_value

print(sum(map(acohash, open('input.txt').read().strip().split(','))))