# Monkey Math

import load_data as ld 

data = ld.load_data('day21example1.txt')
names = []
jobs = []
for line in data:
    name, job = line.split(':')
    names.append(name)
    jobs.append(job.strip(' '))

# while(True):
#     if()