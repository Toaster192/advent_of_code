# import pdb

with open('day6-input') as f:
    input_data = f.read()

data = list(map(int, input_data.split()))

# pdb.set_trace()
turns = 0
history = []
end = False

while True:
    for j, item in enumerate(history):
        if item == data:
            end = True
            loopsize = turns - j
    if end:
        break
    history.append(data.copy())
    turns += 1
    max = 0

    for i in range(len(data)):
        if data[i] > data[max]:
            max = i

    amount = data[max]
    data[max] = 0
    i = max + 1

    while amount:
        if i > len(data) - 1:
            i = 0
        data[i] += 1
        amount -= 1
        i += 1

print(turns)

# Part 2:

print(loopsize)
