# Supply Stacks

import re # to split with multiple delimiters

def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def parse_data(data):
    stacks = []
    instructions = []
    for i in range(len(data)):
        if(len(data[i]) == 0):
            breakline = i
    stacks_raw = data[:breakline]
    instructions = data[breakline+1:]
    n_stacks = int(stacks_raw[-1].strip()[-1])
    stacks = [[] for x in range(n_stacks)]
    for i in range(len(stacks_raw) - 2, -1 , -1): # goes from bottom of stacks text to top
        for j in range(len(stacks)):
            text = data[i][j*4+1:j*4+2]
            if(text != ' '):
                stacks[j].append(text)
    return stacks, instructions

def top_crates(stacks, instructions):
    for instruction in instructions:
        n_crates, from_stack, to_stack = re.split(r'from | to ', instruction.strip('move '))
        for i in range(int(n_crates)):
            # pop off the end of stack identified by from
            popped = stacks[int(from_stack)-1].pop()
            # append to stack identified by to
            stacks[int(to_stack)-1].append(popped)
    answer = ''
    for stack in stacks:
        answer += stack[-1]
    return answer


data = load_data('day05example1.txt')
stacks, instructions = parse_data(data)
answer = top_crates(stacks, instructions)
print(f'Example: {answer}') # CMZ

data = load_data('input05.txt')
stacks, instructions = parse_data(data)
answer = top_crates(stacks, instructions)
print(f'Part 1: {answer}') # WHTLRMZRC was the answer

# Part 2
def top_crates2(stacks, instructions):
    for instruction in instructions:
        n_crates, from_stack, to_stack = re.split(r'from | to ', instruction.strip('move '))
        sliced = stacks[int(from_stack)-1][-int(n_crates):]  
        del stacks[int(from_stack)-1][-int(n_crates):]
        stacks[int(to_stack)-1].extend(sliced)
    answer = ''
    for stack in stacks:
        answer += stack[-1]
    return answer

data = load_data('day05example1.txt')
stacks, instructions = parse_data(data)
answer = top_crates2(stacks, instructions)
print(f'Example: {answer}') # MCD 

data = load_data('input05.txt')
stacks, instructions = parse_data(data)
answer = top_crates2(stacks, instructions)
print(f'Part 2: {answer}') # GMPMLWNMG was the answer