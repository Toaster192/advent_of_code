day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()


twos = 0
threes = 0
for line in data:
    letters = {}
    for char in line:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    if 2 in letters.values():
        twos += 1
    if 3 in letters.values():
        threes += 1


print(twos * threes)

# part 2:

for x in data:
    for y in data:
        if x != y:
            differences = [i for i in range(len(x)) if x[i] != y[i]]
            if len(differences) == 1:
                print(x[:differences[0]] + x[differences[0]+1:])
                exit()
