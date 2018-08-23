with open('day4-input') as f:
    input_data = f.read()


result = 0


def checkline(line):
    for i, word in enumerate(line.split()):
        for j in range(i):
            if word == line.split()[j]:
                return 0
    return 1


for line in input_data.split('\n'):
    if line != "":
        result += checkline(line)


print(result)

# Part 2:

result = 0


def checklineSorted(line):
    for i, word in enumerate(line.split()):
        word = sorted(word)
        for j in range(i):
            if word == sorted(line.split()[j]):
                return 0
    return 1


for line in input_data.split('\n'):
    if line != "":
        result += checklineSorted(line)

print(result)
