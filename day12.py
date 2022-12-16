# Hill Climbing Algorithm

import load_data as ld 
import random 

def find_start_and_end(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j] == 'S'):
                start = [i, j]
                # print(f'start: ({i},{j})')
            elif(data[i][j] == 'E'):
                end = [i, j]
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
    return score

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

#TODO: path that starts from the end; two paths seek each other and meet in the middle

data = ld.load_data('day12example1.txt')
start, end = find_start_and_end(data)
# path = find_path(start, end, data)
print(f'Example: {simulate_paths(start, end, data)} (should be 31)')

# data = ld.load_data('input12.txt')
# start, end = find_start_and_end(data)
# print(f'Part 1: {simulate_paths(start, end, data)}') # 231 was too low


