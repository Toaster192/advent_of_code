import pdb

with open('day9-input') as f:
    input_data = list(f.read().strip())

pdb.set_trace()


for i, char in enumerate(input_data):
    if char == '!':
        input_data[i] = ''
        input_data[i + 1] = ''


input_data = list(filter(('').__ne__, input_data))
i = -1
total_garbage = 0

for j, char in enumerate(input_data):
    if i == -1:
        if char == '<':
            i = j
    elif char == '>':
        for k in range(i, j + 1):
            input_data[k] = ''

        total_garbage += j - i - 1
        i = -1

input_data = list(filter(('').__ne__, input_data))


chars = []

for char in (x for x in input_data if x not in "{}"):
    if char not in chars:
        chars.append(char)


for char in chars:
    input_data = list(filter((char).__ne__, input_data))


total = 0
curr = 1

for char in input_data:
    if char == '{':
        total += curr
        curr += 1
    elif char == '}':
        curr -= 1

print(total)
print(total_garbage)
