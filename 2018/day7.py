day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()


def get_next(steps):
    available = get_available(steps)
    available.sort()
    if available:
        return available[0]
    else:
        return None


def get_available(steps):
    return [x for x in steps if steps[x] == ""]


steps = {}

for line in data:
    line = line.split()
    step = line[7]
    requirement = line[1]
    if step in steps:
        steps[step] += requirement
    else:
        steps[step] = requirement
    if requirement not in steps:
        steps[requirement] = ""

steps_backup = steps.copy()
order = ""

while True:
    next_step = get_next(steps)
    if next_step is None:
        break
    order += next_step

    del steps[next_step]
    for step in steps:
        steps[step] = steps[step].replace(next_step, '')

print(order)

# part 2

steps = steps_backup

second = 0

workers = {}

while True:
    for worker in list(workers):
        if not workers[worker]:
            del steps[worker]
            for step in steps:
                steps[step] = steps[step].replace(worker, '')
            del workers[worker]

    for _ in range(5 - len(workers)):
        available = get_available(steps)
        available.sort()

        for step in available:
            if step not in workers:
                next_step = step
                break
        else:
            break

        workers[next_step] = ord(next_step) - ord('A') + 61

    if not workers:
        break

    second += 1
    for worker in workers:
        workers[worker] -= 1

print(second)
