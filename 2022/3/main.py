with open('input.txt') as f:
    lines = f.readlines()

def ascii_convert(letter): # converto il valore in ascii e sottraggo la differenza
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

total = 0

for line in lines:
    if line != lines[-1]: # se non siamo arrivati all'ultmia riga devo rimuovere "\n"
        firstHalf, secondHalf = line[:len(line[:-1])//2], line[len(line[:-1])//2:]
    else: # se invece ci siamo arrivati allora non è piu necessario
        firstHalf, secondHalf = line[:len(line)//2], line[len(line)//2:]
    # cerco il valore uguale tra le due half
    common_value = [letter for letter in firstHalf if letter in secondHalf]
    total += ascii_convert(common_value[0])

print(total)
