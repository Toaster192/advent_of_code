day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

sum = 0

for number in data:
    sum += int(number)

print(sum)

# part 2:

sum = 0

sum_list = [0]

done = False
while not done:
    for number in data:
        sum += int(number)

        if sum in sum_list:
            done = True
            break

        sum_list.append(sum)

print(sum)
