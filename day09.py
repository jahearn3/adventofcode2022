# Rope Bridge

import load_data as ld

def move_head(head_pos, direction):
    if(direction == 'U'):
        head_pos[1] += 1
    elif(direction == 'D'):
        head_pos[1] -= 1
    elif(direction == 'L'):
        head_pos[0] -= 1
    elif(direction == 'R'):
        head_pos[0] += 1
    return head_pos 

def move_tail(head_pos, tail_pos):
    delta_x = head_pos[0] - tail_pos[0]
    delta_y = head_pos[1] - tail_pos[1]
    if((delta_x == 2) and (delta_y == 0)):
        tail_pos[0] += 1
    elif((delta_x == -2) and (delta_y == 0)):
        tail_pos[0] -= 1
    elif((delta_y == 2) and (delta_x == 0)):
        tail_pos[1] += 1
    elif((delta_y == -2) and (delta_x == 0)):
        tail_pos[1] -= 1
    # circumstances that require diagonal motion
    elif((delta_x == 2) and (delta_y == 1)):
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif((delta_x == 2) and (delta_y == -1)):
        tail_pos[0] += 1
        tail_pos[1] -= 1
    elif((delta_x == -2) and (delta_y == 1)):
        tail_pos[0] -= 1
        tail_pos[1] += 1
    elif((delta_x == -2) and (delta_y == -1)):
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    elif((delta_x == 1) and (delta_y == 2)):
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif((delta_x == -1) and (delta_y == 2)):
        tail_pos[0] -= 1
        tail_pos[1] += 1
    elif((delta_x == 1) and (delta_y == -2)):
        tail_pos[0] += 1
        tail_pos[1] -= 1
    elif((delta_x == -1) and (delta_y == -2)):
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    return tail_pos

def simulate(data):
    head_x = 0; head_y = 0; tail_x = 0; tail_y = 0
    head_pos = [head_x, head_y]
    tail_pos = [tail_x, tail_y]
    tail_pos_visited = []
    tail_pos_visited.append(str(tail_pos))

    for line in data:
        direction, magnitude = line.split()
        # direction = line[0]
        # magnitude = line[2] # this line was the source of my errors: it only accounted for magnitudes up to 9
        for i in range(int(magnitude)):
            head_pos = move_head(head_pos, direction)
            tail_pos = move_tail(head_pos, tail_pos)
            tail_pos_visited.append(str(tail_pos))

    return len(set(tail_pos_visited))

data = ld.load_data('day09example1.txt')
print(f'Example: {simulate(data)}')

data = ld.load_data('input09.txt')
print(f'Part 1: {simulate(data)}') # 2985 was too low, 5619 was the answer

# Part 2

def move_tail2(head_pos, tail_pos):
    delta_x = head_pos[0] - tail_pos[0]
    delta_y = head_pos[1] - tail_pos[1]
    if((abs(delta_x)) + abs(delta_y) == 2): # diagonal motion not required
        if((delta_x == 2) and (delta_y == 0)):
            tail_pos[0] += 1
        elif((delta_x == -2) and (delta_y == 0)):
            tail_pos[0] -= 1
        elif((delta_y == 2) and (delta_x == 0)):
            tail_pos[1] += 1
        elif((delta_y == -2) and (delta_x == 0)):
            tail_pos[1] -= 1
    # circumstances that require diagonal motion
    elif((abs(delta_x)) + abs(delta_y) > 2):
        if(delta_x > 0):
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
        if(delta_y > 0):
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1
    return tail_pos

def simulate2(data):
    init_x = 0; init_y = 0
    knots = []
    for i in range(10): # initializing
        knots.append([init_x, init_y])
    tail_pos_visited = []
    tail_pos_visited.append(str(knots[-1]))
    for line in data:
        direction, magnitude = line.split()
        for i in range(int(magnitude)):
            knots[0] = move_head(knots[0], direction)
            for j in range(1, len(knots)):
                knots[j] = move_tail2(knots[j-1], knots[j])
            tail_pos_visited.append(str(knots[-1]))

    return len(set(tail_pos_visited)) 

print(f'Part 2: {simulate2(data)}') # 2376 was the answer