with open('src.txt', "r") as f:
    lines = f.read().splitlines()

def safe(line):
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
    return less or more

def remove(line):
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        if safe(modified_line):
            return True
    return False

count = 0

for line in lines:
    line = [int(num) for num in line.split()]
    if remove(line):
        count += 1

print(count)