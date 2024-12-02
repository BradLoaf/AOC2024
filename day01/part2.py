with open('src.txt', "r") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    line = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))

count_dict = {}

for num in right:
    count_dict[num] = count_dict.get(num, 0) + 1

score = 0

for num in left:
    score += (num * count_dict.get(num, 0))

print(score)