with open('src.txt', "r") as f:
    lines = f.read().splitlines()

trailheads = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '0':
            trailheads.append((row, col))

scores = []
for trailhead in trailheads:
    stack = [trailhead]
    score = 0
    while stack:
        pos = stack.pop()
        height = lines[pos[0]][pos[1]]
        if height == '9':
            score += 1
        else:
            if pos[0] + 1 < len(lines) and int(height) + 1 == int(lines[pos[0] + 1][pos[1]]):
                stack.append((pos[0] + 1, pos[1]))
            if pos[0] - 1 >= 0 and int(height) + 1 == int(lines[pos[0] - 1][pos[1]]):
                stack.append((pos[0] - 1, pos[1]))
            if pos[1] + 1 < len(lines[0]) and int(height) + 1 == int(lines[pos[0]][pos[1] + 1]):
                stack.append((pos[0], pos[1] + 1))
            if pos[1] - 1 >= 0 and int(height) + 1 == int(lines[pos[0]][pos[1] - 1]):
                stack.append((pos[0], pos[1] - 1))
    scores.append(score)

print(sum(scores))