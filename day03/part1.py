import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    mult = re.findall(r'mul\((\d+),(\d+)\)', line)
    for exp in mult:
        count += (int(exp[0]) * int(exp[1]))

print(count)