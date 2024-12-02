with open('src.txt', "r") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    line = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

count = 0

for x in range(len(left)):
    count += abs(left[x] - right[x])

print(count)