# No Space Left On Device

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def dict_of_dirs(data):
    dirs = {}
    # keys will be the paths of directories, values will be the total size
    path = ''
    for line in data:
        if(line[0:4] == '$ cd'): 
            if(line[5:] != '..'):
                if(len(dirs) == 0):
                    #print('parent directory')
                    path = '/'
                #if(line[5:] == '/'):
                    
                elif(path == '/'):
                    path += line[5:]
                else:
                    path += '/' + line[5:]
                #print('cd: ', path)
                key = path 
                if key not in dirs:
                    dirs[key] = 0 # calculate sizes later
            else:
                path = path[:-len(line[5:])-2]
    return dirs 

def calculate_sizes(dirs, data):
    answer = 0 # size of directories with a total_size <= 100000
    dirdir = []
    for path in dirs:
        if(path != '/'):
            dir = path.split('/')[-1]
        else:
            dir = path 
        dirdir.append(dir)
        for i in range(len(data)):
            line = data[i]
            if(line == '$ cd ' + dir): 
                levels_in = 1
                total_size = 0
                j = i + 1
                while(levels_in > 0):
                    cur_line = data[j]
                    if(cur_line == '$ cd ..'):
                        levels_in -= 1
                    elif(cur_line[:4] == '$ cd'):
                        levels_in += 1
                    if(cur_line[0].isdigit()):
                        # print(cur_line)
                        size = cur_line.split(' ')[0]
                        total_size += int(size)
                    if(j + 1 < len(data)):
                        j += 1
                    else:
                        break 
                dirs[path] = total_size
    for k,v in dirs.items():
        if(v <= 100000):
            answer += v       
    return answer 

data = load_data('day07example1.txt')
dirs = dict_of_dirs(data)
answer = calculate_sizes(dirs, data)
print(f'Example: {answer}') #95437

# Followed advice from hyper neutrino

data = load_data('input07.txt')
pwd = nd = {}
ancestors = []
for line in data:
    if(line[0] == '$'): # whenever there is a command
        if(line[2] == 'c'): # whenever we cd 
            dir = line[5:]
            if(dir == '/'): # whenever we go back to the outermost directory
                pwd = nd
                ancestors = []
            elif(dir == '..'): # whenever we go back up a level
                pwd = ancestors.pop() # resets pwd and removes last dir from ancestors
            else: # go into the directory
                if(dir not in pwd):  # if directory hasn't already been made
                    pwd[dir] = {} # make a new empty directory
                ancestors.append(pwd) # add present directory to ancestors list
                pwd = pwd[dir] # descend into subdirectory 
        # no need to do anything for ls lines
    else:
        if(line[0].isdigit()): # whenever it is a file the line begins with a digit
            size, filename = line.split()
            pwd[filename] = int(size)

def count(dir = nd):
    if(type(dir) == int): # whenever it is a file
        return (dir, 0) # dir = size of the file
    size = 0
    answer = 0
    for subdir in dir.values(): # iterating through the file sizes, ignoring their names
        s, a = count(subdir)
        size += s # size of a directory = size of its subdirectories and files
        answer += a 
    if(size <= 100000):
        answer += size 
    # if the size of a directory is too large, only the sizes of its subdirectories are added to answer
    return (size, answer)

print(f'Part 1: {count()[1]}')

# Part 2

def size(dir = nd):
    if(type(dir) == int): # whenever it is a file
        return dir # dir = size of the file
    return sum(map(size, dir.values())) # sum sizes of directory's contents 

threshold = size() - 40000000

def find_minimum_sufficient_dir(dir = nd):
    answer = 99999999999
    dir_size = size(dir)
    if(dir_size >= threshold): # whenever the dir is large enough to be a candidate for deletion
        answer = dir_size
    for subdir in dir.values():
        if(type(subdir) != int): # to skip over files
            candidate = find_minimum_sufficient_dir(subdir) # recursion to find smallest candidate directory
            answer = min(answer, candidate) # comparing previous min to new candidate min 
    return answer 

print(f'Part 2: {find_minimum_sufficient_dir()}')
