with open('input.txt') as f:
    lines = f.readlines()

# ENEMY
# A = ROCK -> score = 1
# B = PAPER -> score = 2
# C = SCISSORS -> score = 3

# HOW THE ROUND MUST END
# Z = WIN -> score = 6
# Y = DRAW -> score = 3
# X = LOSS -> score = 0

def rockPaperScissor(opponent, endRound):
    score = 0
    # if he choose rock
    if opponent == "A":
        if endRound == "X": #loss
            score += 3
        elif endRound == "Y": #draw
            score += 4
        elif endRound == "Z": #win
            score += 8

    # if he choose paper     
    elif opponent == "B":
        if endRound == "X": #loss
            score += 1
        elif endRound == "Y": #draw
            score += 5
        elif endRound == "Z": #win
            score += 9

    # if he choose scissor
    else:
        if endRound == "X": #loss
            score += 2
        elif endRound == "Y": #draw
            score += 6
        elif endRound == "Z": #win
            score += 7
    return score
count = 0
for line in lines:
    round = line.split()
    count += rockPaperScissor(round[0], round[1])
print(count)