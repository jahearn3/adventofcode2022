# Boiling Boulders

import load_data as ld 
import numpy as np 
from collections import deque 

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

# data = ld.load_data('input18.txt')  
# max_a, max_b, max_c = size_up(data)  
# grid = populate_grid(max_a, max_b, max_c)
# print(f'Part 1: {calculate_surface_area(grid, max_a, max_b, max_c)}') # 3564 was the answer

# Part 2
def search_for_path_to_edge(grid, max_a, max_b, max_c, i, j, k):
    # breadth-first search from day 12 
    q = deque()
    q.append((i, j, k))
    visited = {(i, j, k)}

    while(q):
        x, y, z = q.popleft()
        neighbors = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
        for xx, yy, zz in neighbors:
            if((xx < 0) or (xx > max_a) or (yy < 0) or (yy > max_b) or (zz < 0) or (zz > max_c)): # checking if that coordinate exists in the grid
                continue
            if((xx, yy, zz) in visited): # checking if it's already been visited
                continue
            if(grid[xx][yy][zz] == 1): # checking if it's part of the lava and not open air
                continue 
            if((xx == 0) or (xx == max_a) or (yy == 0) or (yy == max_b) or (zz == 0) or (zz == max_c)): # checking if we've reached the edge
                return True
            visited.add((xx, yy, zz))
            q.append((xx, yy, zz))
    # if we exhaust the deque and have not returned True, then it is False (it is an interior pocket)
    return False

def recalculate_surface_area(grid, max_a, max_b, max_c):
    surface_area = 0
    for i in range(max_a + 1):
        for j in range(max_b + 1):
            for k in range(max_c + 1):
                # pocket = True 
                # if((i == 0) or (i == max_a)):
                #     pocket = False
                # else:
                #     s = 0
                #     for ii in range(i):
                #         s += grid[ii][j][k]
                #     if(s == 0):
                #         pocket = False
                #     else:
                #         s = 0
                #         for ii in range(max_a, i, -1):
                #             s += grid[ii][j][k]
                #         if(s == 0):
                #             pocket = False

                
                # if((j == 0) or (j == max_b)):
                #     pocket = False
                # else:
                #     s = 0
                #     for jj in range(j):
                #         s += grid[i][jj][k]
                #     if(s == 0):
                #         pocket = False
                #     else:
                #         s = 0
                #         for jj in range(max_b, j, -1):
                #             s += grid[i][jj][k]
                #         if(s == 0):
                #             pocket = False
                
                # if((k == 0) or (k == max_c)):
                #     pocket = False
                # else:
                #     s = 0
                #     for kk in range(k):
                #         s += grid[i][j][kk]
                #     if(s == 0):
                #         pocket = False
                #     else:
                #         s = 0
                #         for kk in range(max_c, k, -1):
                #             s += grid[i][j][kk]
                #         if(s == 0):
                #             pocket = False
                

                # if((grid[i][j][k] == 1) and (pocket == False)):
                
                if(grid[i][j][k] == 1):
                    exterior_surface = False 
                    if((i == 0) or (i == max_a)):
                        exterior_surface = True
                    if((j == 0) or (j == max_b)):
                        exterior_surface = True
                    if((k == 0) or (k == max_c)):
                        exterior_surface = True
                    if(exterior_surface == False):
                        exterior_surface = search_for_path_to_edge(grid, max_a, max_b, max_c, i, j, k)
                    if(exterior_surface):
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

print(f'Part 2: {recalculate_surface_area(grid, max_a, max_b, max_c)}') #  was the answer