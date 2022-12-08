# No Space Left On Device

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def build_filesystem_tree(data):
    filesystem = {}
    for line in data:
        if(line[0:4] == '$ cd'): 
            if(line[5:] == '..'):
                print('go up a level')
                for k, v in filesystem.items():
                    print(k, v)
                    
                        #if(value == k):
                # value = key 
                # key = # find key for that value 
            else:
                key = line[5:]
                if key not in filesystem:
                    filesystem[key] = {}
                print('create directory if it does not exist ' + line[5:])
                print('change to that directory')

        elif(line[0:4] == '$ ls'):
            print('list')
            #pass
        else:
            if(line[0:3] == 'dir'):
                key = line[3:]
                print('create directory ' + line[3:])
                if key not in filesystem:
                    filesystem[key] = {}
            else: 
                size, filename = line.split(' ')
                print('create file ' + filename + ' with size ' + size)
                filesystem[key].append([filename, size])

    return filesystem


# filesystem = build_filesystem_tree(data)
# for elem in filesystem:
#     print(elem)
# print(filesystem)

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
            if(line == '$ cd ' + dir): #TODO add a condition to check that the path is the unique one
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

    print(len(dirdir))
    print(len(set(dirdir)))

    for k,v in dirs.items():
        if(v <= 100000):
            answer += v       

    return answer 

data = load_data('day07example1.txt')
dirs = dict_of_dirs(data)
answer = calculate_sizes(dirs, data)
#print(dirs)
print(f'Example: {answer}') #95437

data = load_data('input07.txt')
dirs = dict_of_dirs(data)
answer = calculate_sizes(dirs, data)
#print(dirs)
print(f'Part 1: {answer}') # 1598125 was too low



