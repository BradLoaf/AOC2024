with open('src.txt', "r") as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    line = [int(num) for num in line.split()]
    less = True
    more = True
    for num in range(1, len(line)):
        if abs(line[num-1] - line[num]) <= 3:
            if line[num-1] <= line[num]:
                less = False
            if line[num-1] >= line[num]:
                more = False
        else:
            less, more = False, False
    if less or more:
        count += 1

print(count)