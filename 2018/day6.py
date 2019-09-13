day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()


def distance(pointX, pointY, X, Y):
    return abs(X - pointX) + abs(Y - pointY)


max_x = 0
max_y = 0

for line in data:
    x, y = line.split(',')

    x = int(x.strip())
    y = int(y.strip())

    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

max_x += 2
max_y += 2

grid = [[{} for _ in range(max_x)] for _ in range(max_y)]

ids = []

for y in range(max_y):
    for x in range(max_x):
        for i, line in enumerate(data):
            pointX, pointY = line.split(',')

            pointX = int(pointX.strip())
            pointY = int(pointY.strip())

            grid[y][x][i] = distance(x, y, pointX, pointY)

            if i not in ids:
                ids.append(i)

        min_distance = 99999
        for i in grid[y][x]:
            if grid[y][x][i] < min_distance:
                min_distance = grid[y][x][i]

        grid[y][x] = {k: v for k, v in grid[y][x].items() if v == min_distance}

infinite = []

for y in range(max_y):
    for x in range(max_x):
        if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
            for i in grid[y][x]:
                if i not in infinite:
                    infinite.append(i)

finite = {x: 0 for x in ids if x not in infinite}

for y in range(max_y):
    for x in range(max_x):
        if len(grid[y][x]) == 1:
            foo = list(grid[y][x].keys())[0]
            if foo in finite:
                finite[foo] += 1

max_area = 0
for i in finite.values():
    if i > max_area:
        max_area = i

print(max_area)

# part 2:

grid = [[{} for _ in range(max_x)] for _ in range(max_y)]

maximum_total_distance = 10000
area_counter = 0

for y in range(max_y):
    for x in range(max_x):
        for i, line in enumerate(data):
            pointX, pointY = line.split(',')

            pointX = int(pointX.strip())
            pointY = int(pointY.strip())

            grid[y][x][i] = distance(x, y, pointX, pointY)

        total_distance = 0
        for i in grid[y][x]:
            total_distance += grid[y][x][i]

        if total_distance < maximum_total_distance:
            area_counter += 1

print(area_counter)
