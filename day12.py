import parse
import pdb

with open('day12-input') as f:
    input_data = f.read().strip()

pdb.set_trace()

data = dict()

for line in input_data.split('\n'):
    parsed_data = parse.parse(
            "{program:d} <-> {pair}",
            line)
    data[parsed_data['program']] = parsed_data['pair']


programs = [0]
new = [0]

while new:
    for item in new:
        new.remove(item)
        for program in data[item].split(','):
            program = int(program)
            if program not in programs:
                programs.append(program)
                new.append(program)

print(len(programs))

# Part 2:

groups = 1

for item in list(data):
    if item in programs:
        data.pop(item, None)

while data:
    programs = [next(iter(data))]
    new = [programs[0]]
    groups += 1
    while new:
        for item in new:
            new.remove(item)
            for program in data[item].split(','):
                program = int(program)
                if program not in programs:
                    programs.append(program)
                    new.append(program)

    for item in list(data):
        if item in programs:
            data.pop(item, None)


print(groups)
