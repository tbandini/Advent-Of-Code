with open('input.txt') as f:
    lines = f.readlines()

zeros = [0] * 12
ones = [0] * 12

archiveOX = []
tempArchiveOX = []
archiveCO = []
tempArchiveCO = []

for line in lines:
    i = 0
    archiveOX.append(line)
    archiveCO.append(line)
    for val in line:
        if val == '0':
            zeros[i] += 1
        elif val == '1':
            ones[i] += 1
        i += 1

print("ONES:  " + ' '.join(map(str, ones)))
print("ZEROS: " + ' '.join(map(str, zeros)))


for val in range(12):
    if ones[val] >= zeros[val]:
        eliminateOX = '0'
        eliminateCO = '1'
    elif ones[val] < zeros[val]:
        eliminateOX = '1'
        eliminateCO = '0'

    for t, line in enumerate(archiveCO):
        if len(archiveCO) < 2:
            print(len(archiveCO))
            CO = archiveCO[0]    
            break 
        if line[val] != eliminateCO: 
            tempArchiveCO.append(archiveCO.pop(t))

    for t, line in enumerate(archiveOX):
            if len(archiveOX) < 3:
                print("OX " + str(len(archiveOX)))
                OX = archiveOX[0]
                break
            if line[val] != eliminateOX: 
                tempArchiveOX.append(archiveOX.pop(t))

    archiveOX = tempArchiveOX 
    tempArchiveOX = []
    archiveCO = tempArchiveCO 
    tempArchiveCO = []

print("OX:" + OX)
print("CO:" + CO)
print(f"Life support rating: {int(OX, 2) * int(CO, 2)}")