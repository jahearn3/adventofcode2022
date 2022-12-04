# Camp Cleanup

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def count_contained(data):
    contained = 0
    for line in data:
        pair = line.split(',')
        limits0 = pair[0].split('-')
        limits1 = pair[1].split('-')
        #print(limits0, limits1)
        if((int(limits0[0]) <= int(limits1[0])) and (int(limits0[1]) >= int(limits1[1]))):
            contained += 1
            # print(f'{limits1} fully contained in {limits0}')
        elif((int(limits0[0]) >= int(limits1[0])) and (int(limits0[1]) <= int(limits1[1]))):
            contained += 1
            # print(f'{limits0} fully contained in {limits1}')
    return contained 

data = load_data('day04example1.txt')
answer = count_contained(data)
print(f'Example: {answer}')

data = load_data('input04.txt')
answer = count_contained(data)
print(f'Part 1: {answer}') # 569 was too high, 542 was the answer

# Part 2
def count_overlaps(data):
    overlaps = 0
    for line in data:
        pair = line.split(',')
        limits0 = pair[0].split('-')
        limits1 = pair[1].split('-')
        if((int(limits0[0]) <= int(limits1[0])) and (int(limits0[1]) >= int(limits1[1]))):
            overlaps += 1
        elif((int(limits0[0]) >= int(limits1[0])) and (int(limits0[1]) <= int(limits1[1]))):
            overlaps += 1
        elif((int(limits0[0]) <= int(limits1[0]) <= int(limits0[1])) or (int(limits0[0]) <= int(limits1[1]) <= int(limits0[1]))): 
            overlaps += 1
        elif((int(limits1[0]) <= int(limits0[0]) <= int(limits1[1])) or (int(limits1[0]) <= int(limits0[1]) <= int(limits1[1]))):
            overlaps += 1
    return overlaps 
answer = count_overlaps(data)
print(f'Part 2: {answer}') # 900 was the answer