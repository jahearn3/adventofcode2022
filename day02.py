# Rock Paper Scissors

# 1st column: what opponent plays
# A Rock
# B Paper
# C Scissors

# 2nd column: what I should play in response
# X Rock --> 1 point
# Y Paper --> 2 pts
# Z Scissors --> 3 pts

# Win --> 6 pts
# Draw --> 3 pts
# Loss --> 0 pts

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def score_by_outcome(opp, you):
    add_to_score = 0
    if(opp == 'A'): # opponent chooses rock
        if(you == 'X'): # you choose rock
            add_to_score = 3
        elif(you == 'Y'): # you choose paper
            add_to_score = 6
        # nothing happens if you choose scissors (add zero)
    elif(opp == 'B'): # opponent chooses paper
        if(you == 'Y'): # you choose paper
            add_to_score = 3
        elif(you == 'Z'): # you choose scissors
            add_to_score = 6
    elif(opp == 'C'): # opponent chooses scissors
        if(you == 'Z'): # you choose scissors
            add_to_score = 3
        elif(you == 'X'): # you choose rock
            add_to_score = 6
    return add_to_score 



def calculate_score(data):
    score = 0
    for line in data:
        opp = line[0]
        you = line[2]
        # points based on player's choice
        if(you == 'X'):
            score += 1
            score += score_by_outcome(opp, you)
        elif(you == 'Y'):
            score += 2
            score += score_by_outcome(opp, you)
        elif(you == 'Z'):
            score += 3
            score += score_by_outcome(opp, you)
    return score

data = load_data('day02example1.txt')
score = calculate_score(data)
print(f'Example: {score}')

data = load_data('input02.txt')
score = calculate_score(data)
print(f'Part 1: {score}') # 13221 was the answer

# Part 2
def fix_outcomes(data):
    score = 0
    for line in data:
        opp = line[0]
        outcome = line[2]
        if(outcome == 'X'):
            score += choose(opp, outcome)
        elif(outcome == 'Y'):
            score += 3
            score += choose(opp, outcome)
        elif(outcome == 'Z'):
            score += 6
            score += choose(opp, outcome)
    return score

def choose(opp, outcome):
    add_to_score = 0
    if(((opp == 'A') and (outcome == 'Y')) or ((opp == 'B') and (outcome == 'X')) or ((opp == 'C') and (outcome == 'Z'))):
        add_to_score = 1 # you choose rock
    elif(((opp == 'A') and (outcome == 'Z')) or ((opp == 'B') and (outcome == 'Y')) or ((opp == 'C') and (outcome == 'X'))):
        add_to_score = 2 # you choose paper
    elif(((opp == 'A') and (outcome == 'X')) or ((opp == 'B') and (outcome == 'Z')) or ((opp == 'C') and (outcome == 'Y'))):
        add_to_score = 3 # you choose scissors
    return add_to_score

score = fix_outcomes(data)
print(f'Part 2: {score}') # 13131 was the answer


