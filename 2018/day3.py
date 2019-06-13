day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

lines = []

for i, line in enumerate(data):
    lines.append({})
    line = line.split("@")
    lines[i]["id"] = int(line[0][1:].strip())
    line = line[1].split(":")
    lines[i]["fromX"] = int(line[0].split(",")[0].strip())
    lines[i]["fromY"] = int(line[0].split(",")[1].strip())
    lines[i]["sizeX"] = int(line[1].split("x")[0].strip())
    lines[i]["sizeY"] = int(line[1].split("x")[1].strip())

maxX = 0
maxY = 0
for line in lines:
    if line["fromX"] + line["sizeX"] > maxX:
        maxX = line["fromX"] + line["sizeX"]
    if line["fromY"] + line["sizeY"] > maxY:
        maxY = line["fromY"] + line["sizeY"]


fabric = [[0 for _ in range(maxX)] for _ in range(maxY)]

for line in lines:
    fromX = line["fromX"]
    fromY = line["fromY"]
    sizeX = line["sizeX"]
    sizeY = line["sizeY"]

    for y in range(sizeY):
        for x in range(sizeX):
            fabric[fromY + y][fromX + x] += 1

shared = 0

for line in fabric:
    for number in line:
        if number > 1:
            shared += 1

print(shared)

# part 2:

fabric = [[[] for _ in range(maxX)] for _ in range(maxY)]

for line in lines:
    id = line["id"]
    fromX = line["fromX"]
    fromY = line["fromY"]
    sizeX = line["sizeX"]
    sizeY = line["sizeY"]

    for y in range(sizeY):
        for x in range(sizeX):
            fabric[fromY + y][fromX + x].append(id)

shared = {}

for line in fabric:
    for ids in line:
        if len(ids) > 1:
            for id in ids:
                shared[id] = '0'

for line in lines:
    if line["id"] not in shared:
        print(line["id"])
