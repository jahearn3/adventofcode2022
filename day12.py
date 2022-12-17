# Hill Climbing Algorithm

import load_data as ld 
import random 
from collections import deque 

def find_start_and_end(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j] == 'S'):
                start = [i, j]
                # data[i][j] = 'a'
                # print(f'start: ({i},{j})')
            elif(data[i][j] == 'E'):
                end = [i, j]
                # data[i][j] = 'z'
                # print(f'end: ({i},{j})')
    return start, end 

def get_score(option, path, data, cur_loc, cur_alt, end):
    score = 50
    path_weight = 20
    alt_weight  = 10
    goal_weight = 10
    x = cur_loc[0]
    y = cur_loc[1]
    delta_x = option[0] - cur_loc[0]
    delta_y = option[1] - cur_loc[1]
    opt_alt = data[x+delta_x][y+delta_y]
    # Test 1: alter score if it has or hasn't already gone that way
    if(option not in path): 
        score += path_weight
    else:
        score -= path_weight
    # Test 2: alter score based on change in altitude
    delta_alt = ord(opt_alt) - ord(cur_alt)
    score += (delta_alt * alt_weight)
    # Test 3: alter score based on proximity and direction of end
    cur2end_x = end[0] - cur_loc[0]
    cur2end_y = end[1] - cur_loc[1]
    opt2end_x = end[0] - option[0]
    opt2end_y = end[1] - option[1]
    if(opt2end_x < cur2end_x):
        score += goal_weight
    elif(opt2end_x > cur2end_x):
        score -= goal_weight
    if(opt2end_y < cur2end_y):
        score += goal_weight
    elif(opt2end_y > cur2end_y):
        score -= goal_weight
    # Test 4: alter the score based on looking further ahead
    # vision = 3
    # # figure out direction of option
    # if(delta_x < 0): # left
    #     # @.......
    #     # @@......
    #     # @@@.....
    #     # @@@@....
    #     # @@@OS...
    #     # @@@@....
    #     # @@@.....
    #     # @@......
    #     # @.......
    #     # S is cur_loc
    #     # O is option
    #     grads = []
    #     for i in range(vision + 1):
    #         for j in range(-i - 1, i + 1):
    #             if(i == 0):
    #                 prev_alt = opt_alt 
    #             elif(i == 1):
    #                 if(j == 0):
    #                     prev_alt = opt_alt 
    #                 elif((j == -1) or (j == 1)):
    #                     prev_alt = data[option[0]+i][option[1]]
    #                 elif(j == -2):
    #                     prev_alt = data[option[0]+i][option[1]+j+1]
    #             candidate_alt = get_candidate_alt(data[option[0]+i][option[1]+j])
    #             grads.append(abs(ord(candidate_alt) - ord(prev_alt)))


    # elif(delta_x > 0): # right
    # elif(delta_y < 0): # down
    # elif(delta_y > 0): # up
    # look further ahead in that direction, trying to include the whole cone in that direction

    # Include some more randomness in the score, 
    # Include a test that looks further ahead, 
    # Include a test to avoid pits by severely penalizing squares that belong to pits 
    return score

# Write a function that identifies pits, then prevent them from being options, 
# maybe by replacing their altitude and pretending they are walls
# could use chr() which is the opposite of ord()  
def identify_pits(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            # find maximum gradient of all 4 directions
            gradients = []
            cur_alt = get_candidate_alt(data[i][j])
            if(0 <= i - 1 <= len(data) - 1): # left
                candidate_alt = get_candidate_alt(data[i-1][j])
                gradients.append(abs(ord(candidate_alt) - ord(cur_alt)))
            if(0 <= i + 1 <= len(data) - 1): # right
                candidate_alt = get_candidate_alt(data[i+1][j])
                gradients.append(abs(ord(candidate_alt) - ord(cur_alt)))
            if(0 <= j - 1 <= len(data[0]) - 1): # down
                candidate_alt = get_candidate_alt(data[i][j-1])
                gradients.append(abs(ord(candidate_alt) - ord(cur_alt)))
            if(0 <= j + 1 <= len(data[0]) - 1): # up
                candidate_alt = get_candidate_alt(data[i][j+1])
                gradients.append(abs(ord(candidate_alt) - ord(cur_alt)))
            max_grad = max(gradients)
            # if(max_grad < 2):
            #     risk[i][j] = 0
            # else:
            #     risk[i][j] = max_grad 
    # see if there are closed loops of gradients of 2 or greater
    # print(ord('Ω'))
    return data 

def get_candidate_alt(datum):
    if(datum == 'E'):
        return 'z'
    elif(datum == 'S'):
        return 'a'
    else:
        return datum

def find_path(start, end, data):
    cur_loc = start
    cur_alt = 'a'
    path = []
    path_str = []
    options = []
    scores = []
    count = 0
    finished = False
    max_count = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5 * 20)
    # print(f'Max count: {max_count}')
    while(cur_loc != end):
        x = cur_loc[0]
        y = cur_loc[1]
        # evaluate up, down, left, right (if they exist)
        if(0 <= x - 1 <= len(data) - 1): # left
            candidate_alt = get_candidate_alt(data[x-1][y])
            if(ord(cur_alt) + 1 >= ord(candidate_alt)):
                options.append([x-1, y])
        if(0 <= x + 1 <= len(data) - 1): # right
            candidate_alt = get_candidate_alt(data[x+1][y])
            if(ord(cur_alt) + 1 >= ord(candidate_alt)):
                options.append([x+1, y])
        if(0 <= y - 1 <= len(data[0]) - 1): # down
            candidate_alt = get_candidate_alt(data[x][y-1])
            if(ord(cur_alt) + 1 >= ord(candidate_alt)):
                options.append([x, y-1])
        if(0 <= y + 1 <= len(data[0]) - 1): # up
            candidate_alt = get_candidate_alt(data[x][y+1])
            if(ord(cur_alt) + 1 >= ord(candidate_alt)):
                options.append([x, y+1])
        # print(options)
        
        if(end in options):
            cur_loc = end
            finished = True
        else:
            for o in range(len(options)):
                scores.append(get_score(options[o], path, data, cur_loc, cur_alt, end)) 
            
            if(len(options) == 1): # go back the way we came if it's a dead end
                cur_loc = options[0]
            elif(len(options) == 0):
                print('How did we get here?')
                cur_loc = end
            else:
                # find the best scores
                m = max(scores)
                idx_maxscore = scores.index(m)
                idx_best = [idx_maxscore]
                for s in range(len(scores)):
                    if(s != idx_maxscore):
                        if(scores[s] == scores[idx_maxscore]):
                            # print('Tied max score')
                            idx_best.append(s)
                if(len(idx_best) == 1): # choose the option with the sole best score
                    cur_loc = options[idx_best[0]]
                else: # randomly choose an option if there are multiple best scores
                    idx = random.randint(0, len(idx_best) - 1)
                    cur_loc = options[idx_best[idx]]
            
        path.append(cur_loc)
        path_str.append(str(cur_loc))
        cur_alt = data[cur_loc[0]][cur_loc[1]]
        # print(cur_loc, cur_alt)
        options.clear()
        scores.clear()
        count += 1
        if(count >= max_count):
            # print('Max count reached!')
            # print(cur_loc, cur_alt)
            break
        if(len(path_str) > 6):
            if(len(set(path_str)) < 0.1 * len(path_str)):
                # print('High length to set ratio!')
                # print(cur_loc, cur_alt)
                break 

    return path, finished 

def simulate_paths(start, end, data):
    N = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5 * 10)
    path_lengths = [999999]
    for i in range(N):
        path, finished = find_path(start, end, data)
        print(f'Simulation {i+1} took {len(path)} steps')
        if(finished):
            path_lengths.append(len(path))
            print('... and finished!')
        else:
            print('... but did not finish.')
    return min(path_lengths)

data = ld.load_data('day12example1.txt')
start, end = find_start_and_end(data)
print(f'Example: {simulate_paths(start, end, data)} (should be 31)')

data = ld.load_data('input12.txt')
start, end = find_start_and_end(data)
# print(f'Part 1: {simulate_paths(start, end, data)}') # 231 was too low

# Learning from hyper neutrino 
# breadth-first search 
def ascend(start, end, data):
    q = deque()
    q.append((0, start[0], start[1]))
    visited = {(start[0], start[1])}

    while(q):
        steps, x, y = q.popleft()
        for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]: # neighbors
            if((next_x < 0) or (next_x >= len(data)) or (next_y < 0) or (next_y >= len(data[0]))): # checking if that coordinate exists in the grid
                continue
            if((next_x, next_y) in visited): # checking if it's already been visited
                continue
            if((ord(get_candidate_alt(data[next_x][next_y])) - ord(get_candidate_alt(data[x][y]))) > 1): # checking if it's a cliff 
                continue
            if((next_x == end[0]) and (next_y == end[1])): # checking if it's the endpoint
                return(steps + 1)
            visited.add((next_x, next_y)) # adding to our set of visited coordinates
            q.append((steps + 1, next_x, next_y)) # adding to our deque
    return 0

print(f'Part 1: {ascend(start, end, data)}') # 497 was the answer

# Part 2
def descend(start, data):
    q = deque()
    q.append((0, start[0], start[1]))
    visited = {(start[0], start[1])}

    while(q):
        steps, x, y = q.popleft()
        for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]: # neighbors
            if((next_x < 0) or (next_x >= len(data)) or (next_y < 0) or (next_y >= len(data[0]))): # checking if that coordinate exists in the grid
                continue
            if((next_x, next_y) in visited): # checking if it's already been visited
                continue
            if((ord(get_candidate_alt(data[next_x][next_y])) - ord(get_candidate_alt(data[x][y]))) < -1): # checking if it's a cliff 
                continue
            if(get_candidate_alt(data[next_x][next_y]) == 'a'): # checking if it's at an altitude of a
                return(steps + 1)
            visited.add((next_x, next_y)) # adding to our set of visited coordinates
            q.append((steps + 1, next_x, next_y)) # adding to our deque
    return 0

print(f'Part 2: {descend(end, data)}')
