puzzle_input = 7403


def calculatePower(x, y, puzzle_input):
    rack_id = x + 10
    power = rack_id * y
    power += puzzle_input
    power *= rack_id
    power = (power // 100) % 10
    return power - 5


grid = [[0 for _ in range(300)] for _ in range(300)]
for y in range(300):
    for x in range(300):
        grid[y][x] = calculatePower(x, y, puzzle_input)


max_power = -9999
max_x, max_y = 0, 0

for y in range(298):
    for x in range(298):
        power = 0
        for j in range(3):
            for i in range(3):
                power += grid[y + j][x + i]
        if power > max_power:
            max_power = power
            max_x, max_y = x, y

print(str(max_x) + ", " + str(max_y))

# part 2:

max_power = -9999
max_x, max_y, max_size = 0, 0, 0

powers = [[0 for _ in range(300)] for _ in range(300)]

powers[0][0] = grid[0][0]

for size in range(2, 301):
    print(size)
    print(str((size * 2) * (301 - size) * (301 - size)).rjust(30))
    for y in range(301 - size):
        for x in range(301 - size):
            power = powers[y][x]
            for j in range(size):
                power += grid[y + j][x + size - 1]
            for i in range(size - 1):
                power += grid[y + size - 1][x + i]
            powers[y][x] = power
            if power > max_power:
                max_power = power
                max_x, max_y, max_size = x, y, size

print(str(max_x) + ", " + str(max_y) + ", " + str(max_size))
