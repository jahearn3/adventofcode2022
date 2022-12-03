# Rucksack Reorganization

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def find_common_item_types(data):
    common_item_types = []
    for line in data:
        # split in half
        half = int(len(line) / 2)
        compartment1 = line[:half]
        compartment2 = line[half:]
        # identify common item type
        common_item_types.append(set(compartment1).intersection(compartment2))
        #print(common_item_types)
    return common_item_types

def prioritize(common_item_types):
    answer = 0
    for x in common_item_types: 
        for char in x: # there is only one char in each x
            if(char.lower() == char): # lowercase
                answer += (ord(char) - 96) 
            else: # uppercase
                answer += (ord(char) - 38)
    return answer

data = load_data('day03example1.txt')
common_item_types = find_common_item_types(data)
answer = prioritize(common_item_types)
print(f'Example: {answer}')

data = load_data('input03.txt')
common_item_types = find_common_item_types(data)
answer = prioritize(common_item_types)
print(f'Part 1: {answer}') # 8240 was the answer

# Part 2
def identify_badges(data):
    badges = []
    for i in range(0, len(data), 3):
        set1 = set(data[i]).intersection(data[i+1])
        set2 = set1.intersection(data[i+2])
        badges.append(set2)
    return badges

badges = identify_badges(data)
answer = prioritize(badges)
print(f'Part 2: {answer}') # 2587 was the answer