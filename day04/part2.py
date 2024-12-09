with open('src.txt', "r") as f:
    lines = f.read().splitlines()

count = 0

for row in range(len(lines)-2):
    for col in range(len(lines[0])-2):
        if (all(lines[row + x][col + x] == 'MAS'[x] for x in range(3)) or all(lines[row + x][col + x] == 'SAM'[x] for x in range(3))) and (all(lines[row + x][col + 2 - x] == 'MAS'[x] for x in range(3)) or all(lines[row + x][col + 2 - x] == 'SAM'[x] for x in range(3))):
            count += 1

print(count)