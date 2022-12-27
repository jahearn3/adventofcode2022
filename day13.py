# Distress Signal

import load_data as ld 
import re 

def preprocess(data):
    packets = [[],[]]
    for i in range(0, len(data)+1, 3):
        packets[0].append(data[i])
        packets[1].append(data[i+1])
    return packets

def discern_elements(packet):
    elements = []
    #layers = len(re.findall("[", packet))
    layers = sum(map(lambda x : 1 if '[' in x else 0, packet))
    print(f'{packet} has {layers} layers')
    if(layers == 0):
        for j in range(len(packet)):
            if(packet[j].isdigit()):
                elements.append(int(packet[j]))
    else:
        j = 0
        for n in range(layers):
            elem = []
            proceed = True
            while(proceed):
                elem.append(packet[j])
                if(packet[j] == ']'):
                    proceed = False
                j += 1
            elements.append(elem)
    return elements

def sum_indices_of_pairs_in_correct_order(data):
    correctly_ordered_pairs = []
    for i in range(len(packets[0])):
        packet1 = packets[0][i][1:-1]
        packet2 = packets[1][i][1:-1]
        elements1 = discern_elements(packet1)
        elements2 = discern_elements(packet2)

        print(elements1)
        print(elements2)
    return sum(correctly_ordered_pairs)

# data = ld.load_data('day13example1.txt')
# packets = preprocess(data)
# print(packets[0])
# print(packets[1])
# print(f'Example: {sum_indices_of_pairs_in_correct_order(packets)}')

# Learning from hyper neutrino 

def f(x, y):
    if(type(x) == int):
        if(type(y) == int):
            return x - y # only the sign matters
        else:
            return f([x], y) # putting x into a list to compare it
    elif(type(y) == int):
            return f(x, [y]) # putting y into a list to compare it 
    # otherwise, they are both lists
    for a, b in zip(x, y): # zip has length of shorter list
        v = f(a, b)
        if(v): # if v is non-zero
            return v # carry on the result 
    return len(x) - len(y) # seeing if one of them is shorter

def sum_indices(x):
    total = 0
    for i, (a, b) in enumerate(x):
        if(f(eval(a), eval(b)) < 0): # eval treats the string as a python expression 
            total += i + 1 # add to running sum the index(+1) of the pairs that are in the right order
    return total

# split into blocks, then into pairs (of strings), and put those into a list 
x = list(map(str.splitlines, open("data/day13example1.txt").read().strip().split("\n\n")))
print(f'Example: {sum_indices(x)}')
x = list(map(str.splitlines, open("data/input13.txt").read().strip().split("\n\n")))
print(f'Part 1: {sum_indices(x)}')

# Part 2

def decoder_key(x):
    i2 = 1
    i6 = 2
    for a in x:
        if(f(a, [[2]]) < 0):
            i2 += 1
            i6 += 1
        elif(f(a, [[6]]) < 0):
            i6 += 1
    return i2 * i6

x = list(map(eval, open("data/day13example1.txt").read().split()))
print(f'Example: {decoder_key(x)}')
x = list(map(eval, open("data/input13.txt").read().split()))
print(f'Part 2: {decoder_key(x)}')
