with open('day5-input') as f:
    input_data = f.read()

field = input_data.split('\n')

field = list(map(int, field))


pos = 0
step = 0
totalSteps = 0

while pos < len(field):
    step = field[pos]
    field[pos] += 1
    pos += step
    totalSteps += 1


print(totalSteps)

# Part 2:

field = input_data.split('\n')

field = list(map(int, field))


pos = 0
step = 0
totalSteps = 0

while pos < len(field):
    step = field[pos]
    if step < 3:
        field[pos] += 1
    else:
        field[pos] -= 1
    pos += step
    totalSteps += 1


print(totalSteps)
