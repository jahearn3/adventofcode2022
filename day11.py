# Monkey in the Middle

import load_data as ld 
import re 

def load_monkeys(data):
    monkeys = []
    for line in data:
        if(len(line) == 0):
            pass
        elif(line[:6] == 'Monkey'):
            id = int(re.split(r'Monkey |:', line)[1])
        else:
            a, b = line.split(':')
            if(a.strip(' ') == 'Starting items'):
                start = list(b.split(','))
                starting_items = [int(item) for item in start]
            elif(a.strip(' ') == 'Operation'):
                operation = b.split(' = ')[1]
            elif(a.strip(' ') == 'Test'):
                test = int(b.split(' by ')[1])
            elif(a.strip(' ') == 'If true'):
                if_true = int(b.split(' monkey ')[1])
            elif(a.strip(' ') == 'If false'):
                if_false = int(b.split(' monkey ')[1])
        if(len(line) == 0):
            monkeys.append([id, starting_items, operation, test, if_true, if_false, 0])

    monkeys.append([id, starting_items, operation, test, if_true, if_false, 0])
    return monkeys 

def operate(value, operation):
    a, b, c = operation.split(' ')
    if(c == 'old'):
        if(b == '+'):
            return value + value
        elif(b == '*'):
            return value * value 
        else:
            print('Hmmm')
            return value 
    else:
        if(b == '+'):
            return value + int(c)
        elif(b == '*'):
            return value * int(c)
        else:
            print('Weird')
            return value 

def monkey_business(monkeys, rounds):
    if(rounds == 10000):
        mod = 1
        for monkey in monkeys:
            mod *= monkey[3]
    for r in range(rounds):
        if(r % 10 == 0):
            print(f'round {r}')
        for i in range(len(monkeys)):
            for j in range(len(monkeys[i][1])):
                monkeys[i][1][j] = operate(monkeys[i][1][j], monkeys[i][2])
                if(rounds == 20): # just for part 1
                    monkeys[i][1][j] = monkeys[i][1][j] // 3 # divide by 3 and round down
                elif(rounds == 10000):
                    monkeys[i][1][j] %= mod # modular math
                if(monkeys[i][1][j] % monkeys[i][3] == 0): # if true
                    monkeys[monkeys[i][4]][1].append(monkeys[i][1][j])
                else:  # if false
                    monkeys[monkeys[i][5]][1].append(monkeys[i][1][j])
                monkeys[i][6] += 1 # increasing the activity count
            monkeys[i][1].clear()
    return monkeys

def evaluate_monkey_activity(monkeys):
    monkey_activity = []
    for i in range(len(monkeys)):
        print(monkeys[i][0], monkeys[i][1], monkeys[i][6])
        monkey_activity.append(monkeys[i][6])
    active_monkeys = sorted(monkey_activity, reverse=True)
    return active_monkeys[0] * active_monkeys[1]

data = ld.load_data('day11example1.txt')
monkeys = load_monkeys(data)
monkeys = monkey_business(monkeys, 20)
print(f'Example: {evaluate_monkey_activity(monkeys)}')

data = ld.load_data('input11.txt')
monkeys = load_monkeys(data)
monkeys = monkey_business(monkeys, 20)
print(f'Part 1: {evaluate_monkey_activity(monkeys)}') # 57348 was the answer

# Part 2
monkeys = load_monkeys(data)
monkeys = monkey_business(monkeys, 10000)
print(f'Part 2: {evaluate_monkey_activity(monkeys)}')