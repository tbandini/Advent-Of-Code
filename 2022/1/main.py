with open('input.txt') as f:
    lines = f.readlines()

elvesCalories = [0] * 1000
i = 0
for line in lines:
    if line.strip():
        # if NOT blank
        elvesCalories[i] += int(line)
    else:
        #if blank
        i += 1
print(max(elvesCalories))