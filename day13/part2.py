import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()

claws = []
for line in range(0, len(lines), 4):
    a = (int(re.findall(r'(?<=X\+)\d+', lines[line])[0]), int(re.findall('(?<=Y\+)\d+', lines[line])[0]))
    b = (int(re.findall(r'(?<=X\+)\d+', lines[line + 1])[0]), int(re.findall('(?<=Y\+)\d+', lines[line + 1])[0]))
    goal = (int(re.findall(r'(?<=X\=)\d+', lines[line + 2])[0]), int(re.findall('(?<=Y\=)\d+', lines[line + 2])[0]))
    goal = (goal[0] + 10000000000000, goal[1] + 10000000000000)
    claws.append((a, b, goal))

count = 0
for claw in claws:
    determinate = claw[0][0] * claw[1][1] - claw[0][1] * claw[1][0]
    da = claw[2][0] * claw[1][1] - claw[2][1] * claw[1][0]
    db = claw[0][0] * claw[2][1] - claw[0][1] * claw[2][0]
    a = da / determinate
    b = db / determinate
    if int(a) == a and int(b) == b:
        count += 3 * a + b

print(count)