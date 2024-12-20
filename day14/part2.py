import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()

SECONDS = 999999999999999999
WIDTH = 101
HEIGHT = 103

guards = []
for guard in lines:
    location = re.findall(r'(?<=p\=)(\d+),(\d+)', guard)[0]
    location = (int(location[0]), int(location[1]))
    velocity = re.findall(r'(?<=v\=)(-?\d+),(-?\d+)', guard)[0]
    velocity = (int(velocity[0]), int(velocity[1]))
    guards.append((location, velocity))

def move(SECONDS):
    return [((guard[0][0] + guard[1][0] * SECONDS) % WIDTH, (guard[0][1] + guard[1][1] * SECONDS) % HEIGHT) for guard in guards]

def print_board(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in grid:
                print('█', end='')
            else:
                print('.', end='')
        print('\n', end='')
    print()

def cluster_score(grid):
    score = 0
    origin = (WIDTH//2, HEIGHT//2)
    for guard in grid:
        score += ((origin[0] - guard[0])**2 + (origin[1] - guard[1])**2)**.5
    return score

for second in range(SECONDS):
    grid = move(second)
    score = cluster_score(grid)
    if cluster_score(grid) < 15000:
        print_board(grid)
        print(second)