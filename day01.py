def load_data(filename):
    lines = []
    with open('data/' + filename) as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines

def count_calories_per_elf(data):
    cal_per_elf = []
    calories = 0
    for line in data:
        if(line == ''):
            cal_per_elf.append(calories)
            calories = 0
        else:
            calories += int(line)
            if(line is data[-1]):
                cal_per_elf.append(calories)
    return cal_per_elf

print('Example: ')
data = load_data('day01example1.txt')
cal_per_elf = count_calories_per_elf(data)
max_cal = max(cal_per_elf)
print(max_cal)

print('Puzzle: ')
data = load_data('input01.txt')
cal_per_elf = count_calories_per_elf(data)
max_cal = max(cal_per_elf)
print(max_cal) # 69626 was the answer

print('Part 2: ')
sorted_cal_per_elf = sorted(cal_per_elf)
top3 = sorted_cal_per_elf[-1] + sorted_cal_per_elf[-2] + sorted_cal_per_elf[-3]
print(top3) # 206780 was the answer
