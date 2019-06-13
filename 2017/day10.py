import pdb

with open('day10-input') as f:
    input_data = f.read().strip()


data = list(range(256))

pdb.set_trace()


def round(input_data, data, position, skip_size):
    for input in input_data:
        input = int(input)
        selected = []
        for i in range(input):
            selected.append(data[(position + i) % 256])
        selected.reverse()
        for i in range(input):
            data[(position + i) % 256] = selected[i]
        position = (position + input + skip_size) % 256
        skip_size += 1
    return [data, position, skip_size]


data = round(input_data.split(','), data, 0, 0)[0]

print(data[0]*data[1])

# Part 2:

input_data = list(input_data)

input_data = [ord(x) for x in input_data] + [17, 31, 73, 47, 23]

data = list(range(256))
position = 0
skip_size = 0

for x in range(64):
    output = round(input_data, data, position, skip_size)
    data, position, skip_size = output[0], output[1], output[2]


output = ""

for x in range(0, 255, 16):
    letter = data[x]
    for y in range(1, 16):
        letter ^= data[x + y]
    output = output + hex(letter)[2:].zfill(2)


print(output)
