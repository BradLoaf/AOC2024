with open('src.txt', "r") as f:
    lines = f.read().splitlines()

lines = [(int(line[0]), list(map(int, line[1].split()))) for line in (line.split(':') for line in lines)]

def permutations(n):
    if n == 0:
        return ['']
    else:
        prev_permutations = permutations(n-1)
        return ['0' + perm for perm in prev_permutations] + ['1' + perm for perm in prev_permutations]

sum = 0
for line in lines:
    goal = line[0]
    nums = line[1]
    permutation = permutations(len(nums) - 1)
    for perm in permutation:
        count = nums[0]
        for index, op in enumerate(perm):
            if op == '0':
                count += nums[index + 1]
            else:
                count *= nums[index + 1]
        if count == goal:
            sum += goal
            break

print(sum)