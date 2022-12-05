with open('input.txt') as f:
    lines = f.readlines()

prev = ''
tot = 0

for line in lines:
    if prev == '':
        prev = line
        next
    if prev < line:
        tot += 1

    prev = line

print(tot)