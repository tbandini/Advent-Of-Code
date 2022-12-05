with open('input.txt') as f:
    lines = f.readlines()

# A, X = ROCK -> score = 1
# B, Y = PAPER -> score = 2
# C, Z = SCISSORS -> score = 3

# WIN -> score = 6
# DRAW -> score = 3
# LOSS -> score = 0

score = 0
count = 0

for line in lines:
    round = line.split()

     # if he choose rock 
    if round[0] == "A":
        if round[1] == "X": #rock
            score += 4
        elif round[1] == "Y": #paper
            score += 8
        elif round[1] == "Z": #scissor
            score += 3

    # if he choose paper     
    elif round[0] == "B":
        if round[1] == "X": #rock
            score += 1
        elif round[1] == "Y": #paper
            score += 5
        elif round[1] == "Z": #scissor
            score += 9

    # if he choose scissor
    else:
        if round[1] == "X": #rock
            score += 7
        elif round[1] == "Y": #paper
            score += 2
        elif round[1] == "Z": #scissor
            score += 6
    
print(score)
