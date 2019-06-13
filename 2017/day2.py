import sys

with open('day2-input') as f:
    input_data = f.read()

sum = max = 0
min = sys.maxsize

for line in input_data.splitlines():
    for number in line.split():
        number = int(number)
        if number < min:
            min = number
        if number > max:
            max = number

    sum += max-min
    max, min = 0, sys.maxsize


print(sum)

# part 2

sum = 0


for line in input_data.splitlines():
    def loop(line):
        global sum
        for i, number in enumerate(line.split()):
            number = int(number)
            if number == 0:
                break
            for y in range(i + 1, len(line.split())):
                list = line.split()
                y = int(list[y])
                if y == 0:
                    break
                if number < y:
                    if y % number == 0:
                        sum += y // number
                        return
                else:
                    if number % y == 0:
                        sum += number // y
                        return

    loop(line)


print(sum)
