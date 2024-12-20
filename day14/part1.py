import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()

SECONDS = 100
WIDTH = 101
HEIGHT = 103

guards = []
for guard in lines:
    location = re.findall(r'(?<=p\=)(\d+),(\d+)', guard)[0]
    location = (int(location[0]), int(location[1]))
    velocity = re.findall(r'(?<=v\=)(-?\d+),(-?\d+)', guard)[0]
    velocity = (int(velocity[0]), int(velocity[1]))
    guards.append((location, velocity))

new_locations = [((guard[0][0] + guard[1][0] * SECONDS) % WIDTH, (guard[0][1] + guard[1][1] * SECONDS) % HEIGHT) for guard in guards]

quad = [0, 0, 0, 0]
for x in range(0, WIDTH//2):
    for y in range(0, HEIGHT//2):
        if (x, y) in new_locations:
            quad[0] += new_locations.count((x, y))

for x in range(WIDTH//2 + 1, WIDTH):
    for y in range(0, HEIGHT//2):
        if (x, y) in new_locations:
            quad[1] += new_locations.count((x, y))

for x in range(0, WIDTH//2):
    for y in range(HEIGHT//2 + 1, HEIGHT):
        if (x, y) in new_locations:
            quad[2] += new_locations.count((x, y))

for x in range(WIDTH//2 + 1, WIDTH):
    for y in range(HEIGHT//2 + 1, HEIGHT):
        if (x, y) in new_locations:
            quad[3] += new_locations.count((x, y))
            
print(quad[0] * quad[1] * quad[2] * quad[3])