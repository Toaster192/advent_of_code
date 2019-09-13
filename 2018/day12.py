day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

state = data[0].split()[2]

combinations = {}

for line in data[2:]:
    line = line.split()
    note, result = line[0], line[2]
    combinations[note] = result


def get_next_gen(state, combinations):
    state = "...." + state + "...."
    next = ""
    for i in range(2, len(state) - 2):
        next += combinations[state[i-2:i+3]]

    return next


gens = 20

for _ in range(gens):
    state = get_next_gen(state, combinations)

sum = 0
for i in range(len(state)):
    if state[i] == '#':
        sum += i - (gens * 2)

print(sum)

# part 2


state = data[0].split()[2]
final_gens = 50000000000
gens = 300

for i in range(gens):
    state = get_next_gen(state, combinations)

print(state)

sum = 0
for i in range(len(state)):
    if state[i] == '#':
        sum += i - (gens * 2) + final_gens - gens

print(sum)
