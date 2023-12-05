import re

# Function to read the file, apply regex to each line, and store results in an array
result_array = []
total_sum = 0
with open('day1input1.txt', 'r') as file:
    for line in file:
        firstdigit = re.search(r'(\d)', line)
        lastdigit = re.search(r'.*(\d)', line)
        num = int(firstdigit.group(1) + lastdigit.group(1))
        total_sum += num
print(f"Total Sum: {total_sum}")

# 54573
