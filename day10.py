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


        
        