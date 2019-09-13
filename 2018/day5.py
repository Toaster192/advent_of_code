day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

base_data = data[0].strip()

data = base_data

while True:
    for i in range(len(data) - 1):
        char = data[i]
        if char.isupper():
            if char.lower() == data[i + 1]:
                data = data[:i] + data[i + 2:]
                break
        else:
            if char.upper() == data[i + 1]:
                data = data[:i] + data[i + 2:]
                break
    else:
        break

print(len(data))

# part 2

min_len = len(data)
min_char = '0'

for j in range(ord('a'), ord('z') + 1):
    print(chr(j))
    data = base_data
    data = data.replace(chr(j), '')
    data = data.replace(chr(j).upper(), '')

    while True:
        for i in range(len(data) - 1):
            char = data[i]
            if char.isupper():
                if char.lower() == data[i + 1]:
                    data = data[:i] + data[i + 2:]
                    break
            else:
                if char.upper() == data[i + 1]:
                    data = data[:i] + data[i + 2:]
                    break
        else:
            break

    if len(data) < min_len:
        min_len = len(data)
        min_char = chr(j)

print(min_len)
