def check_loop(row, col, start, grid):
    if grid[row][col] == '#' or grid[row][col] == '^':
        return False
    grid[row][col] = '#'
    dx = 0
    dy = -1
    visited = set()

    while(True):
        while grid[start[0] + dy][start[1] + dx] != '#':
            if (start[0], start[1], dx, dy) in visited:
                grid[row][col] = '.'
                return True
            visited.add((start[0], start[1], dx, dy))
            start = (start[0] + dy, start[1] + dx)
            if start[0] + dy >= len(grid) or start[0] + dy < 0 or start[1] + dx >= len(grid[0]) or start[1] + dx < 0:
                grid[row][col] = '.'
                return False
        if dy == -1:
            dy, dx = 0, 1
        elif dx == 1:
            dy, dx = 1, 0
        elif dy == 1:
            dy, dx = 0, -1
        else:
            dy, dx = -1, 0

def locations(start, grid):
    dx = 0
    dy = -1
    visited = set()

    while(True):
        while grid[start[0] + dy][start[1] + dx] != '#':
            start = (start[0] + dy, start[1] + dx)
            visited.add((start[0], start[1]))
            if start[0] + dy >= len(grid) or start[0] + dy < 0 or start[1] + dx >= len(grid[0]) or start[1] + dx < 0:
                grid[row][col] = '.'
                return visited
        if dy == -1:
            dy, dx = 0, 1
        elif dx == 1:
            dy, dx = 1, 0
        elif dy == 1:
            dy, dx = 0, -1
        else:
            dy, dx = -1, 0

with open('src.txt', "r") as f:
    lines = [list(line) for line in f.read().splitlines()]

pos = (0, 0)
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '^':
            lines[row][col] = '.'
            pos = (row, col)
locs = locations(pos, lines)

count = 0

for progress, loc in enumerate(locs):
    if check_loop(loc[0], loc[1], pos, lines):
        count += 1

print(count)