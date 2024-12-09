with open('src.txt', "r") as f:
    grid = f.read().splitlines()

directions = [ (0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1) ]

def search_word(x, y, dx, dy):
    for i in range(4):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != 'XMAS'[i]:
            return False
    return True

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        for dx, dy in directions:
            if search_word(x, y, dx, dy):
                count += 1

print(count)