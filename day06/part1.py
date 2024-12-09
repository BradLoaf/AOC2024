with open('src.txt', "r") as f:
    lines = f.read().splitlines()
pos = (0, 0)
visited = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '^':
            pos = (row, col)
dx = 0
dy = -1
while True:
    try:
        while lines[pos[0] + dy][pos[1] + dx] != '#':
            visited.add(pos)
            pos = (pos[0] + dy, pos[1] + dx)
        if dy == -1:
            dy, dx = 0, 1
        elif dx == 1:
            dy, dx = 1, 0
        elif dy == 1:
            dy, dx = 0, -1
        else:
            dy, dx = -1, 0
    except:
        print(len(visited) + 1)
        break