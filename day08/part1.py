with open('src.txt', "r") as f:
    lines = f.read().splitlines()

def distances(antennas, pos):
    dist = []
    for antenna in antennas:
        if pos[0] - antenna[0] != 0 and pos[1] - antenna[1] != 0:
            dist.append((pos[0] - antenna[0], pos[1] - antenna[1]))
    return dist

antennas = {}
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] != '.':
            if lines[row][col] in antennas:
                antennas[lines[row][col]].append((row, col))
            else:
                antennas[lines[row][col]] = [(row, col)]

antinodes = set()
for freq, positions in antennas.items():
    n = len(positions)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            
            dx, dy = x2 - x1, y2 - y1
            
            x3, y3 = x1 - dx, y1 - dy
            if 0 <= x3 < len(lines) and 0 <= y3 < len(lines[0]):
                antinodes.add((x3, y3))
            
            x4, y4 = x2 + dx, y2 + dy
            if 0 <= x4 < len(lines) and 0 <= y4 < len(lines[0]):
                antinodes.add((x4, y4))

print(len(antinodes))