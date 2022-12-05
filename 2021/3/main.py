with open('input.txt') as f:
    lines = f.readlines()

gammaR = ""
epsilonR = ""

zeros = [0] * 12
ones = [0] * 12

for line in lines:
    i = 0
    for val in line:
        if val == '0':
            zeros[i] += 1
        elif val == '1' :
            ones[i] += 1
        i += 1

print("ONES:  " + ' '.join(map(str, ones)))
print("ZEROS: " + ' '.join(map(str, zeros)))

i = 0
for val in range(12):
    if ones[i] > zeros[i]:
        gammaR += "1"
        epsilonR += "0"
    else:
        gammaR += "0"
        epsilonR += "1"
    i += 1

print("Gamma rate: " + gammaR)
print("Epsilon rate: " + epsilonR)

# Trasformo Gamma rate e Epsilon rate in decimali e li moltiplico
print("Power consumption: " + str(int(gammaR, 2) * int(epsilonR, 2)))