with open('input.txt') as f:
    lines = f.readlines()

elvesCalories = [0] * 1000
topThreeCalories = 0
i = 0

for line in lines:
    new = 1
    if line.strip():
        # if NOT blank
        elvesCalories[i] += int(line)
    else:
        #if blank
        i += 1

for i in range(3):
    topThreeCalories += max(elvesCalories)
    max_index = elvesCalories.index(max(elvesCalories))
    del elvesCalories[max_index]
print(topThreeCalories)