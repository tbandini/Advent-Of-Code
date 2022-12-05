with open("input.txt") as f:
    lines = f.readlines()

fullycontained = 0
for line in lines:
    first_compartment = []
    second_compartment = []

    line = line.strip().split(",")
    elves1, elves2 = line[0].split("-"), line[1].split("-")

    for i in range(int(elves1[0]) - 1, int(elves1[1])):
        first_compartment.append(i + 1)
    
    for i in range(int(elves2[0]) - 1, int(elves2[1])):
        second_compartment.append(i + 1)
    
    count1 = 0
    count2 = 0

    for val in first_compartment:
        if val in second_compartment:
            count1 += 1
    for val in second_compartment:
        if val in first_compartment:
            count2 += 1
    
    if count1 == len(first_compartment) or count2 == len(second_compartment):
        fullycontained += 1
print(fullycontained)