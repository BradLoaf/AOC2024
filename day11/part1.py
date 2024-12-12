with open('src.txt', "r") as f:
    line = f.read()

stones = [int(stone) for stone in line.split()]

transformations = {0: [1]}
for _ in range(25):
    new_stones = []
    for stone in stones:
        if transformations.get(stone, False):
            new_stones += transformations[stone]
        else:
            if stone >= 10 and len(str(stone)) % 2 == 0:
                left = int(str(stone)[:len(str(stone))//2])
                right = int(str(stone)[len(str(stone))//2:])
                new_stones.append(left)
                new_stones.append(right)
                transformations[stone] = [left, right]
            else:
                new_stones.append(stone * 2024)
                transformations[stone] = [stone * 2024]
    stones = new_stones
print(len(stones))