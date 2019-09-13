import re

day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

points = []

for line in data:
    line = re.match(r"position=<\s?(-?\d+), \s?(-?\d+)> "
                    r"velocity=<\s?(-?\d+), \s?(-?\d+)>", line)
    point = {}
    point['xpos'] = int(line.group(1))
    point['ypos'] = int(line.group(2))
    point['xvec'] = int(line.group(3))
    point['yvec'] = int(line.group(4))
    points.append(point)


def move(points):
    for point in points:
        point['xpos'] += point['xvec']
        point['ypos'] += point['yvec']
    return points


def minmax(points, coordinate):
    max = -999999
    min = 999999
    index = coordinate + 'pos'
    for point in points:
        if point[index] < min:
            min = point[index]
        if point[index] > max:
            max = point[index]
    return min, max


def print_state(point):
    sizeX = 100
    sizeY = 100
    image = [['.' for _ in range(sizeX)] for _ in range(sizeY)]
    minX, maxX = minmax(points, 'x')
    centerX = (maxX + minX) // 2
    minY, maxY = minmax(points, 'y')
    centerY = (maxY + minY) // 2
    for point in points:
        if abs(point['xpos'] - centerX) < sizeX//2 and\
           abs(point['ypos'] - centerY) < sizeY//2:
            image[point['ypos'] - centerY + 50
                  ][point['xpos'] - centerX + 50] = '#'
    for line in image:
        print(''.join(line))


second = 0
minY, maxY = minmax(points, 'y')

while(abs(maxY - minY) > 10):
    points = move(points)
    minY, maxY = minmax(points, 'y')
    second += 1
    if abs(maxY - minY) < 20:
        print_state(points)
        print(second)
