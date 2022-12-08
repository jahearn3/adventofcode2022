# Treetop Tree House

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def count_visible_trees(data):
    count = 0
    # is visible? 
    for i in range(len(data)):
        for j in range(len(data[i])):
            # if it's on an edge, yes
            if((i == 0) or (j == 0) or (i == len(data) - 1) or (j == len(data) - 1)):
                count += 1

            else: # check all 4 directions
                # check up
                up = True
                for k in range(i):
                    if(data[i][j] <= data[k][j]):
                        up = False
                # check down
                down = True
                for k in range(i+1, len(data)):
                    if(data[i][j] <= data[k][j]):
                        down = False
                # check left
                left = True
                for l in range(j):
                    if(data[i][j] <= data[i][l]):
                        left = False
                # check right
                right = True
                for l in range(j+1, len(data[i])):
                    if(data[i][j] <= data[i][l]):
                        right = False
                if(up or down or left or right):
                    count += 1
    return count

data = load_data('day08example1.txt')
print(f'Example: {count_visible_trees(data)}') # 21

data = load_data('input08.txt')
print(f'Part 1: {count_visible_trees(data)}') # 1807 was the answer

# Part 2
def scenic_scores(data):
    max_scenic_score = 0 
    for i in range(len(data)):
        for j in range(len(data[i])):
            # if it's on an edge, the scenic score will be zero
            if((i == 0) or (j == 0) or (i == len(data) - 1) or (j == len(data) - 1)):
                scenic_score = 0
            else:
                # check up
                up_count = 0
                for k in range(i-1, -1, -1):
                    up_count += 1
                    # print('above ', data[i][j], ':', data[k][j])
                    if(data[i][j] <= data[k][j]):
                        break
                # check down
                down_count = 0
                for k in range(i+1, len(data)):
                    down_count += 1
                    # print('below ', data[i][j], ':', data[k][j])
                    if(data[i][j] <= data[k][j]):
                        break
                # check left
                left_count = 0
                for l in range(j-1, -1, -1):
                    left_count += 1
                    # print('left of ', data[i][j], ':', data[i][l])
                    if(data[i][j] <= data[i][l]):
                        break
                # check right
                right_count = 0
                for l in range(j+1, len(data[i])):
                    right_count += 1
                    # print('right of ', data[i][j], ':', data[i][l])
                    if(data[i][j] <= data[i][l]):
                        break
                scenic_score = up_count * down_count * left_count * right_count
                if(scenic_score > max_scenic_score):
                    max_scenic_score = scenic_score
                
                    # print(data[i][j])
                    # print(up_count, down_count, left_count, right_count)
                
    return max_scenic_score

#data = load_data('day08example1.txt')
print(f'Part 2: {scenic_scores(data)}') # 1921752 was not right, 480000 was right