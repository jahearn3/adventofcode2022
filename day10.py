# Cathode-Ray Tube

import load_data as ld

def check_signal(cycle, x):
    return cycle * x

def sum_signal_strengths(data):
    x = 1
    cycle = 1
    answer = 0
    
    for i in range(len(data)):
        if(data[i] == 'noop'):
            cycle += 1
            if((cycle - 20) % 40 == 0):
                answer += check_signal(cycle, x)
        elif(data[i][:4] == 'addx'):
            v = int(data[i].split(' ')[1])
            cycle += 1
            if((cycle - 20) % 40 == 0):
                answer += check_signal(cycle, x)
            cycle += 1
            x += v
            if((cycle - 20) % 40 == 0):
                answer += check_signal(cycle, x)
    return answer

data = ld.load_data('day10example2.txt')
print(f'Example: {sum_signal_strengths(data)}') #13140

data = ld.load_data('input10.txt')
print(f'Part 1: {sum_signal_strengths(data)}') # 15260 was the answer

# Part 2
def check_for_sprite(position, x):
    if(x - 1 <= (position % 40) <= x + 1):
        return '#'
    else:
        return '.'

def check_cycle_number(cycle, crt_rows, current_row):
    if((cycle - 1) % 40 == 0):
        crt_rows.append(current_row)
        current_row = ''
    return crt_rows, current_row

def produce_image(data):
    x = 1
    cycle = 1
    crt_rows = []
    #current_row = check_for_sprite(cycle, x)
    current_row = ''
    for i in range(len(data)):
        if(data[i] == 'noop'):
            current_row += check_for_sprite(cycle - 1, x)
            cycle += 1
            crt_rows, current_row = check_cycle_number(cycle, crt_rows, current_row)
        elif(data[i][:4] == 'addx'):
            v = int(data[i].split(' ')[1])
            current_row += check_for_sprite(cycle - 1, x)
            cycle += 1
            crt_rows, current_row = check_cycle_number(cycle, crt_rows, current_row)
            current_row += check_for_sprite(cycle - 1, x)
            cycle += 1
            x += v
            crt_rows, current_row = check_cycle_number(cycle, crt_rows, current_row)
    for row in crt_rows:
        print(row)

#data = ld.load_data('day10example2.txt')
produce_image(data) #PGHFGLUG

        
        