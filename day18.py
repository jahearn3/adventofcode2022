# Boiling Boulders

import load_data as ld 
import numpy as np 

def size_up(data):
    max_a = 0; max_b = 0; max_c = 0
    # min_a = 0; min_b = 0; min_c = 0

    for line in data:
        a, b, c = line.split(',')
        a = int(a)
        b = int(b)
        c = int(c)
        if(a > max_a):
            max_a = a 
        if(b > max_b):
            max_b = b 
        if(c > max_c):
            max_c = c 
        # if(a < min_a):
        #     min_a = a 
        # if(b < min_b):
        #     min_b = b 
        # if(c < min_c):
        #     min_c = c 

    # print(min_a, max_a)
    # print(min_b, max_b)
    # print(min_c, max_c)
    return max_a, max_b, max_c 

def populate_grid(max_a, max_b, max_c):
    grid = np.zeros((max_a + 1, max_b + 1, max_c + 1))
    for line in data:
        a, b, c = line.split(',')
        grid[int(a)][int(b)][int(c)] = 1
    return grid

def calculate_surface_area(grid, max_a, max_b, max_c):
    surface_area = 0
    for i in range(max_a + 1):
        for j in range(max_b + 1):
            for k in range(max_c + 1):
                if(grid[i][j][k] == 1):
                    surface_area += 6
                    if(i > 0):
                        if(grid[i-1][j][k] == 1):
                            surface_area -= 1
                    if(i < max_a):
                        if(grid[i+1][j][k] == 1):
                            surface_area -= 1
                    if(j > 0):
                        if(grid[i][j-1][k] == 1):
                            surface_area -= 1
                    if(j < max_b):
                        if(grid[i][j+1][k] == 1):
                            surface_area -= 1
                    if(k > 0):
                        if(grid[i][j][k-1] == 1):
                            surface_area -= 1
                    if(k < max_c):
                        if(grid[i][j][k+1] == 1):
                            surface_area -= 1
    return surface_area

data = ld.load_data('day18example1.txt')
max_a, max_b, max_c = size_up(data)
grid = populate_grid(max_a, max_b, max_c)
print(f'Example: {calculate_surface_area(grid, max_a, max_b, max_c)}') #64

data = ld.load_data('input18.txt')  
max_a, max_b, max_c = size_up(data)  
grid = populate_grid(max_a, max_b, max_c)
print(f'Part 1: {calculate_surface_area(grid, max_a, max_b, max_c)}') # 3564 was the answer

# Part 2

