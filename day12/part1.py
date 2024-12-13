with open('src.txt', "r") as f:
    lines = f.read().splitlines()

def perimiter(group):
    count = 0
    plant = lines[group[0][0]][group[0][1]]
    for cur in group:
        if cur[0] + 1 >= len(lines) or lines[cur[0] + 1][cur[1]] != plant:
            count += 1
        if cur[0] - 1 < 0 or lines[cur[0] - 1][cur[1]] != plant:
            count += 1
        if cur[1] + 1 >= len(lines[0]) or lines[cur[0]][cur[1] + 1] != plant:
            count += 1
        if cur[1] - 1 < 0 or lines[cur[0]][cur[1] - 1] != plant:
            count += 1
    return count

groups = {}
visited = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (row, col) not in visited:
            stack = [(row, col)]
            plant = lines[row][col]
            group = []
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    if cur[0] + 1 < len(lines) and (cur[0] + 1, cur[1]) and lines[cur[0] + 1][cur[1]] == plant:
                        stack.append((cur[0] + 1, cur[1]))
                    if cur[0] - 1 >= 0 and (cur[0] - 1, cur[1]) and lines[cur[0] - 1][cur[1]] == plant:
                        stack.append((cur[0] - 1, cur[1]))
                    if cur[1] + 1 < len(lines[0]) and (cur[0], cur[1] + 1) and lines[cur[0]][cur[1] + 1] == plant:
                        stack.append((cur[0], cur[1] + 1))
                    if cur[1] - 1 >= 0 and (cur[0], cur[1] - 1) and lines[cur[0]][cur[1] - 1] == plant:
                        stack.append((cur[0], cur[1] - 1))
                    visited.add(cur)
                    group.append(cur)
            if plant in groups:
                groups[plant].append(group)
            else:
                groups[plant] = [group]

cost = 0
for key, value in groups.items():
    for group in value:
        cost += len(group) * perimiter(group)

print(cost)