with open('src.txt', "r") as f:
    line = f.read()

stones = [int(stone) for stone in line.split()]
transformations = {}

def blink(stone, blinks):
    if blinks == 75:
        return 1
    
    if (stone, blinks) in transformations:
        return transformations[(stone, blinks)]
    
    stone_str = str(stone)
    stone_len = len(stone_str)
    
    if stone == 0:
        result = blink(1, blinks+1)
    elif stone >= 10 and stone_len % 2 == 0:
        half_len = stone_len // 2
        left = int(stone_str[:half_len])
        right = int(stone_str[half_len:])
        result = blink(left, blinks + 1) + blink(right, blinks + 1)
    else:
        result = blink(stone * 2024, blinks + 1)
    transformations[(stone, blinks)] = result
    return result

all_stones = 0
for stone in stones:
    all_stones += blink(stone, 0)
print(all_stones)