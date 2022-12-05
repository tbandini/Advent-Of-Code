with open('input.txt') as f:
    lines = f.readlines()
    last_line = lines[-1]

def ascii_convert(letter): # converto il valore in ascii e sottraggo la differenza
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def string_overlap(list):
    if list[0] <= list[1] and list[0] <= list[2]:
        return search(list[0], list[1], list[2])
    elif list[1] <= list[0] and list[1] <= list[2]:
        return search(list[1], list[0], list[2])
    elif list[2] <= list[0] and list[2] <= list[1]:
        return search(list[2], list[0], list[1])

def search(shortest, other1, other2):
    for letter in shortest:
        if letter in other1 and letter in other2:
            print(letter)
            return letter

total = 0
rucksucks = []

for index, line in enumerate(lines, 0):
    line = line.lstrip()
    if index % 3 == 0 and index != 0: 
        rucksucks.append(line)
        common_value = string_overlap(rucksucks)
        total += ascii_convert(common_value)
        rucksucks.clear()
    else:
        rucksucks.append(line)
    print(line)

print(total)
