
with open('day11-input') as f:
    input_data = f.read().strip()

x = 0
y = 0
max_steps = 0


def checksteps(x, y):
    steps = 0
    while x or y:
        if x:
            x += 1 if x < 0 else -1
            y += 1 if y < 0 else -1
        else:
            y += 2 if y < 0 else -2
        steps += 1
    return steps


for instruction in input_data.split(','):
    if len(instruction) == 2:
        if instruction[0] == 'n':
            y += 1
        else:
            y -= 1
        if instruction[1] == 'e':
            x += 1
        else:
            x -= 1
    elif instruction == "n":
        y += 2
    else:
        y -= 2
    steps = checksteps(x, y)
    if steps > max_steps:
        max_steps = steps

print(steps)
print(max_steps)
