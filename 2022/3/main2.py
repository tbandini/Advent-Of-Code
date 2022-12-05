with open('input.txt') as f:
    lines = f.readlines()
    last_line = lines[-1]

def ascii_convert(letter): # converto il valore in ascii e sottraggo la differenza
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def string_overlap(first, second, third):
    if len(first) <= len(second) and len(first) <= len(third):
        return search(first, second, third)
    elif len(second) <= len(first) and len(second) <= len(third):
        return search(second, first, third)
    elif len(third) <= len(first) and len(third) <= len(second):
        return search(third, first, second)

def search(shortest, other1, other2):
    for letter in shortest:
        if letter in other1 and letter in other2:
            return letter

total = 0
rucksucks = []

for i in range(0, len(lines), 3):
    first = lines[i].lstrip()
    second = lines[i+1].lstrip()
    third = lines[i+2].lstrip()
    common_letter = string_overlap(first, second, third)
    total += ascii_convert(common_letter)

print(total)
