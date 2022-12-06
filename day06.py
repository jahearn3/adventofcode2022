# Tuning Trouble

def import_line(filename):
    with open('data/' + filename) as f:
        line = f.readlines()[0]
    return line 

def identify_idx(datastream, idx):
    for i in range(idx, len(datastream)):
        if(len(set(datastream[i-idx:i])) == idx):
            return i
    print('Not found!')
    return 0 

datastream = import_line('day06example1.txt')
print(f'Example: {identify_idx(datastream, 4)}')

datastream = import_line('input06.txt')
print(f'Part 1: {identify_idx(datastream, 4)}') # 1816 was the answer 
print(f'Part 2: {identify_idx(datastream, 14)}') # 2625 was the answer