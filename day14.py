# Regolith Reservoir

import load_data as ld 
import numpy as np 

def find_endpoints(data):
    endpoints = []
    min_x = 500; max_x = 500; min_y = 0; max_y = 0
    for line in data:
        coords_str = line.split(' -> ')
        coordinates = []
        for coord in coords_str:
            x, y = coord.split(',')
            x = int(x)
            y = int(y)
            if(x < min_x):
                min_x = x 
            elif(x > max_x):
                max_x = x 
            if(y < min_y):
                min_y = y 
            elif(y > max_y):
                max_y = y 
            coordinates.append([x, y])
        endpoints.append(coordinates)
    return endpoints, min_x, max_x, min_y, max_y

def draw_rock_paths(endpoints, min_x, max_x, min_y, max_y):
    grid = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
    # for i in range(min_x, max_x + 1):
    #     for j in range(min_y, max_y + 1):
    #         grid.append()
    for e in endpoints:
        
        # print(e)
        # print(e[0][0], e[0][1])
        # grid[e[0][0] - min_x][e[0][1] - min_y] = 1
        
        for c in range(len(e) - 1): 
            
            # print(e[c][0], e[c][1])

            delta_x = e[c+1][0] - e[c][0]
            delta_y = e[c+1][1] - e[c][1]

            if(delta_x > 0):
                for i in range(delta_x):
                    # print(e[c][0] + i, e[c][1])
                    grid[e[c][0] + i - min_x][e[c][1]] = 1
            elif(delta_x < 0):
                for i in range(-delta_x):
                    # print(e[c][0] - i, e[c][1])
                    grid[e[c][0] - i - min_x][e[c][1]] = 1
            if(delta_y > 0):
                for i in range(delta_y):
                    # print(e[c][0], e[c][1] + i)
                    grid[e[c][0] - min_x][e[c][1] + i] = 1
            elif(delta_y < 0):
                for i in range(-delta_y):
                    # print(e[c][0], e[c][1] - i)
                    grid[e[c][0] - min_x][e[c][1] - i] = 1

        # print(e[-1][0], e[-1][1])
        grid[e[-1][0] - min_x][e[-1][1]] = 1

    return grid

data = ld.load_data('day14example1.txt')
endpoints, min_x, max_x, min_y, max_y = find_endpoints(data)
# print(endpoints, min_x, max_x, min_y, max_y)
grid = draw_rock_paths(endpoints, min_x, max_x, min_y, max_y)
print(grid)