with open('input.txt') as f:
    lines = f.readlines()

numberExtracted = lines[0].split(",")
numberExtracted[-1] = numberExtracted[-1].replace("\n", "")

for val in numberExtracted:
    break
