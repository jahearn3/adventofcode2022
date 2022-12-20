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

data = ld.load_data('day13example1.txt')
packets = preprocess(data)
# print(packets[0])
# print(packets[1])
print(f'Example: {sum_indices_of_pairs_in_correct_order(packets)}')
