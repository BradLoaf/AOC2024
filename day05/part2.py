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

def valid_line(line):
    pages = []
    for page in line:
        pages.append(page)
        for rule in rules.get(page, []):
            if rule in pages:
                return False
    return True

def fix_line(line):
    while not valid_line(line):
        pages = []
        for page in line:
            pages.append(page)
            for rule in rules.get(page, []):
                if rule in pages:
                    pages.remove(page)
                    pages = pages[:pages.index(rule)] + [page] + pages[pages.index(rule):]
        line = pages
    return int(pages[len(pages)//2])

count = 0

for line in updates:
    if not valid_line(line.split(',')):
        count += fix_line(line.split(','))

print(count)