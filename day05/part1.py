with open('src.txt', "r") as f:
    lines = f.read().splitlines()

before = []
updates = []
update = False
for line in lines:
    if line == '':
        update = True
    else:
        before.append(line) if not update else updates.append(line)

rules = {}
for line in before:
    first, second = line.split('|')
    if first in rules:
        rules[first].append(second)
    else:
        rules[first] = [second]

count = 0

for line in updates:
    pages = []
    fail = False
    for page in line.split(','):
        pages.append(page)
        for rule in rules.get(page, []):
            if rule in pages:
                fail = True
    if not fail:
        count += int(line.split(',')[len(line.split(',')) // 2])

print(count)