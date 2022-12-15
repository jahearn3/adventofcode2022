# Regolith Reservoir

import load_data as ld 

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

# def draw_rock_paths(endpoints, min_x, max_x, min_y, max_y):
#     grid = []
#     for i in range(min_x, max_x + 1):
#         for j in range(min_y, max_y + 1):
#             grid.append()


#     return grid

data = ld.load_data('day14example1.txt')
endpoints, min_x, max_x, min_y, max_y = find_endpoints(data)
# grid = draw_rock_paths(endpoints, min_x, max_x, min_y, max_y)