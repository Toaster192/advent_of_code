import pdb
import parse
import collections
import copy

with open('day7-input') as f:
    input_data = f.read()

# pdb.set_trace()

data = input_data.split('\n')
data = [line for line in data if line.strip()]


class Program:
    def __init__(self, name, weight, holding, holder=None):
        self.name = name
        self.weight = int(weight)
        if holding == []:
            self.holding = holding
        else:
            self.holding = holding.split(', ')
        self.holder = None


Programs = []


def findProgram(name, Programs):
    for program in Programs:
        if program.name == name:
            return program
    return None


def holdingToPointers(Programs):
    for program in Programs:
        if program.holding != []:
            for i, item in enumerate(program.holding):
                program.holding[i] = findProgram(item, Programs)


def updateHolder(Programs):
    for program in Programs:
        if program.holding != []:
            for item in program.holding:
                item.holder = program


for line in data:
    holding = []
    parsed_data = parse.parse("{name} ({weight:d}{leftovers}", line)
    if parsed_data['leftovers'] != ")":
        holding = parsed_data['leftovers'][5:]
    Programs.append(Program(parsed_data['name'],
                            parsed_data['weight'],
                            holding))

holdingToPointers(Programs)
updateHolder(Programs)

BottomProgram = Programs.copy()

for program in Programs:
    for item in program.holding:
        BottomProgram.remove(item)

print(BottomProgram[0].name)

# Part 2:
pdb.set_trace()

Carrying = copy.deepcopy(Programs)

lastLength = 0

while(lastLength != len(Carrying)):
    lastLength = len(Carrying)
    for program in Carrying:
        if program.holding == []:
            holder = program.holder
            weights = []
            for item in holder.holding:
                weights.append(item.weight)
            weights = list(set(weights))
            if len(weights) == 1:
                for item in holder.holding:
                    holder.weight += item.weight
                    holder.holding.remove(item)
                    Carrying.remove(item)


def findOddOneOut(program, expected=0):
    if program.holding != []:
        weights = []
        for item in program.holding:
            weights.append(item.weight)
        counter = collections.Counter(weights)
        weights = list(set(weights))
        if len(weights) == 1:
            if(findProgram(program.name, Programs).holding != []):
                for item in findProgram(program.name, Programs).holding:
                    program.weight -= item.weight
                    expected -= item.weight
            return """Weight: {}, Expected: {}""".format(program.weight,
                                                         expected)
        for item in program.holding:
            if item.weight == min(counter, key=counter.get):
                return findOddOneOut(item, max(counter, key=counter.get))
    else:
        if(findProgram(program.name, Programs).holding != []):
            for item in findProgram(program.name, Programs).holding:
                program.weight -= item.weight
                expected -= item.weight
        return """Weight: {}, Expected: {}""".format(program.weight, expected)


for program in Carrying:
    if program.name == BottomProgram[0].name:
        print(findOddOneOut(program))
        break
