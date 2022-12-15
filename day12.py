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

def find_path(start, end, data):
    cur_loc = start
    cur_alt = 'a'
    path = [cur_loc]
    options = []
    while(cur_loc != end):
        x = cur_loc[0]
        y = cur_loc[1]
        # evaluate up, down, left, right (if they exist)
        if(0 <= x - 1 <= len(data) - 1): # left
            if(ord(cur_alt) + 1 >= ord(data[x-1][y])):
                # print(cur_alt, ord(cur_alt) + 1)
                # print(data[x-1][y], ord(data[x-1][y]))
                options.append([x-1, y])
        if(0 <= x + 1 <= len(data) - 1): # right
            # print(x)
            # print(len(data))
            # print(len(data[0]))
            # print(y)
            if(ord(cur_alt) + 1 >= ord(data[x+1][y])):
                # print(cur_alt, ord(cur_alt) + 1)
                # print(data[x+1][y], ord(data[x+1][y]))
                options.append([x+1, y])
        if(0 <= y - 1 <= len(data[0]) - 1): # down
            if(ord(cur_alt) + 1 >= ord(data[x][y-1])):
                # print(cur_alt, ord(cur_alt) + 1)
                # print(data[x][y-1], ord(data[x][y-1]))
                options.append([x, y-1])
        if(0 <= y + 1 <= len(data[0]) - 1): # up
            if(ord(cur_alt) + 1 >= ord(data[x][y+1])):
                # print(cur_alt, ord(cur_alt) + 1)
                # print(data[x][y+1], ord(data[x][y+1]))
                options.append([x, y+1])
        # print(options)
        #TODO: score the options
        # low score if it's in path
        # high score if it goes closer to end 
        if(len(path) > 1):
            print(f'Before: {len(options)}')
            if(len(options) > 1): # Remove previous location from options if there are more than 1
                options = [option for option in options if option not in path]
            print(f'After: {len(options)}')
        if(len(options) == 1):
            cur_loc = options[0]
        elif(len(options) == 0):
            print('Dead end!')
            cur_loc = end
        else:
            # go in general direction of end
            delta_x = end[0] - cur_loc[0]
            delta_y = end[1] - cur_loc[1]
            max_delta = max(abs(delta_x), abs(delta_y))
            chosen = False
            if(max_delta == abs(delta_x)): # if bigger difference is x
                # print('xward')
                if(delta_x > 0): # go right
                    if([cur_loc[0] + 1, cur_loc[1]] in options):
                        cur_loc[0] += 1
                        chosen = True
                else: # go left
                    if([cur_loc[0] - 1, cur_loc[1]] in options):
                        cur_loc[0] -= 1
                        chosen = True
            else: # if bigger difference is y
                # print('yward')
                if(delta_y > 0):  # go up
                    if([cur_loc[0], cur_loc[1] + 1] in options):
                        cur_loc[1] += 1
                        chosen = True
                else: # go down
                    if([cur_loc[0], cur_loc[1] - 1] in options):
                        cur_loc[1] -= 1
                        chosen = True
            if(chosen == False): # choose direction randomly?
                idx = random.randint(0, len(options) - 1)
                cur_loc = options[idx]
                # chosen = True
        
        path.append(cur_loc)
        cur_alt = data[cur_loc[0]][cur_loc[1]]
        print(cur_loc, cur_alt)
        options.clear()

    return path 

#TODO: path that starts from the end; two paths seek each other and meet in the middle

data = ld.load_data('day12example1.txt')
start, end = find_start_and_end(data)
path = find_path(start, end, data)
print(f'Example: {len(path)}')

# data = ld.load_data('input12.txt')


