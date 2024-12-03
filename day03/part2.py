import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()

count = 0
on = True

for line in lines:
    instructions = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line)
    print(instructions)
    for instruction in instructions:
        exp, num1, num2 = instruction
        if exp.startswith('mul(') and on:
            count += (int(num1) * int(num2))
        elif exp == "don't()":
            on = False
        elif exp == 'do()':
            on = True

print(count)